# Arquitetura do EvoLife

## Escopo implementado

A Sprint 0 atende RF-01: abrir, redesenhar e fechar a janela de 800 × 600.
A Sprint 1 acrescenta RF-02 e RF-03: dez criaturas se movem automaticamente,
desenhadas como círculos, com reflexão nas bordas e lógica independente do FPS.
A Sprint 2 implementa RF-04, RF-05 e RF-06: alimento, busca, consumo,
metabolismo, morte e reposição; o mundo continua funcional após extinção.
A Sprint 3 implementa RF-07: idade, cooldown, nascimento por transferência e
contadores. A Sprint 4 implementa RF-08: Genes imutáveis, herança com mutações
limitadas, parâmetros configuráveis e rastreamento por parent_id.

| Arquivo | Responsabilidade |
| --- | --- |
| `main.py` | Janela, eventos, relógio, acumulador e chamada das camadas |
| `evolife/config.py` | Janela, sobrevivência, reprodução, limites e mutação |
| `evolife/creature.py` | Estado, genes, movimento, busca, energia e ciclo de vida |
| `evolife/world.py` | Gerador próprio, população, interações, nascimento, morte e totais |
| `evolife/food.py` | Posição imutável de uma unidade de alimento, sem Pygame |
| `evolife/genetics.py` | Genes, parâmetros validados, cópia, sorteio e limites |
| `evolife/renderer.py` | Fundo, pontos verdes e círculos, sem atualizar regras |
| `scripts/demonstrate_genetics.py` | Cenário padrão reproduzível, relatório e mídia opcional |

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
sobrevivência, dentro das faixas do PRD. A Sprint 4 agrupa esses atributos em
Genes sem mudar sua inicialização. Creature, Food, Genes e World não dependem
de Pygame.

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
disputas; uma unidade nunca fornece energia a duas criaturas. Na Sprint 2 ainda não havia contadores
de mortes ou nascimentos; a Sprint 3 acrescentou esses totais ao domínio,
sem antecipar o painel de indicadores.

A reposição ocorre ao final: acumula frações de unidade a 1/s, cria unidades
inteiras até 125 e zera crédito quando o mapa enche, evitando reposição em
rajada após consumo. Tolerância absoluta de 1e-12 trata a soma de passos fixos
perto de inteiros, sem arredondamento relativo. Reposição independe de população.
A aplicação continua usando 1/60 s; passos maiores isolados não substituem a
sequência fixa para comparar decisões e colisões de sobrevivência.

### ADR-009 — Reprodução por transferência e aplicação ao final

Creature guarda age_seconds e reproduction_cooldown, ambos inicialmente zero.
World avança os dois por dt para cada criatura viva. Elegibilidade é verificada
após alimentação e gasto do passo: idade ≥10 s, energia ≥110 e espera encerrada.
Ao nascer, o progenitor perde 45 e recebe cooldown 10 s; o filhote recebe 45,
idade zero, cooldown zero, geração do progenitor +1 e speed/vision/efficiency
copiados na Sprint 3; a Sprint 4 acrescenta mutação conforme ADR-010.
A operação de nascimento conserva energia; o metabolismo do passo
continua consumindo energia separadamente.

World usa contador crescente de IDs, iniciando em zero, sem reutilização
após mortes. A população inicial tem geração zero e não incrementa births_total.
Criaturas isoladas têm id None até serem inseridas e processadas no mundo;
World também atribui IDs em cenários preparados. A aplicação não edita IDs.
Na Sprint 3 não havia parent_id; a Sprint 4 registra o ID do progenitor no
filhote. Criaturas iniciais mantêm parent_id None. O ID permanece no filhote
mesmo depois de o progenitor sair da população; World não guarda mortos.

A posição do filhote usa ângulo do RNG próprio e distância de 16 pixels,
centralizada em config como 2 raios +2. Cada coordenada é limitada ao intervalo
válido do centro; nas bordas os círculos podem se sobrepor, sem colisão entre
criaturas. O ângulo também define a direção inicial; intervalo de exploração
é sorteado pelo mesmo RNG. IDs e contadores não consomem números aleatórios.

A iteração mantém listas separadas de sobreviventes e recém-nascidos. Cada
progenitor gera no máximo um filhote por passo. World aplica a nova população
após percorrer a lista anterior; filhotes não se movem, comem, envelhecem ou
reproduzem no passo de nascimento. Isso evita atualização recursiva. Mortos
no início ou ao esgotar energia são removidos e contados uma única vez.
Births_total e deaths_total ficam disponíveis no domínio, sem HUD ou Metrics.

O tempo fixo continua na aplicação. Testes das três cadências incluem nascimento,
idade, energia e contadores; mesma seed e mesma sequência de passos repetem
estado, alimento, IDs e eventos. Extinção não recria população automaticamente.

### ADR-010 — Genes imutáveis e compatibilidade de Creature

`evolife/genetics.py` contém `Genes`, dataclass congelada com exatamente
speed, vision e efficiency. A construção rejeita valores não numéricos,
booleanos, não finitos ou fora dos intervalos inclusivos de config:

| Gene | Intervalo | Desvio padrão default |
| --- | --- | --- |
| speed | 25–90 pixels/s | 5,2 pixels/s |
| vision | 35–160 pixels | 10 pixels |
| efficiency | 0,8–1,2 | 0,032 |

Imutabilidade evita alterar genes de um progenitor por meio do filhote e
permite comparação direta por valor. `Creature` armazena somente `_genes`;
`genes` expõe essa estrutura. Propriedades speed/vision/efficiency preservam
o acesso anterior e, ao receber valor, substituem Genes por uma cópia validada.
O construtor aceita a assinatura anterior (inclusive argumentos posicionais)
ou `genes=Genes(...)`; mistura das duas formas é rejeitada. O construtor
explícito mantém a fonte única sem duplicar os três atributos; a dataclass
continua fornecendo igualdade de estado para testes de determinismo.

### ADR-011 — Mutação por nascimento pelo RNG do mundo

`MutationSettings` é imutável: probability finita de 0 a 1; stddev_fraction
finita e não negativa. Defaults 0,12 e 0,08 ficam em config. `World` aceita
`mutation_probability` e `mutation_stddev_fraction` como argumentos nomeados,
valida antes de criar a população e usa esses parâmetros nos nascimentos.

`Genes.inherit(world.random, world.mutation_settings)` cria outra estrutura.
Na ordem fixa speed → vision → efficiency, consome um `random()` para cada
gene. Se o sorteio for menor que probability, soma `gauss(0, sigma)`, com
sigma = stddev_fraction × (máximo − mínimo), e limita ao intervalo.
Cada decisão ocorre em cada nascimento; não há direção planejada, avaliação
de sobrevivência, nova característica ou RNG global. Desvio zero e clamp
podem produzir valor idêntico apesar de um sorteio de mutação positivo.
Com probability zero, os três sorteios continuam ocorrendo, sem gauss.

World conserva todos os requisitos de elegibilidade, energia e agenda da
Sprint 3, atribuindo ID único crescente, geração +1 e parent_id. Os genes
alteram diretamente movimento, percepção e custo pela fórmula preservada:
`(0.55 + 0.012 * speed + 0.003 * vision) * efficiency`. Sobrevivência e
reprodução resultam de alimento e gasto, sem favorecimento artificial.

Mesma seed, parâmetros e sequência de passos reproduzem genes, linhagem,
estado e RNG nesta implementação. Sorteios novos mudam a sequência em relação
à Sprint 3; não se espera repetir os números de sua mídia histórica.
Sem genealogia persistente no World: parent_id é a referência mínima; a
demonstração guarda snapshots locais dos nascimentos para inspecionar mortos.

### ADR-012 — Evidências genéticas fora da interface

O script de demonstração usa World e Renderer reais, com seed 42 e 3600
passos fixos; não edita energia, idade, cooldown ou alimento. Relata genes
de cada progenitor/filhote e mudanças efetivas em Markdown. A opção `--gif`
usa Pygame fora da tela e ffmpeg já disponível para 225 quadros, 800 ×600,
15 s a 4x; texto e anéis são exclusivos da mídia. Execução sem `--gif` não
importa Pygame nem depende de ffmpeg. Não há HUD, médias ou CSV na aplicação.
Parâmetros, resultados e limites em [GENETICS_DEMO.md](GENETICS_DEMO.md).

Testes usam RNG controlado para decisões, sinais e sigmas, evitando estimar
probabilidades por amostragem. Integração cobre herança, mutações, parent_id,
duas gerações descendentes, energia, fenótipos, extinção e determinismo.
A suíte da Sprint 3 conserva seus 103 casos. Testes de cópia/metabolismo e
cadências desativam mutação explicitamente; o teste de contato usa visão 35
e isola steer, substituindo a visão zero fora dos limites do PRD.

## Componentes por sprint

| Componente | Responsabilidade | Introdução prevista |
| --- | --- | --- |
| `Creature` | Estado, movimento, sobrevivência e ciclo básico | Sprint 1; sobrevivência na 2; ciclo na 3 |
| `World` | População, interações e totais de eventos | Sprint 1; sobrevivência na 2; reprodução na 3 |
| `Renderer` | Desenho do mundo, separado das regras | Implementado na Sprint 1; HUD futuro |
| `Food` | Estado de alimento; consumo resolvido por World | Implementado na Sprint 2 |
| `Genetics` | Genes, herança, mutação e limites | Implementado na Sprint 4 |
| `Metrics` | Agregações, amostragem e CSV | Sprint 5 |

O passo fixo, o gerador próprio e o domínio independente de Pygame já existem.
Nascimentos e mortes são aplicados fora da iteração da população. Ambos
estão implementados na Sprint 3. As regras são testáveis sem Pygame.

## Fora do escopo atual

Indicadores, CSV, pausa, reinício e controles de sementes aguardam suas
sprints. Sprint 5 não autorizada. Não criar
arquivos vazios para esses componentes. Evolução e aprendizado individual
são conceitos distintos; redes neurais pertencem ao backlog pós-1.0.
