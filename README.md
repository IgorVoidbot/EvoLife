# EvoLife

Laboratório desktop 2D de vida e evolução artificial, feito em Python.
O objetivo futuro é observar criaturas buscando alimento, reproduzindo-se e
transmitindo genes. **A implementação atual contém somente a Sprint 0:**
uma janela preta de 800 × 600, com processamento de eventos e encerramento seguro.

## Requisitos

- Python 3.14 com `venv` (ambiente atual: Python 3.14.4).
- Ambiente gráfico para abrir a janela; Linux é a plataforma inicial.
- Internet para instalar dependências pela primeira vez; depois a aplicação
  funciona localmente, sem APIs ou serviços externos.

Usamos `pygame-ce==2.5.8` por compatibilidade com Python 3.14. A distribuição
continua fornecendo o módulo `pygame`; não instale `pygame` e `pygame-ce`
no mesmo ambiente. A [distribuição oficial](https://pypi.org/project/pygame-ce/2.5.8/)
documenta suporte a Python 3.14. A decisão está em
[ARCHITECTURE.md](docs/ARCHITECTURE.md). O PRD original foi preservado.

## Instalação e execução no Linux

Na raiz do projeto, crie um ambiente somente se ainda não existir:

```bash
python3 --version
# Execute apenas em uma instalação nova, sem .venv:
python3 -m venv .venv
```

No projeto atual, **reuse o `.venv` existente**, sem recriá-lo:

```bash
source .venv/bin/activate
python -m pip install --only-binary=:all: --no-cache-dir -r requirements.txt
python -c "import pygame; print(pygame.version.ver)"
python main.py
```

A janela deve permanecer preta e responsiva. Feche pelo botão da janela,
pressione **Esc** ou use **Ctrl+C** no terminal para sair.
Não há criaturas nem outros controles nesta sprint.

No Windows, em uma instalação nova, crie o ambiente com `py -3.14 -m venv .venv`
e ative no PowerShell com `.venv\Scripts\Activate.ps1`; os comandos `python`
acima continuam iguais. A execução no Windows ainda não foi validada.

## Desenvolvimento e testes

`requirements.txt` contém apenas a dependência de execução.
`requirements-dev.txt` inclui a dependência de execução e o `pytest`.

```bash
source .venv/bin/activate
python -m pip install --only-binary=:all: --no-cache-dir -r requirements-dev.txt
python -m pytest -q
python -m pip check
python -m compileall -q main.py evolife tests
```

Os testes usam o driver SDL `dummy`: verificam dimensão, título, redesenho,
eventos de encerramento e liberação de recursos sem depender do desktop.
Para verificar a aparência, execute `python main.py` no desktop e encerre
com Esc ou pelo botão. O driver `dummy` não comprova a aparência no monitor.

Nesta entrega, os sete testes passaram com Python 3.14.4, pygame-ce 2.5.8
e pytest 9.1.1. Uma verificação automatizada com janela real X11 também
validou redesenho e encerramento. A [demonstração de cinco segundos](docs/media/sprint0.mp4)
captura somente o conteúdo da janela EvoLife. Resultados completos e limites
estão em [PROJECT_STATE.md](docs/PROJECT_STATE.md).

Se a instalação falhar, preserve a mensagem completa e consulte
[PROJECT_STATE.md](docs/PROJECT_STATE.md). O uso de `--only-binary=:all:`
interrompe a instalação quando não existe um pacote pré-compilado compatível;
não tente compilação, sudo, SDL do sistema ou trocar o Python como solução automática.

## Organização e continuidade

```text
EvoLife_PRD_Roadmap.md     Especificação original, preservada
AGENTS.md                Instruções comuns para Codex CLI e OpenCode CLI
main.py                  Janela e loop de eventos da Sprint 0
requirements.txt         pygame-ce, execução
requirements-dev.txt     pytest, desenvolvimento
pytest.ini               Descoberta dos testes
evolife/                 Pacote Python e configuração da janela
tests/                   Verificação da aplicação com SDL dummy
docs/ARCHITECTURE.md      Arquitetura e decisões técnicas
docs/SPRINTS.md           Roteiro e portões de cada sprint
docs/TASKS.md             Tarefas e evidências de conclusão
docs/PROJECT_STATE.md     Memória compartilhada e resultados da sessão
```

Leia `AGENTS.md` e a memória compartilhada antes de alterar o projeto em
qualquer CLI. A Sprint 1 e o primeiro commit aguardam autorização do usuário.
