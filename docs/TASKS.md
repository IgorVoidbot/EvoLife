# Quadro de tarefas

Escopo autorizado: Sprint 1. Manter uma tarefa
de implementação em andamento por vez. Atualizar este arquivo ao concluir
cada tarefa; evidências detalhadas ficam em `PROJECT_STATE.md`.

| ID | Tarefa | Critério / evidência | Status |
| --- | --- | --- | --- |
| S0-01 | Ler PRD e inspecionar arquivos existentes | Escopo registrado; hash do PRD preservado | Concluída |
| S0-02 | Preparar instruções para Codex CLI e OpenCode CLI | AGENTS.md comum, com restrições e fluxo de continuidade | Concluída |
| S0-03 | Criar arquitetura, sprints, tarefas e memória | Quatro documentos em docs/ | Concluída |
| S0-04 | Reutilizar Git e criar .gitignore | Git existente preservado; venv e caches ignorados | Concluída |
| S0-05 | Preparar pacote Python mínimo | main.py, evolife/__init__.py e config.py | Concluída |
| S0-06 | Criar e preservar ambiente virtual Python 3.14 | .venv existente mantido | Concluída |
| S0-07 | Instalar pygame-ce e pytest via wheels | pygame-ce 2.5.8, pytest 9.1.1, import e pip check aprovados | Concluída |
| S0-08 | Implementar RF-01 | Janela preta 800 × 600, eventos e encerramento seguro; 7 testes aprovados | Concluída |
| S0-09 | Documentar instalação, uso e decisões | README e ADR de compatibilidade | Concluída |
| S0-10 | Executar verificações automatizadas | 7 testes, pip check, compileall e hash do PRD aprovados | Concluída |
| S0-11 | Verificar janela no desktop | Teste automatizado X11: 374 quadros em 6,29 s, saída 0 e recursos liberados | Concluída |
| S0-12 | Gravar demonstração de 5 segundos | docs/media/sprint0.mp4; ffprobe confirma 5 s e 800 × 600 | Concluída |
| S0-13 | Atualizar memória e entregar resumo | Estado, dificuldades resolvidas, evidências e próxima ação registrados | Concluída |
| S0-14 | Primeiro commit do PRD | Commit 73d5e04 feito pelo usuário | Concluída pelo usuário |

## Sprint 1 — entrega para revisão

| ID | Próxima tarefa | Dependência | Status |
| --- | --- | --- | --- |
| S1-01 | Criar uma Creature e atualizar posição por dt | Exemplos do PRD aprovados | Concluída |
| S1-02 | Testar movimento e reflexão nas bordas | 17 testes de movimento aprovados; raio e cantos | Concluída |
| S1-03 | Desenhar e gerar 10 criaturas | População, desenho e integração aprovados na suíte | Concluída |
| S1-04 | Separar tempo lógico e renderização | Cadências de 100, 10 e 1 FPS simulados produzem 60 passos/s | Concluída |
| S1-05 | Executar testes e verificar aplicação | 33 testes, compileall, pip check e verificação X11 aprovados | Concluída |
| S1-06 | Produzir GIF de 15 segundos | docs/media/sprint1.gif: 800 × 600, 225 quadros distintos, 15 s | Concluída |
| S1-07 | Atualizar documentação e memória | Decisões, evidências, limites e entrega para revisão | Concluída |
| S1-08 | Commit da Sprint 1 | Requer autorização explícita | Suspenso pelo usuário |

Sprint 2: não iniciada e não autorizada.

As demais entregas estão em `SPRINTS.md` e no PRD. Aprendizado desta fundação:
a distribuição instalada pode mudar por compatibilidade sem alterar o nome
do módulo importado; um teste SDL sem tela e uma inspeção visual são evidências distintas.

Aprendizado da Sprint 1: velocidade é medida em pixels/s e multiplicada por
dt; limitar FPS não define o tempo lógico. A reflexão precisa considerar o
raio e o deslocamento restante para manter o círculo inteiro dentro do mundo.
