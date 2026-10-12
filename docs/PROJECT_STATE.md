# Memória compartilhada — EvoLife

Última atualização: 12/10/2026, revisão externa e validação da Sprint 4 pelo usuário.

## Protocolo de continuidade

Este documento é a memória comum de Codex CLI, OpenCode CLI e agentes futuros.
Leia-o no início de cada sessão junto com `AGENTS.md` e `TASKS.md`. Atualize
ao terminar tarefas e antes de encerrar; preserve decisões e dificuldades
relevantes. Resultados abaixo representam evidências executadas, não intenções.

## Estado e autorização

- Sprint atual: **4**, **entrega técnica concluída, revisada externamente sem
  problemas bloqueantes e validada pelo usuário no Ubuntu**. Desenvolvimento
  interrompido; sessão atual autorizada somente para documentação.
- Usuário executou a aplicação e a suíte de testes da Sprint 4 no Ubuntu sem
  identificar erros. Relato separado dos **192 testes executados pelo Codex**
  na entrega técnica; não foi informado novo total ou saída detalhada da suíte.
- Commit e push da Sprint 4 realizados pelo usuário: `f90c98f`, presente em
  develop e origin/develop. main e origin/main permanecem em `96ab068`;
  integração da Sprint 4 à main não informada. Sem novos commits pelo agente.
- Sprint 3 concluída, aprovada na revisão técnica e integrada à main pelo
  **PR #4**, merge `96ab068`, confirmado pelo usuário e pelo Git local.
- Usuário executou manualmente o EvoLife da Sprint 3 no Ubuntu e não
  identificou erros; relato registrado ao final, separado dos 103 testes
  automatizados já aprovados.
- Sprint 2 concluída, revisada, aprovada e integrada à main pelo PR #3,
  merge `3b75b6e`, confirmado pelo usuário e presente na develop/origin/main.
- Usuário executou manualmente a aplicação e a suíte de testes da Sprint 2
  no Ubuntu, sem identificar erros; relato registrado ao final deste documento.
- Sprint 1 concluída, aprovada e integrada à main; merge do **PR #1**
  confirmado pelo usuário nesta sessão.
- Sprint 0 concluída e registrada pelo usuário em `73d5e04`.
- Sprint 5: **não autorizada**. Aguardar novas instruções do usuário.
  Novos commits, pushes, PRs ou integração não autorizados nesta sessão.
- PRD original: lido e preservado; não editar.
- Commits, tags, pushes e publicação: não autorizados.
- Preservar Python global 3.14 e `.venv`; não usar sudo, instalar SDL ou
  bibliotecas no sistema operacional, nem alterar permissões automaticamente.
- Se uma instalação falhar, informar erro completo antes de outras alterações
  no ambiente. Instalar exclusivamente pacotes pré-compilados.

## Implementação atual

Sprint 4 implementada: Genes imutáveis e validados, herança com 12% de mutação
independente por gene, normal de desvio 8% da amplitude, limitação ao PRD,
parent_id e geração. Creature mantém propriedades compatíveis; World usa seu
RNG e preserva as regras de energia, reprodução e sobrevivência. 192 testes
aprovados pelo Codex na entrega técnica; demonstração com gerações 0–3.
Critérios técnicos do MVP Evolutivo 0.1 atendidos; revisão externa sem
bloqueantes e validação Ubuntu relatadas posteriormente pelo usuário.
Integração à main não informada. Sem HUD, CSV, controles novos
ou dependências adicionais. Base histórica abaixo; evidências novas ao final.

### Base histórica da Sprint 3

Sprint 3 implementada: idade e cooldown por tempo lógico, reprodução assexuada
com transferência de energia, IDs únicos, geração básica, características
copiadas sem mutação e contadores de nascimentos/mortes. Filhotes entram ao
final do passo e só agem no seguinte. Comida, metabolismo, bordas e encerramento
preservados; domínio sem Pygame, tempo fixo 1/60 s e RNG próprio. Sem estrutura
genética, mutações, HUD ou controles novos. Evidências ao final.

### Base histórica da Sprint 2

Sprint 2 implementada: Food, 75 alimentos iniciais, busca por visão, exploração,
consumo, gasto energético, remoção de mortos e reposição a 1/s até 125.
Creature, Food e World não conhecem Pygame. Renderer desenha criaturas azuis e
comida verde. Tempo fixo, reflexão e encerramento preservados. Não há reprodução,
herança, HUD, métricas ou controles novos. Evidências da entrega ao final.

### Base histórica da Sprint 1

Instruções compartilhadas em `AGENTS.md`, quatro documentos de projeto,
README, .gitignore, dependências separadas, pacote `evolife` com configuração
e `main.py` com janela 800 × 600. Creature guarda os cinco atributos do PRD e
move-se por dt, refletindo nas bordas com o raio do círculo considerado. World
cria dez criaturas; Renderer desenha círculos azuis claros sobre fundo preto.
A aplicação usa acumulador e passos lógicos de 1/60 s, separados do desenho.
Fechar, Esc e Ctrl+C encerram com liberação em `finally`. Energia permanece 100;
não há comida, metabolismo, reprodução, genes, HUD ou comandos adicionais.

## Ambiente observado

- Plataforma: Linux, shell bash.
- Python global e do `.venv`: 3.14.4.
- `.venv` criado na primeira parte da sessão e preservado após nova instrução.
- pip inicial do `.venv`: 25.1.1.
- Git no início da Sprint 0: branch `main`; registrada em `73d5e04`.
- Sessão da Sprint 2: branch `develop`, HEAD `160687a`; sem novos commits.
- Início da Sprint 1: árvore de trabalho limpa e sete testes existentes
  aprovados (`7 passed in 0.18s`), Python 3.14.4, pygame-ce 2.5.8 e pytest 9.1.1.
- Dependência de execução: `pygame-ce==2.5.8`; módulo `pygame` verificado.
- Dependência de desenvolvimento: `pytest==9.1.1`.
- Dependências transitivas instaladas como wheels: iniconfig 2.3.1,
  packaging 26.3, pluggy 1.6.0 e Pygments 2.21.0.
- SDL fornecido pelo pacote: 2.32.10. Python e ambiente virtual preservados.

## Decisões

- Usar pygame-ce 2.5.8 por instrução do usuário para preservar Python 3.14;
  o módulo de uso continua `pygame`. Detalhes em ADR-001 de `ARCHITECTURE.md`.
- Separar requirements de execução e desenvolvimento; exigir wheels.
- Centralizar configuração da janela; criar componentes somente quando necessários.
- Inicializar somente vídeo nesta sprint, sem áudio; limitar desenho a 60 FPS.
- Memória e regras ficam em Markdown no repositório, comuns aos dois CLIs.
- A Sprint 0 foi registrada pelo usuário; não fazer novos commits.
- Creature e World não importam Pygame. Renderer desenha sem mudar o estado.
- Reflexão espelha o deslocamento excedente e inverte a componente da velocidade,
  mantendo o círculo inteiro dentro do mundo; cantos refletem os dois eixos.
- Posições lógicas permanecem float; arredondamento ocorre somente no desenho.
- Configuração inicial: dez criaturas, velocidades entre 25 e 90 pixels/s,
  energia 100, raio 7, cor (80, 190, 255), seed interna 42.
- O World usa `random.Random` próprio, conforme PRD 6.1. A seed inicial não
  introduz controles ou experimentos da Sprint 6.
- Passos fixos com acumulador preservam o tempo restante entre quadros;
  `math.isclose` evita perder passos por arredondamento na comparação.

## Plano executado da Sprint 1

Implementar RF-02 e RF-03: Creature com x/y/direction/speed/energy, movimento
por dt, dez círculos e reflexão nas bordas. Separar Creature, World e Renderer;
usar tempo fixo de 1/60 s com acumulador na aplicação. Energia não muda ainda.
Testar movimento conhecido, bordas/cantos, população, desenho e cadências de
renderização; preservar encerramento, PRD e dependências. Atualizar os documentos
que ainda indicavam Sprint 0 sem commit ou Sprint 1 não autorizada: são registros
da sessão anterior, superados pela autorização atual e pelo estado do Git.

## Dificuldades históricas da Sprint 0 (resolvidas)

1. Primeira instalação de `pygame pytest` no sandbox falhou na resolução de
   rede: `Failed to establish a new connection: [Errno -2] Name or service not known`.
   Foi solicitada e concedida autorização para repetir aquele comando fora
   do sandbox. Nenhuma biblioteca foi instalada no sistema operacional.
2. A tentativa autorizada selecionou `pygame-2.6.1.tar.gz` no Python 3.14 e
   falhou na preparação da compilação:

   ```text
   /bin/sh: 1: sdl2-config: not found
   RuntimeError: Unable to run "sdl-config". Please make sure a development version of SDL is installed.
   error: subprocess-exited-with-error
   Getting requirements to build wheel did not run successfully.
   exit code: 1
   ```

   Instalação abortada sem pygame instalado. Antes de qualquer instalação de
   Python alternativo ou SDL, o usuário determinou pygame-ce 2.5.8 e wheels.
   Nenhum Python alternativo ou SDL do sistema foi instalado.
3. Cache global de pip não é gravável no sandbox. Os comandos do projeto
   usam `--no-cache-dir`, sem alterar propriedade ou permissões do cache.
4. A tentativa com wheels de pygame-ce no sandbox terminou com saída 1.
   Comando: `.venv/bin/python -m pip install --only-binary=:all: --no-cache-dir --retries 0 -r requirements-dev.txt`.
   Mensagem completa:

   ```text
   ERROR: Could not find a version that satisfies the requirement pygame-ce==2.5.8 (from versions: none)
   ERROR: No matching distribution found for pygame-ce==2.5.8
   ```

   A versão consta no PyPI; o sandbox já apresentou bloqueio de rede nesta
   sessão. Próxima tentativa requer autorização de acesso externo, mantendo
   Python, `.venv` e instalação exclusivamente por wheels.
   **Resolvido:** autorização concedida e repetição bem-sucedida fora do
   sandbox, com o mesmo comando. Todos os downloads foram `.whl`, incluindo
   `pygame_ce-2.5.8-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.whl`.
   Sem compilação ou instalação no sistema operacional.

## Verificações e evidências históricas — Sprint 0

| Verificação | Resultado executado |
| --- | --- |
| Leitura do PRD e estado inicial do Git | Realizada; somente PRD como arquivo não rastreado |
| Criação do .venv | `python3 -m venv .venv`, saída 0 |
| Versão do Python após retomada | `.venv/bin/python --version`: Python 3.14.4 |
| Dependências instaladas na retomada | Somente pip 25.1.1; instalação de pygame anterior não concluiu |
| Hash original do PRD | `740fabf9754d5fa4081a8229607a3ced6bd27c3c333440062a491904a10f4802` |
| Instalação com wheels | Saída 0; pygame-ce 2.5.8 e pytest 9.1.1 instalados no .venv |
| `import pygame` | Aprovado: pygame-ce 2.5.8, SDL 2.32.10, Python 3.14.4 |
| `.venv/bin/python -m pytest -q` | **7 passed in 0.22s**, saída 0, driver SDL dummy |
| `.venv/bin/python -m pip check` | `No broken requirements found.`, saída 0 |
| `.venv/bin/python -m compileall -q main.py evolife tests` | Saída 0, sem erros |
| `sha256sum EvoLife_PRD_Roadmap.md` | Hash idêntico ao original |
| `git diff --check` | Saída 0; arquivos novos ainda não rastreados |
| Janela real no desktop | Autorizada; driver X11, 374 quadros em 6,29 s, saída 0 e display liberado |
| Vídeo da janela | `docs/media/sprint0.mp4`, somente a janela EvoLife, sem áudio |
| `ffprobe` da demonstração | H.264, 800 × 600, 15 FPS, duração 5,000 s, tamanho 4.626 bytes |
| `git check-ignore` | .venv, __pycache__ e .pytest_cache ignorados corretamente |
| Python global ao terminar | `python3 --version`: Python 3.14.4, preservado |
| Links locais de AGENTS, README e docs | Todos os destinos existentes, saída 0 |
| Whitespace dos novos arquivos textuais | `git diff --no-index --check`, sem avisos; PRD excluído dessa checagem |

Os sete casos automatizados verificaram QUIT, Esc, três redesenhos com fundo
preto/tamanho/título e tecla sem ação, limpeza após erros em set_mode/flip,
Ctrl+C e importação sem abrir janela. Driver dummy não comprova aparência
no monitor. Separadamente, a verificação gráfica executou `main()` com driver
X11 e instrumentou o redesenho para conferir tamanho e fundo; um evento QUIT
programado após seis segundos encerrou o aplicativo. O ffmpeg já disponível
gravou apenas a própria janela via seu identificador, sem áudio nem outras
áreas do desktop. A captura e o encerramento tiveram saída 0.

O script de verificação foi temporário (`/tmp/evolife_verify_sprint0.py`),
não é dependência da aplicação nem necessário aos testes do repositório.
Para repetir a verificação visual, use `python main.py`; para a automação
permanente, use `python -m pytest -q`. Não houve inspeção visual manual por
uma pessoa nem teste em Windows. Não há falhas de instalação pendentes.

A checagem auxiliar de whitespace inicialmente interpretou o código 1 de
`git diff --no-index` (diferença de arquivo novo) como falha. O verificador foi
corrigido para distinguir diferenças de avisos; a repetição passou sem
alterar os arquivos ou o PRD.

## Arquivos entregues — Sprint 0

- `AGENTS.md`, `README.md` e `.gitignore`.
- `requirements.txt`, `requirements-dev.txt` e `pytest.ini`.
- `main.py`, `evolife/__init__.py` e `evolife/config.py`.
- `tests/conftest.py` e `tests/test_application.py`.
- `docs/ARCHITECTURE.md`, `docs/SPRINTS.md`, `docs/TASKS.md` e esta memória.
- `docs/media/sprint0.mp4`; `.venv` local criado e preservado, ignorado pelo Git.

Os arquivos preexistentes, incluindo PRD e diretórios .git/.agents/.codex/.aws,
foram preservados. Na entrega inicial, os arquivos ainda não estavam rastreados
e o agente não executou git add, commit, tag ou push. Posteriormente, o usuário
registrou a Sprint 0 em `73d5e04`. As mudanças da Sprint 1 não foram commitadas.

## Entrega da Sprint 1

Requisitos implementados: RF-02 (dez criaturas com movimento autônomo) e RF-03
(bordas). RF-01 da Sprint 0 foi preservado. Os registros que proibiam Sprint 1
foram atualizados de acordo com a autorização do usuário, sem alterar o PRD.

| Arquivos criados/alterados | Finalidade |
| --- | --- |
| `evolife/creature.py` (novo) | Estado e movimento com reflexão |
| `evolife/world.py` (novo) | Inicialização e atualização da população |
| `evolife/renderer.py` (novo) | Círculos e fundo; desenho independente |
| `evolife/config.py`, `main.py` | Parâmetros e integração com tempo fixo |
| `tests/test_movement.py` (novo) | 17 casos de movimento, bordas, cantos e dt |
| `tests/test_world.py` (novo) | 4 casos de população, bordas por 60 s e domínio sem Pygame |
| `tests/test_renderer.py` (novo) | 2 casos de desenho, limpeza e estado preservado |
| `tests/test_timing.py` (novo) | 3 cadências de quadros com 60 passos por segundo lógico |
| `docs/media/sprint1.gif` (novo) | Demonstração gráfica de 15 segundos prevista no PRD |
| `AGENTS.md`, `README.md`, documentos em `docs/` | Autorização, execução, arquitetura, quadro e continuidade |

Os sete casos originais de `tests/test_application.py` não foram alterados.
Requirements, Python e `.venv` foram mantidos; não houve instalação adicional.

## Testes executados — Sprint 1

| Comando / verificação | Resultado |
| --- | --- |
| `.venv/bin/python -m pytest -q` antes da implementação | 7 passed in 0.18s |
| `.venv/bin/python -m pytest -q tests/test_movement.py` | 17 passed in 0.06s |
| `.venv/bin/python -m pytest -q` após integração | **33 passed in 0.51s**, saída 0 |
| `.venv/bin/python -m pytest -q` na validação final | **33 passed in 0.49s**, saída 0 |
| `.venv/bin/python -m pip --no-cache-dir check` | No broken requirements found., saída 0 |
| `.venv/bin/python -m compileall -q main.py evolife tests` | Saída 0 |
| `git diff --check` | Sem avisos, saída 0 |
| `sha256sum EvoLife_PRD_Roadmap.md` | Mesmo hash original: 740fabf9754d5fa4081a8229607a3ced6bd27c3c333440062a491904a10f4802 |
| Verificação gráfica X11 | Saída 0, 995 quadros, 961 passos fixos (16,02 s lógicos), dez criaturas se moveram e ficaram nas bordas |
| Encerramento da aplicação gráfica | Evento QUIT programado após 16 s; código 0 e display liberado |
| GIF via ffprobe | docs/media/sprint1.gif: 800 × 600, 225 quadros, 15,000 s, 1.111.183 bytes |
| GIF via ffmpeg framemd5 | 225 quadros com 225 conteúdos distintos; movimento registrado |
| Captura visual inspecionada pelo agente | Dez círculos azuis claros sobre fundo preto, dentro da área |
| Links locais e whitespace | Documentos e arquivos novos verificados, sem problemas |
| Estado final do Git | HEAD continua 73d5e04; oito arquivos alterados e oito novos, sem commits nesta sessão |

Teste do PRD: (100,100), direção zero e velocidade 40 com dt=0,5 resulta em
(120,100). As quatro bordas e os cantos foram verificados considerando raio,
contato exato e excesso de deslocamento. O teste de população rodou 3.600
passos (60 s lógicos), conferindo limites de todas as criaturas em cada passo.
Cadências simuladas de 100, 10 e 1 FPS produziram os mesmos 60 passos de 1/60 s
em um segundo, com posição final (140,100). Importar domínio em um processo
novo não carregou Pygame; desenhar não mudou atributos das criaturas.

A verificação gráfica usou script temporário `/tmp/evolife_verify_sprint1.py`
para instrumentar o main existente, conferindo população, cor, limites e
movimento, sem alterar o código da aplicação. A gravação capturou somente a
janela EvoLife via seu identificador X11. O ffmpeg preexistente foi usado
para criar o GIF; não é dependência para executar o jogo ou os testes.
A execução do verificador durou 21,09 s incluindo conversão da mídia; o jogo
avançou 16,02 s lógicos e o GIF contém 15 s. Os arquivos temporários não são
parte da entrega e não precisam existir para executar ou testar o projeto.

## Problemas conhecidos e limites — Sprint 1

Nenhuma falha funcional encontrada nos testes executados. A validação visual
manual pelo usuário e a plataforma Windows não foram realizadas. O desenho
não interpola entre passos lógicos. Se a aplicação ficar suspensa por muito
tempo, recupera o tempo acumulado antes de desenhar novamente; não há descarte
de tempo ou limite de recuperação nesta sprint. Não houve benchmark com 100
criaturas nem teste de estabilidade de 15 minutos; essas medições não são
critérios da Sprint 1. A memória distingue segundos lógicos de duração real.

## Próxima ação

Aguardar revisão do usuário da Sprint 3 antes de qualquer commit ou integração.
Para avaliar, usar
`source .venv/bin/activate`, `python main.py` e `python -m pytest -q`.
Não iniciar Sprint 4, commits, pushes ou merges sem autorização explícita.


## Abertura da Sprint 2 — 12/10/2026

- Usuário confirmou Sprint 0 concluída, Sprint 1 aprovada e integrada à main
  pelo PR #1, Sprint 2 autorizada e Sprint 3 bloqueada.
- Branch verificada: develop; árvore limpa antes das alterações. HEAD 160687a,
  referência local origin/develop no mesmo commit.
- Referências locais main e origin/main ainda em 73d5e04. Não houve fetch nem
  alteração da main; integração registrada pela confirmação do usuário.
- Base executada: `.venv/bin/python -m pytest -q`, **33 passed in 0.51s**,
  saída 0, SDL dummy. Nenhuma instalação adicional.
- Registros anteriores de entrega sem commit e autorização limitada à Sprint 1
  são históricos, sucedidos pela confirmação acima.
- S2-01 concluída: instruções, memória, sprints e tarefas atualizadas.
- Plano: comida e busca, consumo/metabolismo, morte/reposição, testes e
  demonstração. Configuração centralizada e domínio sem Pygame preservados.

## Implementação da Sprint 2 — tarefas S2-02 a S2-05

- Food criado sem Pygame; 75 pontos verdes, raio 3, posições dentro do mundo.
- Busca do alvo mais próximo até o limite inclusivo da visão. Empates usam
  a ordem dos alimentos. Sem alvo, intervalo sorteado de 1 a 3 s para virar,
  usando o gerador próprio. O intervalo avança somente ao vagar.
- Visão inicial 100 e eficiência 1,0 são valores fixos dentro dos intervalos
  do PRD. Ainda não são genes herdáveis. Velocidades originais preservadas.
- Consumo em contato antes e depois do movimento; ganho 45 e teto 130.
  Gasto aplicado em seguida pela fórmula original; energia mínima 0.
- Mortos no início do passo não se movem nem comem. A lista de sobreviventes
  substitui a população após a iteração, sem remoções durante o percurso.
  Disputas por alimento são resolvidas na ordem da população, uma vez por unidade.
- Reposição acumula frações a 1 unidade/s até 125; não acumula crédito com
  mundo cheio e continua após extinção. Atualização zero não muda o estado;
  dt negativo/não finito é rejeitado também com população zerada.
- Primeira integração: `.venv/bin/python -m pytest -q`, **69 passed in 1.56s**,
  saída 0, SDL dummy. Novos casos cobrem busca, consumo, competição, fórmula,
  teto, mortes simultâneas, extinção, reposição e repetição interna por seed.
- Revisão refinou a tolerância absoluta da reposição para evitar arredondar
  segundos incompletos; teste de fronteira e teste do main após extinção adicionados.
- S2-02 a S2-05 concluídas. S2-06 em andamento: validação final e demonstração.

## Entrega da Sprint 2 — tarefas S2-06 e S2-07

RF-04, RF-05 e RF-06 implementados. Arquivos novos: `evolife/food.py`,
`tests/test_food.py`, `tests/test_energy.py` e `docs/media/sprint2.gif`.
Config, Creature, World e Renderer estendidos; testes de mundo, desenho e
cadências atualizados para as regras novas. `main.py`, os 17 testes de movimento
e os sete de ciclo de vida da aplicação foram preservados integralmente.
AGENTS, memória, tarefas, sprints, README e arquitetura refletem a entrega.

| Verificação executada | Resultado |
| --- | --- |
| `.venv/bin/python -m pytest -q` final | **71 passed in 1.54s**, saída 0, SDL dummy |
| `.venv/bin/python -m pip --no-cache-dir check` | No broken requirements found., saída 0 |
| `.venv/bin/python -m compileall -q main.py evolife tests` | Saída 0 |
| `git diff --check` durante a validação | Saída 0, sem avisos |
| Python global e do .venv | Ambos 3.14.4, preservados |
| `sha256sum EvoLife_PRD_Roadmap.md` | 740fabf9754d5fa4081a8229607a3ced6bd27c3c333440062a491904a10f4802, original preservado |
| Demonstração de alimentação | 360 passos de 1/60 s; alimento consumido em 2 s; energia 27,36217 → 72,34000 após consumo e gasto do passo |
| GIF via ffprobe | 800 × 600, 90 quadros, 6,000 s, 158.273 bytes |
| Frame da demonstração inspecionado pelo agente | Criatura azul, alimento verde e legenda com energia recuperada |

A suíte contém 38 casos adicionais à base de 33: energia, busca, exploração,
visão/contato inclusivos, alimento inicial, competição, reposição fracionada,
limite sem crédito acumulado, remoção simultânea de mortos e extinção.
O teste do main após extinção desenha dez quadros com 600 passos lógicos,
repõe dez unidades e encerra pelo evento QUIT com o display liberado.
As cadências de 100, 10 e 1 FPS produzem posição e energia iguais, 60 passos
e uma reposição por segundo. O domínio continua importando sem Pygame.

Demonstração: cenário preparado com uma criatura em (300,300), velocidade 40,
energia 30, visão 100, eficiência 1, intervalo de exploração 3 e alimento
em (390,300), seed 42. O World e o Renderer reais avançaram 360 passos;
90 superfícies foram convertidas em GIF a 15 FPS pelo ffmpeg preexistente.
Renderização fora da tela, ambiente SDL dummy, sem janela no desktop.
Legendas de energia/tempo foram adicionadas apenas à demonstração, sem HUD
na aplicação. Ao final, energia 67,02. Arquivos intermediários foram temporários;
ffmpeg continua sendo ferramenta de mídia, sem nova dependência do jogo.

Revisão de código executada nesta sessão: separação domínio/desenho, fórmula
original, ordem de alimentação e gasto, desempate e consumo único, aplicação
segura de mortes, limite/fração de reposição e validação de dt após extinção.
A revisão refinou a tolerância da reposição; os dois casos adicionais de
fronteira e ciclo da aplicação passaram na suíte final.

Limites no momento da entrega técnica: não houve teste da Sprint 2 com driver gráfico X11, avaliação manual
pelo usuário ou Windows. GIF fora da tela e testes dummy não comprovam fluidez
no monitor. Não houve calibração da fórmula nem benchmark de 100 criaturas ou
estabilidade de 15 minutos (Sprint 7). Regras de sobrevivência usam passos fixos;
nenhuma garantia de equivalência de decisões para dt arbitrariamente grande.
Sem reprodução: a população pode chegar a zero e não se renova nesta sprint.
Não houve dificuldade de ambiente nem instalação adicional.

S2-06 e S2-07 concluídas. Na entrega original, a Sprint 2 aguardava revisão;
posteriormente foi aprovada e integrada pelo PR #3 (ver abertura da Sprint 3).
Não foram executados commits, tags, pushes, merges, fetch ou publicação.
A main local foi preservada. Nenhum trabalho da Sprint 3 foi iniciado.

Conferência de encerramento: branch develop, HEAD 160687a e main local 73d5e04
inalterados; 13 arquivos rastreados modificados e quatro arquivos novos,
todos referentes à entrega. `git diff --check` final passou; whitespace dos
três arquivos Python novos e destinos dos links locais também passaram.

## Validação pelo usuário — Sprint 2, Ubuntu — 12/10/2026

O usuário informou ter executado manualmente a aplicação e a suíte de testes
da Sprint 2 no Ubuntu, sem identificar erros em nenhuma das duas execuções.
Esta é uma evidência relatada pelo usuário, distinta dos testes automatizados
com SDL dummy e da demonstração fora da tela executados pelo agente.

Os resultados anteriores foram preservados, incluindo os 71 testes aprovados
na validação do agente. A suíte não foi executada novamente pelo agente nesta
atualização documental. A pendência de avaliação manual da aplicação no Ubuntu
fica atendida pelo relato acima, sem alterar o estado de aprovação ou integração
da Sprint 2 naquele registro. A Sprint 3 ainda não estava autorizada
naquele momento; a autorização posterior consta na abertura abaixo.

Somente esta memória foi atualizada nesta tarefa; nenhum código foi modificado
e nenhum commit foi realizado. As alterações preexistentes foram preservadas.


## Abertura da Sprint 3 — 12/10/2026

- Sprint 2 concluída, revisada, aprovada e integrada pelo PR #3. Sprint 3
  autorizada nesta sessão; Sprint 4 não autorizada. Preservado o histórico.
- Git inicialmente limpo. develop, origin/develop e origin/main apontam para
  3b75b6e; `git rev-list --left-right --count origin/main...develop`: 0 / 0.
- main local continua em 73d5e04, sete commits atrás, sem alterações. A develop
  contém a versão estável aprovada indicada pelo usuário; não houve fetch,
  checkout, merge ou atualização da main local.
- Base executada: `.venv/bin/python -m pytest -q`, **71 passed in 1.57s**,
  saída 0, SDL dummy. Python e .venv preservados; sem instalação.
- S3-01 concluída. Plano: idade/cooldown e identidade básica; nascimento após
  sobrevivência com transferência 45; coleção de filhotes aplicada ao final;
  totais de eventos; testes de regras e determinismo; demonstração e revisão.
- Sem estrutura genética nova, mutações, HUD ou funcionalidades da Sprint 4.

## Implementação da Sprint 3 — S3-02 a S3-04

- Creature recebeu age_seconds, reproduction_cooldown, id e generation, sem
  estrutura genética. World distribui IDs inteiros crescentes a partir de 0,
  não reutilizados após morte; criaturas isoladas podem ter id None, atribuído
  pelo mundo ao processar cenários preparados.
- Idade e cooldown avançam pelo dt validado. Após alimentação e metabolismo,
  cada sobrevivente com idade ≥10, energia ≥110 e cooldown encerrado pode
  gerar exatamente um filhote naquele passo. Transferência 45, espera 10 s.
- Características copiadas: speed, vision, efficiency. Filhote inicia com
  idade e cooldown zero, energia 45 e geração do progenitor +1, sem mutação.
- Posição sorteada a 16 pixels do progenitor (2 raios +2), com coordenadas
  limitadas pelo raio nas bordas. Direção e intervalo inicial de exploração
  usam o RNG próprio. IDs e contadores não consomem aleatoriedade.
- Lista de recém-nascidos separada: entram ao final e só agem no próximo passo.
  Sobreviventes e filhotes substituem a coleção após a iteração. Totais
  births_total e deaths_total no World; população inicial não conta como nascimento.
- Mortos anteriores e os que esgotam energia são contados uma vez e removidos;
  não reproduzem. Contadores persistem após extinção. Não há HUD ou métricas novas.
- Primeira regressão encontrou a expectativa antiga de população fixa no teste
  de 60 s (70 passaram, 1 falhou). Teste atualizado para população dinâmica,
  balanço de eventos e IDs únicos, preservando verificações de movimento/bordas.
- Integração seguinte: `.venv/bin/python -m pytest -q`, **99 passed in 3.50s**,
  saída 0, SDL dummy. Casos incluem bloqueios, conservação descontando metabolismo,
  espera completa, IDs não reutilizados, bordas/cantos, gerações e determinismo.
- S3-02 a S3-04 concluídas; S3-05 em andamento. Adicionados também casos de
  nascimento em cadências diferentes e desenho sem alterar ciclo/contadores.

## Entrega da Sprint 3 — S3-05 a S3-07

RF-07 implementado, com identidade e geração básicas necessárias aos nascimentos,
conforme autorização explícita do usuário. Sem estrutura Genetics ou mutações.
Config, Creature e World alterados; Renderer e main.py preservados. Testes de
mundo, cadência e desenho estendidos; `tests/test_reproduction.py` e
`docs/media/sprint3.gif` novos. AGENTS, README, arquitetura, sprints, tarefas e
esta memória atualizados. Sprints 0–2 e suas mídias preservadas.

| Comando / verificação executada | Resultado |
| --- | --- |
| `.venv/bin/python -m pytest -q` após implementação final | **103 passed in 3.61s**, saída 0, SDL dummy |
| `.venv/bin/python -m pip --no-cache-dir check` | No broken requirements found., saída 0 |
| `.venv/bin/python -m compileall -q main.py evolife tests` | Saída 0 |
| Python global / .venv | Ambos 3.14.4, preservados |
| `sha256sum EvoLife_PRD_Roadmap.md` | 740fabf9754d5fa4081a8229607a3ced6bd27c3c333440062a491904a10f4802, original |
| Execução da demonstração | 3.600 passos, 60 s simulados; 28 nascimentos, 5 mortes; população máxima 34, final 33 |
| Primeiro nascimento | 10 s lógicos, ID 10, geração 1 e energia inicial 45 |
| Geração máxima ao final da demonstração | 3, características copiadas sem mutação |
| GIF final via ffprobe | 800 × 600, 225 quadros, 15,000 s, 734.228 bytes |
| Frame inspecionado pelo agente | 10,4 s lógicos: 20 criaturas, dez nascimentos, círculos novos destacados |

A suíte final acrescenta 32 casos à base de 71: 28 em reprodução, três novas
cadências com nascimento e um desenho de recém-nascido. Verifica requisitos
inclusivos e bloqueios, transferência 45, conservação descontando metabolismo,
idade por 600 passos, cooldown completo, ausência de reprodução recursiva,
características copiadas e geração, bordas/cantos e mundo pequeno, IDs iniciais
e não reutilizados, eventos simultâneos e morte contada uma vez, extinção,
dt zero e determinismo com births/deaths/IDs. Os testes anteriores de importação,
movimento, sobrevivência e ciclo de aplicação continuam aprovados.

Demonstração: `World(seed=42)` padrão, área 800 ×600, dez criaturas, energia
inicial 100, idade/cooldown zero, geração zero, visão 100, eficiência 1,
velocidades sorteadas de 25 a 90, 75 alimentos, reposição 1/s até 125.
Reprodução oficial: idade ≥10, energia ≥110 após metabolismo, cooldown zero;
transferência 45 e espera 10 s. Distância inicial do filhote 16 pixels,
com ajuste de posição nas bordas. Nenhum parâmetro oficial foi alterado.
World e Renderer reais geraram 225 superfícies, amostradas a cada 16 passos;
ffmpeg preexistente codificou a 15 FPS. Assim o GIF mostra 60 s lógicos em 15 s,
a 4x, sem implementar controle de velocidade na aplicação. Legendas e anéis
amarelos destacam nascimento recente apenas na mídia, sem HUD novo.
Renderização fora da tela; SDL dummy, sem janela de desktop. Intermediários
em diretório temporário; nenhuma dependência instalada. Houve oscilação real:
por exemplo, aos 56,7333 s a população caiu de 33 para 32, e aos 59,3333 s
um nascimento elevou-a novamente a 33.

Revisão estática realizada: elegibilidade após metabolismo, ordem do ciclo,
transferência sem criação de energia, cooldown, IDs monotônicos, geração,
clamp nas bordas, RNG próprio e cópia dos atributos; nenhuma alteração da
coleção percorrida, recém-nascidos diferidos e contagem única de mortos.
Diff de código e testes revisado; compileall aprovado. Nenhuma falha funcional
pendente. A única falha intermediária foi a expectativa antiga de população
fixa, já corrigida e registrada acima.

Limitações no momento da entrega técnica: sem validação manual da Sprint 3
pelo usuário, execução gráfica
X11 nesta sprint, teste Windows, benchmark ou estabilidade de 15 minutos.
A simulação mantém contrato de passo fixo; dt grande não reproduz a mesma
sequência de decisões. Não há limite de população novo nem morte por velhice.
Nas bordas um filhote pode sobrepor o progenitor; não há colisão entre criaturas.
ID/generation são a estrutura mínima, sem parent_id ou organização genética.
Nenhuma dificuldade de instalação/ambiente; Python global, .venv e dependências
preservados. Não houve agentes auxiliares.

S3-05, S3-06 e S3-07 concluídas. Desenvolvimento da Sprint 3 interrompido para
revisão antes de qualquer commit ou integração. Sprint 4 não autorizada.
Sem commits, pushes, tags, merges, publicação ou alterações da main.

Conferência final: develop e origin/main permanecem em 3b75b6e, main local em
73d5e04; 12 arquivos rastreados modificados e dois novos nesta entrega.
`git diff --check` passou sem avisos; whitespace do novo teste e destinos dos
links locais passaram. PRD e todas as mídias anteriores foram preservados.

## Validação pelo usuário — Sprint 3, Ubuntu — 12/10/2026

O usuário informou ter executado manualmente o EvoLife da Sprint 3 no Ubuntu
e não ter identificado erros na aplicação. Esta evidência é um relato do
usuário, distinto dos testes automatizados com SDL dummy e da demonstração
renderizada fora da tela pelo agente. A pendência de avaliação manual no Ubuntu
fica atendida pelo relato, sem alterar o estado de aprovação ou integração.

Preservados os resultados anteriores, incluindo **103 passed in 3.61s** na
suíte automatizada executada pelo agente. O relato atual refere-se à aplicação;
não registra nova execução da suíte de testes. Não houve reexecução dos testes
pelo agente nesta atualização documental.

S3-08 concluída pelo usuário; relato registrado na memória, no quadro de tarefas,
no plano de sprints e no README. Somente esses documentos foram alterados nesta
tarefa, preservando código e mudanças preexistentes. Sem commits ou push.
Desenvolvimento continua interrompido para revisão; Sprint 4 não autorizada.

## Abertura da Sprint 4 — 12/10/2026

- Autorização explícita do usuário; Sprint 3 revisada, aprovada e integrada
  pelo PR #4, merge 96ab068. Sprint 5 não autorizada.
- Na primeira tentativa, main local estava em 73d5e04, nove commits atrás;
  trabalho interrompido sem editar arquivos. Usuário resolveu por fast-forward.
- Retomada: branch develop, árvore limpa, main/develop/origin/main/origin/develop
  iguais a 96ab068; comparação main...develop: 0 / 0. Sem fetch ou alteração
  de referências pelo agente.
- Base: `.venv/bin/python -m pytest -q`: **103 passed in 3.88s**, saída 0.
- PRD, código, documentos e testes consultados. Sem instalação ou agentes
  auxiliares. Plano: genes imutáveis e propriedades compatíveis em Creature;
  parâmetros validados no World, herança pelo seu RNG e parent_id; testes
  controlados sem estimar probabilidades; demonstração e revisão final.

## Entrega da Sprint 4 — S4-02 a S4-06

### Implementação e decisões

- RF-08: `evolife/genetics.py` contém Genes e MutationSettings, dataclasses
  imutáveis. Apenas speed, vision, efficiency; igualdade por valor. Genes
  rejeita booleanos, não numéricos, não finitos e valores fora das faixas.
- Limites inclusivos em config: speed 25–90, vision 35–160, efficiency 0,8–1,2.
  Defaults de mutação: probabilidade 0,12 e fração de desvio 0,08. Desvios
  efetivos 5,2 / 10 / 0,032; normal centrada em zero, sem direção planejada.
- Genes.inherit recebe o RNG do World. Ordem fixa speed/vision/efficiency,
  um sorteio independente por gene em cada nascimento; gauss apenas quando
  random() < probability; limitar o resultado à faixa. Mudanças podem ser
  positivas, negativas ou nulas (inclusive pelo clamp). Progenitor preservado.
- World aceita mutation_probability e mutation_stddev_fraction nomeados;
  valida probabilidade finita 0–1 e desvio finito não negativo. Sem RNG global.
  Mesmo com probabilidade zero são consumidos três sorteios, sem gauss.
  Mesma seed/configuração/passos repete esta versão; trajetórias históricas
  da Sprint 3 diferem porque agora há sorteios adicionais.
- Creature armazena somente `_genes`, exposto por genes. A assinatura anterior
  é preservada, inclusive argumentos posicionais; alternativamente aceita
  genes=Genes(...). Misturar genes e os três atributos é rejeitado. Propriedades
  speed/vision/efficiency substituem a estrutura por cópia validada ao escrever,
  sem alterar outras criaturas. Construtor explícito evita duplicar atributos.
- Filhotes recebem novo ID, parent_id e geração +1. Valores iniciais parent_id
  None; IDs crescentes não reutilizados. Relação permanece mesmo após morte
  do progenitor, sem guardar mortos na aplicação. Demo arquiva snapshots locais.
- Idade mínima 10, energia mínima 110 após metabolismo, cooldown 10,
  transferência 45, filhote energia 45, posição limitada e ações no passo
  seguinte foram preservados. Fórmula `(0.55 + 0.012 * speed + 0.003 * vision)
  * efficiency` inalterada. Não há seleção artificial.
- main.py, Renderer, Food, requirements e mídias anteriores preservados.
  Domínio continua independente de Pygame; aplicação continua em 1/60 s.

### Testes, revisão e verificações executadas

| Comando / verificação | Resultado |
| --- | --- |
| Suíte base `.venv/bin/python -m pytest -q` | 103 passed in 3.88s, saída 0 |
| Primeira integração com genética | 191 passed in 6.96s, saída 0 |
| Suíte final `.venv/bin/python -m pytest -q` | **192 passed in 6.85s**, saída 0; SDL dummy |
| `.venv/bin/python -m compileall -q main.py evolife tests scripts` | Saída 0, sem erros |
| `.venv/bin/python -m pip --no-cache-dir check` | No broken requirements found., saída 0 |
| Python global e .venv | Ambos Python 3.14.4, preservados |
| `sha256sum EvoLife_PRD_Roadmap.md` | 740fabf9754d5fa4081a8229607a3ced6bd27c3c333440062a491904a10f4802, idêntico |
| `git diff --check` | Saída 0, sem avisos |
| Auditoria AST, whitespace de textos novos e links locais | Aprovada, saída 0 |
| Relatório com e sem mídia | Texto reproduzido identicamente, saída 0 |
| ffprobe do GIF final | GIF 800 ×600, 225 quadros, 15,000 s, 1.036.758 bytes |
| Git | develop e main continuam em 96ab068; 13 arquivos modificados e cinco novos |

Os 103 casos anteriores foram preservados; 89 casos novos em test_genetics.
Cobertura nova: cópia sem mutação, oito combinações de decisões individuais,
limiar configurável, sigmas por amplitude, sinais positivo/negativo/zero,
limites inclusivos e mutações próximas/dentro das bordas, validação de valores
inválidos, propriedades compatíveis, isolamento do progenitor, parent_id,
geração, conservação de energia, atualização diferida, efeitos no movimento,
percepção/metabolismo, duas gerações descendentes, determinismo e extinção.
Não há testes que dependam de estimar frequência por amostragem aleatória.

Adaptações necessárias na regressão: cenários de cópia/metabolismo de filhotes
em test_reproduction e cadências em test_timing desativam mutação explicitamente.
O teste de contato em test_food antes usava vision=0, inválido no PRD;
agora usa 35 e isola steer para continuar verificando colisão, movimento e
energia. O teste de importação sem Pygame inclui genetics. Nenhum caso removido.
Sem falhas funcionais nas execuções da Sprint 4.

Revisão estática do código e diff realizada sem agentes auxiliares: fonte
única dos genes, limites e rejeição antes de substituir estado, imutabilidade,
sorteios por gene sem favorecimento, uso do RNG próprio, ordem do ciclo,
transferência, cooldown, identidade/linhagem, coleção percorrida preservada,
filhotes diferidos e ausência de Pygame no domínio. Revisão dos arquivos novos,
parse AST e compileall complementam a leitura; não foi instalado linter.

### Demonstração e limites

Relatório completo em `docs/GENETICS_DEMO.md`, com os 26 nascimentos:
ID progenitor/filhote, tempo, geração, genes dos dois e mudanças efetivas.
Script permanente `scripts/demonstrate_genetics.py`; executar na raiz:
`.venv/bin/python -m scripts.demonstrate_genetics`. Esta forma não importa
Pygame nem exige ffmpeg. Para mídia opcional, adicionar
`--gif docs/media/sprint4.gif`; ffmpeg preexistente, sem nova dependência.

Cenário: World(seed=42), parâmetros oficiais padrão, área 800 ×600,
população inicial dez, geração zero, energia 100, idade/cooldown zero,
speed sorteado 25–90, vision 100, efficiency 1. Comida inicial 75,
reposição 1/s até 125. 3600 passos de 1/60 s, total 60 s lógicos;
probabilidade 12% por gene e desvio 8% da amplitude. Sem edição de energia,
idade, cooldown ou alimentos, e sem alterar regras oficiais para reproduzir.

Resultado: 26 nascimentos, seis mortes, máximo 34 criaturas e final 30;
geração máxima três. Linhagem 8 → 18 → 25 → 35 (gerações 0 → 1 → 2 → 3):

| Relação | Genes do progenitor (speed, vision, efficiency) | Genes do filhote | Mudanças |
| --- | --- | --- | --- |
| 8 → 18, geração 1 | (60,882641; 100; 1) | (62,677782; 100; 1) | speed |
| 18 → 25, geração 2 | (62,677782; 100; 1) | (62,677782; 100; 1) | nenhuma |
| 25 → 35, geração 3 | (62,677782; 100; 1) | (62,677782; 100; 1,022780) | efficiency |

O GIF tem 225 quadros a 15 FPS e mostra 60 s lógicos em 15 s de mídia,
a 4x. Renderização fora da tela, legendas e anéis exclusivos da demonstração;
um quadro foi inspecionado pelo agente para legibilidade. Não houve janela
real/X11, inspeção manual pelo usuário ou validação Windows da Sprint 4.

A execução não apresentou mudança em vision; testes controlados verificam
sua mutação e efeito na percepção. A demonstração prova herança e variação,
não adaptação: sem comparação entre ambientes/seeds, médias ou inferência
causal de seleção. Ausência de limite populacional e sobreposição de filhotes
nas bordas permanecem como antes. Estabilidade de 15 minutos e métricas são
trabalho de sprints posteriores; Sprint 5 não autorizada. Sem bloqueios de
ambiente, instalação ou permissões; nenhuma dependência instalada.

### Arquivos e próxima ação

Criados: evolife/genetics.py, tests/test_genetics.py,
scripts/demonstrate_genetics.py, docs/GENETICS_DEMO.md, docs/media/sprint4.gif.
Modificados: evolife/config.py, evolife/creature.py, evolife/world.py,
tests/test_food.py, tests/test_reproduction.py, tests/test_timing.py,
tests/test_world.py, AGENTS.md, README.md, docs/ARCHITECTURE.md,
docs/SPRINTS.md, docs/TASKS.md e esta memória.

S4-01 a S4-06 concluídas; critérios técnicos do MVP Evolutivo 0.1 atendidos,
aguardando revisão técnica e aprovação do usuário. Desenvolvimento interrompido.
Próxima ação: usuário revisar código, testes, relatório e GIF; executar
`python main.py` no desktop para avaliação manual, se desejar. Nenhum commit,
push, PR, tag, merge, publicação ou alteração da main feito pelo agente.
Não retomar desenvolvimento nem iniciar Sprint 5 sem nova instrução autorizada.

## Validação posterior da Sprint 4 — revisão externa e usuário no Ubuntu — 12/10/2026

O usuário informou que, após o push para develop, a Sprint 4 foi revisada
tecnicamente e a revisão estática externa não identificou problemas bloqueantes.
Também relatou ter executado a aplicação e a suíte de testes no Ubuntu sem
identificar erros. Esta seção complementa a entrega técnica anterior, cujas
pendências e restrições representam aquele momento e foram preservadas.

As evidências são distintas:

- **Codex, entrega técnica anterior:** 192 passed in 6.85s, saída 0, SDL dummy;
  103 casos anteriores e 89 novos. Resultado e comandos históricos preservados.
- **Usuário, execução no Ubuntu:** aplicação e suíte executadas sem erros
  identificados, conforme relato. Sem novo total, duração, comando exato ou
  saída detalhada informados; não se atribui o total 192 a esta execução.
- **Revisão estática externa após o push:** sem problemas bloqueantes,
  conforme informação do usuário; não foi fornecido relatório detalhado.

A pendência de validação manual no Ubuntu fica atendida pelo relato.
Validação Windows permanece pendente. Não houve nova execução da aplicação
ou da suíte pelo Codex nesta sessão exclusivamente documental.

Commit e push foram realizados pelo usuário, sem ação Git de escrita pelo
agente. Conferência local: branch develop, árvore inicialmente limpa,
develop e origin/develop em `f90c98fd21fd5e0990ee1f8db17b6ce33f2e3eba`
(`feat: adicionar heranca genetica e mutacoes`); main e origin/main em
`96ab068fd608a2cbfe6cc60f512b27972fefa9d8`. Integração da Sprint 4 à main
não informada. Sem fetch, checkout ou alteração de referências nesta sessão.

S4-07 a S4-10 registradas: commit/push do usuário, revisão externa, validação
Ubuntu e atualização documental. Alterados somente AGENTS.md, README.md,
docs/PROJECT_STATE.md, docs/TASKS.md, docs/SPRINTS.md e docs/GENETICS_DEMO.md.
O relatório da demonstração mantém os resultados originais e recebe somente
nota posterior; o script reproduz o texto original, sem essa nota documental.
Código, testes, script, mídias e PRD preservados. Nenhum commit ou push pelo
agente; Sprint 5 não iniciada e não autorizada. Desenvolvimento interrompido;
aguardar novas instruções, sem presumir autorização de integração à main.

Verificações documentais executadas nesta sessão: `git diff --check`, saída 0;
conferência de whitespace e links locais, aprovada; comparação do histórico
da memória com HEAD confirmou preservação integral a partir da base histórica
da Sprint 3. `git status --short` mostra somente os seis documentos acima
modificados, sem arquivos novos. Código, testes, PRD e mídias sem diferenças.
