# Arquitetura do EvoLife

## Escopo implementado

A Sprint 0 atende RF-01: abrir, redesenhar e fechar a janela de 800 × 600.
A Sprint 1 acrescenta RF-02 e RF-03: dez criaturas se movem automaticamente,
desenhadas como círculos, com reflexão nas bordas e lógica independente do FPS.
A Sprint 2 implementa RF-04, RF-05 e RF-06: alimento, busca, consumo,
metabolismo, morte e reposição; o mundo continua funcional após extinção.

| Arquivo | Responsabilidade |
| --- | --- |
| `main.py` | Janela, eventos, relógio, acumulador e chamada das camadas |
| `evolife/config.py` | Janela, movimento, visão, energia, exploração e alimento |
| `evolife/creature.py` | Estado, reflexão, busca, exploração e energia, sem Pygame |
| `evolife/world.py` | Gerador próprio, população, interações, morte e reposição |
| `evolife/food.py` | Posição imutável de uma unidade de alimento, sem Pygame |
| `evolife/renderer.py` | Fundo, pontos verdes e círculos, sem atualizar regras |

`evolife/config.py` concentra os parâmetros usados nesta sprint. O pacote
`evolife` não inicializa Pygame na importação. A função `main()` retorna zero
ao fechar a janela, receber Esc ou Ctrl+C; `finally` libera os recursos também
se a inicialização ou a renderização falhar. Falhas de vídeo reais continuam
visíveis no terminal, em vez de serem ocultadas.

Apenas o subsistema de vídeo é inicializado nesta sprint. Isso fornece janela
e eventos sem acessar um dispositivo de áudio desnecessário. Os testes usam
Pygame/SDL reais com driver `dummy`, sem dependência de um desktop.

## Decisões técnicas

### ADR-001 — pygame-ce 2.5.8 com Python 3.14

**Status:** adotada por instrução do usuário em 11/10/2026.

**Contexto:** o `.venv` existente usa Python 3.14.4. A tentativa de instalar
`pygame` selecionou o código-fonte 2.6.1 e falhou porque `sdl2-config` não está
disponível. O usuário determinou preservar Python e ambiente virtual, sem
sudo nem instalação de bibliotecas do sistema.

**Decisão:** usar `pygame-ce==2.5.8` como única dependência de execução. A
[página oficial da versão](https://pypi.org/project/pygame-ce/2.5.8/) inclui
Python 3.14 entre as versões suportadas. O código mantém `import pygame`.
Instalar apenas wheels com `--only-binary=:all:`; não compilar dependências.

**Consequências:** evita trocar o interpretador ou instalar SDL de desenvolvimento
no sistema. Não coexistir com a distribuição `pygame`, pois ambas fornecem
o mesmo módulo. A disponibilidade do wheel precisa ser verificada em cada
plataforma. A escolha altera a distribuição instalada, sem modificar o PRD
ou antecipar funcionalidades. As versões efetivamente testadas ficam na memória.

### ADR-002 — Dependências de execução e desenvolvimento separadas

`requirements.txt` fixa pygame-ce 2.5.8. `requirements-dev.txt` referencia
esse arquivo e fixa pytest 9.1.1 somente para desenvolvimento. O ambiente virtual
é local e ignorado pelo Git. Não são necessários frameworks, backend, banco,
ferramentas de empacotamento ou serviços externos nesta entrega.

### ADR-003 — Memória comum em Markdown

`AGENTS.md` direciona Codex CLI e OpenCode CLI para `docs/PROJECT_STATE.md`
na abertura e no encerramento de sessões. Essa memória registra estado,
decisões, evidências e próxima ação; `TASKS.md` mantém o quadro de execução.
Nenhuma informação essencial depende de uma conversa ou de configuração
privada em `.codex`/`.agents`. Em trabalho simultâneo autorizado, um responsável
consolida a memória para evitar sobrescritas.

### ADR-004 — Estrutura incremental e testes de ciclo de vida

Na Sprint 0 existiam apenas entrada, pacote e configuração. Testes de integração
verificam o contrato RF-01 e limpeza diante de falhas. O driver `dummy` permite
automação; a avaliação manual da janela continua sendo uma evidência distinta.
Na Sprint 1, Creature, World e Renderer entram porque são necessários para
movimento, população e desenho. Não há interfaces abstratas ou motor genérico.

### ADR-005 — Movimento em passos fixos

O relógio mede milissegundos decorridos entre quadros; a aplicação os converte
em segundos e acumula. Enquanto houver tempo suficiente, chama
`World.update(1/60)`; o tempo restante fica para o próximo quadro. Depois
`Renderer.draw(world)` desenha o estado, sem modificá-lo. Um quadro pode ter
zero ou vários passos lógicos. `math.isclose` trata arredondamento na comparação
do acumulador com o passo, evitando perder um passo na fronteira de floats.

O limite de 60 FPS controla somente a renderização. Não há descarte de tempo
decorrido nem interpolação nesta sprint. Uma pausa longa da aplicação pode
exigir vários passos de recuperação antes do próximo desenho; otimizações
ficam para quando houver medição que as justifique.

### ADR-006 — Reflexão do círculo nas bordas

Posições são centros em ponto flutuante; direções são radianos, com zero para
a direita e y crescendo para baixo. Movimento usa `cos(direction) * speed * dt`
e `sin(direction) * speed * dt`. Os centros ficam em `[raio, largura - raio]`
e `[raio, altura - raio]`, mantendo o círculo inteiro dentro da janela.

A colisão espelha o excesso de deslocamento e inverte a componente da
velocidade correspondente. Isso preserva a distância restante após a batida,
inclusive nos cantos ou em um dt que atravesse várias bordas. Um helper curto
trata cada eixo; `atan2` recompõe a direção quando houver reflexão. Pygame
recebe posições arredondadas somente ao desenhar, sem arredondar o estado.

### ADR-007 — Inicialização e limites do escopo

`World` possui `random.Random` próprio, como prevê a seção 6.1 do PRD.
A semente padrão 42 em config facilita demonstrar a mesma distribuição
inicial; não há interface de controle de sementes ou protocolo de experimentos
nesta sprint. São criadas dez criaturas com posições, direções e velocidades
sorteadas no intervalo do PRD (25 a 90 pixels/s), energia inicial 100,
raio de desenho 7 e cor azul clara. Raio e cor são decisões visuais locais.

Na Sprint 1, energia permanecia constante e a direção mudava nas bordas.
Na Sprint 2, visão inicial 100 e eficiência 1,0 são atributos necessários à
sobrevivência, dentro das faixas do PRD; genes/herança aguardam Sprint 4.
Creature, Food e World continuam sem dependência de Pygame.

### ADR-008 — Sobrevivência em passos fixos

Food guarda x/y e é desenhado como ponto verde de raio 3, menor que a criatura.
Há 75 unidades iniciais, geradas pelo mesmo RNG do mundo. A busca compara
distâncias ao quadrado; alcance e contato são inclusivos. Empates de distância
usam a ordem dos alimentos. Sem alvo, a criatura mantém a direção até vencer
o intervalo sorteado de 1 a 3 s; o cronômetro avança apenas durante exploração.

World valida dt antes de qualquer alteração. dt zero não muda estado. Para
cada criatura viva, resolve contato inicial, direção, movimento com reflexão,
contato final e gasto energético. Isso permite comida gerada na posição inicial
e recuperação da energia antes do gasto do passo. Mortos anteriores não agem.
O gasto é a fórmula original do PRD, proporcional a dt, limitado inferiormente
a zero. Cada unidade fornece 45, até 130, antes do gasto do passo.

Alimentos consumidos saem por uma nova lista, e criaturas mortas saem por uma
lista de sobreviventes aplicada após o percurso. A ordem da população resolve
disputas; uma unidade nunca fornece energia a duas criaturas. Não há contadores
de mortes ou nascimentos, pois indicadores pertencem às próximas sprints.

A reposição ocorre ao final: acumula frações de unidade a 1/s, cria unidades
inteiras até 125 e zera crédito quando o mapa enche, evitando reposição em
rajada após consumo. Tolerância absoluta de 1e-12 trata a soma de passos fixos
perto de inteiros, sem arredondamento relativo. Reposição independe de população.
A aplicação continua usando 1/60 s; passos maiores isolados não substituem a
sequência fixa para comparar decisões e colisões de sobrevivência.

## Componentes por sprint

| Componente | Responsabilidade | Introdução prevista |
| --- | --- | --- |
| `Creature` | Estado, posição e movimento, sem Pygame | Implementado na Sprint 1 |
| `World` | População e interações de sobrevivência | Sprint 1; sobrevivência na Sprint 2 |
| `Renderer` | Desenho do mundo, separado das regras | Implementado na Sprint 1; HUD futuro |
| `Food` | Estado de alimento; consumo resolvido por World | Implementado na Sprint 2 |
| `Genetics` | Herança, mutação e limites | Sprint 4 |
| `Metrics` | Agregações, amostragem e CSV | Sprint 5 |

O passo fixo, o gerador próprio e o domínio independente de Pygame já existem.
Mortes já são aplicadas fora da iteração da população. Nascimentos aguardam
a Sprint 3 autorizada; seguirão o mesmo princípio. As regras são testáveis sem Pygame.

## Fora do escopo atual

Reprodução, genes herdáveis, indicadores, CSV, pausa, reinício e controles
de sementes aguardam suas sprints. A Sprint 3 não está autorizada. Não criar
arquivos vazios para esses componentes. Evolução e aprendizado individual
são conceitos distintos; redes neurais pertencem ao backlog pós-1.0.
