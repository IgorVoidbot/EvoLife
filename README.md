# EvoLife

Laboratório desktop 2D de vida e evolução artificial, feito em Python.
O objetivo futuro é observar reprodução e transmissão de genes.
**A implementação atual vai até a Sprint 2:** dez criaturas se movimentam,
buscam pontos verdes de comida, gastam energia e morrem quando ela acaba.
Movimento com reflexão, passos fixos e encerramento seguro foram preservados.

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

A janela começa com dez círculos azuis claros e 75 pontos verdes sobre fundo
preto. As criaturas procuram alimento, refletem nas bordas e podem morrer;
a comida consumida desaparece e novos pontos surgem pelo tempo simulado. Feche pelo botão da janela,
pressione **Esc** ou use **Ctrl+C** no terminal para sair.
Esses são os únicos comandos implementados nesta sprint.

## Movimento e sobrevivência

Comece por `evolife/creature.py`: cada criatura guarda x, y, direção em radianos,
velocidade em pixels/s, energia, visão e eficiência. Com direção zero, velocidade 40 e `dt=0.5`,
a posição `(100, 100)` vira `(120, 100)`, conforme o PRD. O raio de 7 pixels
entra no cálculo das bordas. `Creature.update` trata o movimento; `World.update`
coordena a busca, a alimentação, o gasto energético e as mortes.

`World` cria dez criaturas e 75 alimentos e atualiza o domínio sem Pygame.
`Renderer` desenha o estado sem atualizá-lo. `main.py` acumula o tempo medido
pelo relógio e avança o mundo em passos de 1/60 s, independentemente de quantos
quadros são desenhados. A configuração reúne velocidades iniciais de 25 a
90 pixels/s e uma semente interna padrão 42, sem novos controles de usuário.

A visão inicial é 100 pixels e a eficiência é 1,0, atributos simples ainda
sem herança. A criatura segue o alimento mais próximo dentro da visão. Sem
alvo, mantém a direção e sorteia outra após 1 a 3 segundos de exploração.

A energia começa em 100; o gasto por segundo segue
`(0.55 + 0.012 * speed + 0.003 * vision) * efficiency`.
Cada alimento repõe 45 pontos até o teto de 130. O contato considera os raios
de criatura (7) e comida (3), antes e depois do movimento. Depois de comer,
a criatura paga o gasto do passo e sai da população se atingir zero.
Criaturas já mortas não comem nem se movem. Na disputa por uma unidade,
a primeira criatura em contato na ordem da população a consome.

A reposição é de 1 alimento por segundo simulado até 125 unidades, sem crédito
acumulado enquanto o mapa estiver cheio. Mesmo sem criaturas, a aplicação
continua desenhando, repondo alimento e aceitando comandos de encerramento.
Reprodução, herança, indicadores e controles novos aguardam suas sprints.

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

Os **71 testes** passaram com Python 3.14.4, pygame-ce 2.5.8 e pytest 9.1.1.
Incluem busca, consumo, competição, fórmula de energia, teto, remoção de
mortos, reposição, extinção e os comportamentos das sprints anteriores.
Veja a [demonstração de alimentação da Sprint 2](docs/media/sprint2.gif):
cena preparada com uma criatura de energia 30, mostrando busca e recuperação.
O GIF foi renderizado fora da tela; suas legendas de energia são exclusivas
da demonstração e não fazem parte da interface atual.

A [demonstração da Sprint 1](docs/media/sprint1.gif), validada com X11 naquela
sprint, e o [vídeo da Sprint 0](docs/media/sprint0.mp4) foram preservados.
Nesta Sprint 2 não houve verificação com driver gráfico de desktop nem
inspeção manual pelo usuário. Resultados e limites estão em
[PROJECT_STATE.md](docs/PROJECT_STATE.md).

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
evolife/config.py         Parâmetros de janela, movimento e sobrevivência
evolife/creature.py       Movimento, busca e energia
evolife/world.py          População, interações, morte e reposição
evolife/food.py           Posição de alimento, sem Pygame
evolife/renderer.py       Desenho dos círculos com Pygame
tests/                   Movimento, mundo, desenho, tempo e ciclo de vida
docs/ARCHITECTURE.md      Arquitetura e decisões técnicas
docs/SPRINTS.md           Roteiro e portões de cada sprint
docs/TASKS.md             Tarefas e evidências de conclusão
docs/PROJECT_STATE.md     Memória compartilhada e resultados da sessão
```

Leia `AGENTS.md` e a memória compartilhada antes de alterar o projeto em
qualquer CLI. A Sprint 1 foi aprovada e integrada à main pelo PR #1. A entrega
técnica da Sprint 2 está concluída e aguarda revisão. Sprint 3 não autorizada;
commits, pushes e merges continuam exigindo autorização explícita.
