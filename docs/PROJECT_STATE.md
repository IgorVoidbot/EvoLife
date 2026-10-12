# Memória compartilhada — EvoLife

Última atualização: 12/10/2026, entrega da Sprint 1 para revisão.

## Protocolo de continuidade

Este documento é a memória comum de Codex CLI, OpenCode CLI e agentes futuros.
Leia-o no início de cada sessão junto com `AGENTS.md` e `TASKS.md`. Atualize
ao terminar tarefas e antes de encerrar; preserve decisões e dificuldades
relevantes. Resultados abaixo representam evidências executadas, não intenções.

## Estado e autorização

- Sprint atual: **1**, **entrega técnica concluída e aguardando revisão do usuário**.
  Desenvolvimento interrompido ao concluir esta entrega.
- Sprint 0 concluída e registrada pelo usuário em `73d5e04`.
- Sprint 2: **não iniciada e não autorizada**. Encerrar ao concluir a Sprint 1
  e aguardar revisão. Novos commits não autorizados.
- PRD original: lido e preservado; não editar.
- Commits, tags, pushes e publicação: não autorizados.
- Preservar Python global 3.14 e `.venv`; não usar sudo, instalar SDL ou
  bibliotecas no sistema operacional, nem alterar permissões automaticamente.
- Se uma instalação falhar, informar erro completo antes de outras alterações
  no ambiente. Instalar exclusivamente pacotes pré-compilados.

## Implementação atual

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
- Git existente, branch `main`; Sprint 0 registrada em `73d5e04`.
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

Aguardar revisão do usuário. Para verificar: `source .venv/bin/activate`,
`python main.py` e `python -m pytest -q`. Ajustes da Sprint 1 devem responder
à revisão; nenhuma tarefa da Sprint 2 ou novo commit está autorizada.
Não iniciar comida, energia ou busca automaticamente na próxima sessão.
