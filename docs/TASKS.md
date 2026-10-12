# Quadro de tarefas

Escopo autorizado: Sprint 4, entrega técnica concluída para revisão.
Desenvolvimento interrompido; Sprint 5 não autorizada. Manter uma tarefa
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

## Sprint 1 — concluída, aprovada e integrada

| ID | Próxima tarefa | Dependência | Status |
| --- | --- | --- | --- |
| S1-01 | Criar uma Creature e atualizar posição por dt | Exemplos do PRD aprovados | Concluída |
| S1-02 | Testar movimento e reflexão nas bordas | 17 testes de movimento aprovados; raio e cantos | Concluída |
| S1-03 | Desenhar e gerar 10 criaturas | População, desenho e integração aprovados na suíte | Concluída |
| S1-04 | Separar tempo lógico e renderização | Cadências de 100, 10 e 1 FPS simulados produzem 60 passos/s | Concluída |
| S1-05 | Executar testes e verificar aplicação | 33 testes, compileall, pip check e verificação X11 aprovados | Concluída |
| S1-06 | Produzir GIF de 15 segundos | docs/media/sprint1.gif: 800 × 600, 225 quadros distintos, 15 s | Concluída |
| S1-07 | Atualizar documentação e memória | Decisões, evidências, limites e entrega para revisão | Concluída |
| S1-08 | Registro e integração da Sprint 1 | Commit 0f32887; PR #1 integrado à main, conforme usuário | Concluída pelo usuário |

## Sprint 2 — concluída, aprovada e integrada pelo PR #3

| ID | Tarefa | Critério / evidência | Status |
| --- | --- | --- | --- |
| S2-01 | Atualizar autorização e continuidade | Sprint 1 aprovada/PR #1; Sprint 2 autorizada; Sprint 3 bloqueada | Concluída |
| S2-02 | Criar Food e população inicial de alimentos | 75 unidades dentro dos limites; domínio sem Pygame | Concluída |
| S2-03 | Implementar busca e exploração | Alvo visível mais próximo; nova direção a cada 1–3 s sem alvo | Concluída |
| S2-04 | Implementar consumo e energia | Colisão remove alimento; ganho 45, teto 130 e fórmula do PRD | Concluída |
| S2-05 | Remover mortos e repor comida | Remoção segura; 1 unidade/s até 125; extinção funcional | Concluída |
| S2-06 | Validar regras e regressão; demonstrar alimentação | 71 testes aprovados; GIF de 6 s fora da tela | Concluída |
| S2-07 | Revisar código e entregar documentação | Revisão, README, arquitetura, evidências e limites registrados | Concluída |
| S2-08 | Aprovar e integrar a Sprint 2 | PR #3, merge 3b75b6e; validação manual Ubuntu sem erros | Concluída pelo usuário |

## Sprint 3 — concluída, aprovada e integrada pelo PR #4

| ID | Tarefa | Critério / evidência | Status |
| --- | --- | --- | --- |
| S3-01 | Preparar estado e conferir develop/main | Base 3b75b6e, origin/main igual, 71 testes aprovados | Concluída |
| S3-02 | Adicionar idade, cooldown, ID e geração básicos | Idade por dt, cooldown 10 s, IDs não reutilizados | Concluída |
| S3-03 | Implementar nascimento com transferência | Idade ≥10, energia ≥110, cooldown zero; transferência 45 | Concluída |
| S3-04 | Aplicar população e contadores com segurança | Filhotes aguardam próximo passo; mortes contadas uma vez | Concluída |
| S3-05 | Testar reprodução, determinismo e regressões | 103 testes aprovados; regras, cadências, limites e extinção | Concluída |
| S3-06 | Demonstrar nascimentos pelas regras reais | GIF de 15 s; seed 42, 60 s lógicos, 28 nascimentos e 5 mortes | Concluída |
| S3-07 | Revisar código, documentar e entregar | Revisão estática, verificações e memória atualizadas | Concluída |
| S3-08 | Executar aplicação manualmente no Ubuntu | Usuário relatou execução do EvoLife sem identificar erros; 103 testes automatizados anteriores preservados | Concluída pelo usuário |
| S3-09 | Revisão técnica, aprovação e integração | PR #4, merge 96ab068 confirmado pelo usuário e Git | Concluída pelo usuário |

## Sprint 4 — entrega técnica concluída para revisão

| ID | Tarefa | Critério / evidência | Status |
| --- | --- | --- | --- |
| S4-01 | Preparar estado e conferir develop/main | Base limpa 96ab068; branches iguais; 103 testes aprovados | Concluída |
| S4-02 | Estruturar e validar os três genes | Genes imutáveis e propriedades compatíveis; validação executada | Concluída |
| S4-03 | Implementar herança, mutação e linhagem | 12% por gene; normal de 8%; RNG próprio; parent_id | Concluída |
| S4-04 | Testar genética e preservar regressões | 192 testes aprovados; 103 anteriores e 89 genéticos | Concluída |
| S4-05 | Demonstrar duas gerações descendentes | Gerações 0–3; relatório reproduzível; GIF 800 ×600, 225 quadros, 15 s | Concluída |
| S4-06 | Revisar código, documentar e entregar | Revisão estática, compileall, pip check, PRD, diff check e memória | Concluída |

Não iniciar Sprint 5 nem realizar commits, pushes ou PRs automaticamente.

As demais entregas estão em `SPRINTS.md` e no PRD. Aprendizado desta fundação:
a distribuição instalada pode mudar por compatibilidade sem alterar o nome
do módulo importado; um teste SDL sem tela e uma inspeção visual são evidências distintas.

Aprendizado da Sprint 1: velocidade é medida em pixels/s e multiplicada por
dt; limitar FPS não define o tempo lógico. A reflexão precisa considerar o
raio e o deslocamento restante para manter o círculo inteiro dentro do mundo.
