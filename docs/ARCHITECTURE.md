# Arquitetura do EvoLife

## Escopo implementado

A Sprint 0 atende RF-01 do PRD: abrir, redesenhar e fechar uma janela preta
de 800 × 600. `main.py` processa a fila de eventos, desenha o fundo e limita
a renderização a 60 quadros por segundo. Não existe tempo de simulação ainda.

`evolife/config.py` concentra tamanho, título, cor e limite de FPS. O pacote
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

### ADR-004 — Estrutura mínima e testes de ciclo de vida

Somente entrada, pacote e configuração existem agora. Testes de integração
verificam o contrato RF-01 e limpeza diante de falhas. O driver `dummy` permite
automação; a avaliação manual da janela continua sendo uma evidência distinta.

## Arquitetura planejada, ainda não implementada

| Componente | Responsabilidade | Introdução prevista |
| --- | --- | --- |
| `Creature` | Estado, posição e movimento, sem Pygame | Sprint 1 |
| `World` | Atualização da população e interações | Conforme necessário a partir da Sprint 1 |
| `Renderer` | Desenho do mundo, separado das regras | Sprint 1, quando houver criaturas |
| `Food` | Estado de alimento e consumo | Sprint 2 |
| `Genetics` | Herança, mutação e limites | Sprint 4 |
| `Metrics` | Agregações, amostragem e CSV | Sprint 5 |

Nas sprints autorizadas, o motor deverá avançar em passos fixos de 1/60 s,
independentes do desenho, e usar um `random.Random` próprio com semente.
Nascimentos e mortes serão aplicados fora da iteração da população.
As regras deverão ser testáveis sem importar Pygame. Esses contratos estão
documentados como direção futura, não como implementação da Sprint 0.

## Fora do escopo atual

Criaturas, movimento, bordas, comida, energia, reprodução, genes, indicadores,
CSV, pausa, reinício e controle de sementes aguardam suas sprints. Não criar
arquivos vazios para esses componentes. Evolução e aprendizado individual
são conceitos distintos; redes neurais pertencem ao backlog pós-1.0.
