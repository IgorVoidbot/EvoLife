# Memória compartilhada — EvoLife

## Protocolo de continuidade

Este documento é a memória comum de Codex CLI, OpenCode CLI e agentes futuros.
Leia-o no início de cada sessão junto com `AGENTS.md` e `TASKS.md`. Atualize
ao terminar tarefas e antes de encerrar; preserve decisões e dificuldades
relevantes. Resultados abaixo representam evidências executadas, não intenções.

## Estado e autorização

- Sprint atual: **0**, fundação; **entrega técnica concluída**, incluindo
  dependências, testes sem tela, verificação gráfica automatizada e vídeo.
- Tarefa de commit do PRD: suspensa pelo usuário; nenhum commit realizado.
- Sprint 1: **não iniciada e não autorizada**.
- PRD original: lido e preservado; não editar.
- Commits, tags, pushes e publicação: não autorizados.
- Preservar Python global 3.14 e `.venv`; não usar sudo, instalar SDL ou
  bibliotecas no sistema operacional, nem alterar permissões automaticamente.
- Se uma instalação falhar, informar erro completo antes de outras alterações
  no ambiente. Instalar exclusivamente pacotes pré-compilados.

## Implementação atual

Instruções compartilhadas em `AGENTS.md`, quatro documentos de projeto,
README, .gitignore, dependências separadas, pacote `evolife` com configuração
e `main.py` com janela preta 800 × 600. Fechar, Esc e Ctrl+C encerram com
liberação em `finally`. Testes de ciclo de vida usam SDL `dummy`.
Não foram implementados mundo, criaturas, movimento ou qualquer regra de simulação.

## Ambiente observado

- Plataforma: Linux, shell bash.
- Python global e do `.venv`: 3.14.4.
- `.venv` criado na primeira parte da sessão e preservado após nova instrução.
- pip inicial do `.venv`: 25.1.1.
- Git já existia, branch `main`, sem commits; não foi reinicializado.
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
- Suspender tarefa de commit do PRD por determinação explícita do usuário.

## Dificuldades encontradas

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

## Verificações e evidências

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

## Arquivos entregues

- `AGENTS.md`, `README.md` e `.gitignore`.
- `requirements.txt`, `requirements-dev.txt` e `pytest.ini`.
- `main.py`, `evolife/__init__.py` e `evolife/config.py`.
- `tests/conftest.py` e `tests/test_application.py`.
- `docs/ARCHITECTURE.md`, `docs/SPRINTS.md`, `docs/TASKS.md` e esta memória.
- `docs/media/sprint0.mp4`; `.venv` local criado e preservado, ignorado pelo Git.

Os arquivos preexistentes, incluindo PRD e diretórios .git/.agents/.codex/.aws,
foram preservados. Os arquivos de entrega estão novos e ainda não rastreados;
nenhum git add, commit, tag ou push foi executado.

## Próxima ação

Entrega da Sprint 0 disponível para revisão. O usuário pode executar
`source .venv/bin/activate` e `python main.py` para inspecionar a janela.
Qualquer commit ou trabalho da Sprint 1 depende de autorização explícita.
Quando a Sprint 1 for autorizada, começar por uma Creature e pelo teste de
movimento descrito em `SPRINTS.md`, antes de gerar a população inteira.
