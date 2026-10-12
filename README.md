# EvoLife

Laboratório desktop 2D de vida e evolução artificial, feito em Python.
O objetivo futuro é observar criaturas buscando alimento, reproduzindo-se e
transmitindo genes. **A implementação atual vai até a Sprint 1:**
dez círculos se movem sozinhos em uma janela de 800 × 600 e refletem nas bordas.
O processamento de eventos e o encerramento seguro da Sprint 0 foram preservados.

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

A janela deve mostrar dez círculos azuis claros sobre fundo preto, movendo-se
sem entradas do teclado e refletindo nas bordas. Feche pelo botão da janela,
pressione **Esc** ou use **Ctrl+C** no terminal para sair.
Esses são os únicos comandos implementados nesta sprint.

## Como estudar o movimento

Comece por `evolife/creature.py`: cada criatura guarda x, y, direção em radianos,
velocidade em pixels/s e energia. Com direção zero, velocidade 40 e `dt=0.5`,
a posição `(100, 100)` vira `(120, 100)`, conforme o PRD. O raio de 7 pixels
entra no cálculo das bordas, e a energia permanece 100 nesta sprint.

`World` cria dez criaturas e atualiza a população sem conhecer Pygame.
`Renderer` desenha o estado sem atualizá-lo. `main.py` acumula o tempo medido
pelo relógio e avança o mundo em passos de 1/60 s, independentemente de quantos
quadros são desenhados. A configuração reúne velocidades iniciais de 25 a
90 pixels/s e uma semente interna padrão 42, sem novos controles de usuário.

Não há comida, consumo de energia, reprodução ou genes nesta entrega.

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
Também verificam deslocamento, bordas e cantos, população, desenho e o mesmo
tempo simulado em diferentes cadências de renderização. Há uma execução de
60 segundos lógicos que verifica as bordas de cada criatura a cada passo.
Para verificar a aparência, execute `python main.py` no desktop e encerre
com Esc ou pelo botão. O driver `dummy` não comprova a aparência no monitor.

Os 33 testes passaram com Python 3.14.4, pygame-ce 2.5.8 e pytest 9.1.1,
incluindo os sete casos da Sprint 0. A verificação gráfica X11 também passou;
veja a [demonstração de 15 segundos da Sprint 1](docs/media/sprint1.gif).
A [demonstração anterior](docs/media/sprint0.mp4)
da janela vazia continua preservada. Resultados completos, verificação gráfica
e limites estão em [PROJECT_STATE.md](docs/PROJECT_STATE.md).

Se a instalação falhar, preserve a mensagem completa e consulte
[PROJECT_STATE.md](docs/PROJECT_STATE.md). O uso de `--only-binary=:all:`
interrompe a instalação quando não existe um pacote pré-compilado compatível;
não tente compilação, sudo, SDL do sistema ou trocar o Python como solução automática.

## Organização e continuidade

```text
EvoLife_PRD_Roadmap.md     Especificação original, preservada
AGENTS.md                Instruções comuns para Codex CLI e OpenCode CLI
main.py                  Janela, eventos e tempo fixo
requirements.txt         pygame-ce, execução
requirements-dev.txt     pytest, desenvolvimento
pytest.ini               Descoberta dos testes
evolife/config.py         Parâmetros de janela e movimento
evolife/creature.py       Estado e movimento da criatura
evolife/world.py          População e atualização do mundo
evolife/renderer.py       Desenho dos círculos com Pygame
tests/                   Movimento, mundo, desenho, tempo e ciclo de vida
docs/ARCHITECTURE.md      Arquitetura e decisões técnicas
docs/SPRINTS.md           Roteiro e portões de cada sprint
docs/TASKS.md             Tarefas e evidências de conclusão
docs/PROJECT_STATE.md     Memória compartilhada e resultados da sessão
```

Leia `AGENTS.md` e a memória compartilhada antes de alterar o projeto em
qualquer CLI. A Sprint 1 está concluída e aguarda revisão do usuário. A Sprint 2
e novos commits exigem autorização explícita.
