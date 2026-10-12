# Plano de sprints

Fonte: `EvoLife_PRD_Roadmap.md`, versão 1.0. O documento original permanece
inalterado. A cadência sugerida é semanal; os critérios de aceite orientam
a conclusão, sem impor datas. Sprint 2 autorizada; Sprint 3 não autorizada.

| Sprint | Esforço do PRD | Entrega / portão de aceite | Status |
| --- | --- | --- | --- |
| 0 | 2–3 h | Repositório, venv, dependências, README; janela 800 × 600 abre, redesenha e fecha | Concluída e registrada pelo usuário em 73d5e04 |
| 1 | 4–6 h | 10 criaturas se movem por tempo decorrido; bordas verificadas | Concluída, aprovada e integrada à main pelo PR #1 |
| 2 | 6–8 h | Comida, busca, consumo, energia, morte e reposição | Entrega técnica concluída; aguarda revisão |
| 3 | 5–7 h | Idade, cooldown, reprodução e transferência de energia | Não iniciada e não autorizada |
| 4 | 6–8 h | Genes herdáveis, mutação limitada e gerações; MVP 0.1 | Não iniciada |
| 5 | 4–6 h | Indicadores, médias, amostras e exportação CSV | Não iniciada |
| 6 | 3–5 h | Pausa, reinício, passo único e repetibilidade por semente | Não iniciada |
| 7 | 5–8 h | Testes, estabilidade por 15 minutos, mídia e release 1.0 | Não iniciada |
| 8 | 5–9 h | Predadores e ambientes, após a versão 1.0 | Backlog opcional |
| 9 | 8–15+ h | Controlador neural com hipótese e comparação, após 1.0 | Backlog opcional |

## Sprint 0 — fundação concluída

- Reutilizar o Git existente, sem reinicializar ou fazer commits.
- Preservar Python 3.14 e `.venv`; instalar pygame-ce 2.5.8 e pytest apenas
  como pacotes pré-compilados, sem instalar componentes no sistema operacional.
- Entregar janela preta de 800 × 600, loop responsivo e saída com Esc/fechar.
- Criar README e .gitignore, instruções para ambos os CLIs e documentação.
- Registrar testes e dificuldades na memória e atualizar o quadro de tarefas.

A Sprint 0 foi registrada pelo usuário em `73d5e04`. Não fazer novos commits
sem autorização explícita.
A demonstração prevista no PRD é um vídeo de 5 segundos; sua produção e a
avaliação visual devem aparecer separadas dos resultados automatizados.

**Evidências desta entrega:** sete testes aprovados com SDL dummy, verificação
automatizada com janela real X11 (374 quadros em 6,29 s e encerramento sem erro)
e [vídeo de 5 segundos](media/sprint0.mp4). Não houve avaliação manual por uma
pessoa; os resultados e limites estão registrados na memória compartilhada.

## Sprint 1 — plano executado

Começar com uma `Creature`, movimento
por `dt` e teste de `(100, 100)` para `(120, 100)` em 0,5 s a 40 pixels/s.
Depois tratar bordas e gerar as outras nove criaturas. Separar domínio,
população e desenho; usar passos fixos de 1/60 s. Não implementar metabolismo,
comida ou controles novos. Entregar GIF de 15 segundos e testes; interromper
ao concluir e aguardar revisão, como ocorreu na entrega técnica original.

**Evidências:** 33 testes aprovados (sete da Sprint 0), incluindo movimento,
reflexão e cadências de renderização; verificação gráfica X11 com dez criaturas
e encerramento sem erro; [GIF de 15 segundos](media/sprint1.gif).
A Sprint 1 foi aprovada e integrada à main pelo PR #1, conforme confirmação
do usuário. O agente não realizou commit automático.

## Sprint 2 — entrega técnica concluída para revisão

Implementar Food com 75 unidades iniciais, busca do alimento visível mais
próximo, exploração sem alvo, consumo com ganho de 45 e teto de 130, gasto
energético pela fórmula do PRD, remoção segura de mortos e reposição de 1/s
até 125 alimentos. Validar energia, busca, competição, reposição e extinção,
preservando movimento, bordas, tempo fixo e encerramento. Demonstrar uma
criatura com fome comendo. Interromper para revisão; Sprint 3 não autorizada.

**Evidências:** 71 testes aprovados com SDL dummy; busca, energia, consumo,
morte, reposição e extinção validados. Pip check, compileall e hash do PRD
aprovados. [GIF de alimentação de 6 segundos](media/sprint2.gif), renderizado
fora da tela com legendas exclusivas da demonstração. Não houve validação
da Sprint 2 com driver gráfico de desktop nem inspeção manual pelo usuário.
Entrega técnica concluída, desenvolvimento interrompido e aguardando revisão.
