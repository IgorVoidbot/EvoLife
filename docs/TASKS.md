# Quadro de tarefas

Escopo autorizado: Sprint 0 e documentação de fundação. Manter uma tarefa
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
| S0-14 | Primeiro commit do PRD | Requer autorização explícita do usuário | Suspensa pelo usuário |

## Backlog, sem execução autorizada

| ID | Próxima tarefa | Dependência | Status |
| --- | --- | --- | --- |
| S1-01 | Criar uma Creature e atualizar posição por dt | Autorizar Sprint 1 | Não iniciada |
| S1-02 | Testar movimento e reflexão nas bordas | S1-01 | Não iniciada |
| S1-03 | Desenhar e gerar 10 criaturas | S1-02 | Não iniciada |

As demais entregas estão em `SPRINTS.md` e no PRD. Aprendizado desta fundação:
a distribuição instalada pode mudar por compatibilidade sem alterar o nome
do módulo importado; um teste SDL sem tela e uma inspeção visual são evidências distintas.
