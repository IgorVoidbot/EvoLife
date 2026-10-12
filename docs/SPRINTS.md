# Plano de sprints

Fonte: `EvoLife_PRD_Roadmap.md`, versão 1.0. O documento original permanece
inalterado. A cadência sugerida é semanal; os critérios de aceite orientam
a conclusão, sem impor datas. Sprint 4 autorizada, entrega técnica concluída
para revisão; desenvolvimento interrompido. Sprint 5 não autorizada.

| Sprint | Esforço do PRD | Entrega / portão de aceite | Status |
| --- | --- | --- | --- |
| 0 | 2–3 h | Repositório, venv, dependências, README; janela 800 × 600 abre, redesenha e fecha | Concluída e registrada pelo usuário em 73d5e04 |
| 1 | 4–6 h | 10 criaturas se movem por tempo decorrido; bordas verificadas | Concluída, aprovada e integrada à main pelo PR #1 |
| 2 | 6–8 h | Comida, busca, consumo, energia, morte e reposição | Concluída, aprovada e integrada pelo PR #3 (3b75b6e) |
| 3 | 5–7 h | Idade, cooldown, reprodução e transferência de energia | Concluída, aprovada e integrada pelo PR #4 (96ab068) |
| 4 | 6–8 h | Genes herdáveis, mutação limitada e gerações; MVP 0.1 | Entrega técnica concluída; aguarda revisão e aprovação |
| 5 | 4–6 h | Indicadores, médias, amostras e exportação CSV | Não iniciada e não autorizada |
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

## Sprint 2 — concluída, aprovada e integrada

Implementar Food com 75 unidades iniciais, busca do alimento visível mais
próximo, exploração sem alvo, consumo com ganho de 45 e teto de 130, gasto
energético pela fórmula do PRD, remoção segura de mortos e reposição de 1/s
até 125 alimentos. Validar energia, busca, competição, reposição e extinção,
preservando movimento, bordas, tempo fixo e encerramento. Demonstrar uma
criatura com fome comendo. Plano da entrega original, concluído e aprovado.

**Evidências:** 71 testes aprovados com SDL dummy; busca, energia, consumo,
morte, reposição e extinção validados. Pip check, compileall e hash do PRD
aprovados. [GIF de alimentação de 6 segundos](media/sprint2.gif), renderizado
fora da tela com legendas exclusivas da demonstração. Não houve validação
da Sprint 2 com driver gráfico de desktop pelo agente. Posteriormente,
o usuário executou aplicação e testes no Ubuntu sem identificar erros.
Sprint 2 aprovada e integrada à main pelo PR #3, merge 3b75b6e.

Registro anterior preservado: Sprint 2 aprovada na revisão de código,
com pequeno ajuste documental recomendado; referências de estado corrigidas
na abertura da Sprint 3.

## Sprint 3 — concluída, aprovada e integrada

Implementar idade, cooldown de 10 s e reprodução assexuada: idade ≥10 s,
energia ≥110 e cooldown encerrado. Transferir 45 para o filhote; copiar
velocidade, visão e eficiência; novo ID e geração do progenitor +1. Posicionar
próximo e dentro das bordas, usando RNG próprio. Aplicar nascimentos e mortes
fora da iteração e registrar totais. Validar bloqueios, conservação, limites,
IDs, determinismo e extinção; demonstrar nascimento com parâmetros registrados.
Plano original preservado: entrega sem mutações, seguida de revisão.

**Evidências:** 103 testes aprovados com SDL dummy; idade, cooldown, bloqueios,
conservação no nascimento, limites, IDs, eventos, extinção e repetibilidade
validados. Revisão estática, pip check, compileall e hash do PRD aprovados.
[GIF de 15 segundos](media/sprint3.gif): configuração padrão, seed 42,
60 s simulados com passos de 1/60 s, 28 nascimentos e 5 mortes. Mídia a 4x,
renderizada fora da tela, com legendas exclusivas da demonstração. População
inicial 10, máxima 34 e final 33. Posteriormente, o usuário executou manualmente
o EvoLife da Sprint 3 no Ubuntu e não identificou erros. Relato separado dos
103 testes automatizados anteriores, cujos resultados foram preservados.
Sprint 3 aprovada na revisão técnica e integrada à main pelo PR #4,
merge 96ab068, conforme usuário e Git local. Sprint 4 autorizada posteriormente.

## Sprint 4 — entrega técnica concluída para revisão

Agrupar speed, vision e efficiency em genes validados; herdar no nascimento
com 12% de mutação independente por gene e normal centrada em zero com
desvio de 8% da amplitude. Limitar aos intervalos do PRD, usando RNG próprio.
Registrar parent_id e preservar geração, IDs, energia e regras da Sprint 3.
Testar herança, limites, determinismo e regressões. Demonstrar duas gerações
descendentes com parâmetros e genes inspecionáveis. Encerrar para revisão,
sem commit, push, PR ou início da Sprint 5.

**Evidências:** 192 testes aprovados com SDL dummy (103 casos anteriores e
89 genéticos); revisão estática, compileall, pip check e hash do PRD aprovados.
[Relatório genético](GENETICS_DEMO.md) reproduzido identicamente com e sem
renderização: seed 42, parâmetros oficiais padrão, 60 s em passos de 1/60 s,
26 nascimentos, 6 mortes, população máxima 34 e final 30, geração máxima 3.
Linhagem 8 → 18 → 25 → 35 demonstra herança e mudanças em speed/efficiency.
[GIF de 15 segundos](media/sprint4.gif), 800 ×600, 225 quadros a 15 FPS,
renderizado fora da tela a 4x, com legendas exclusivas da mídia.
Critérios técnicos do MVP Evolutivo 0.1 atendidos; aprovação do usuário pendente.
Sem evidência de adaptação decorrente desta demonstração isolada; execução
manual da Sprint 4 no desktop e validação Windows pendentes.
