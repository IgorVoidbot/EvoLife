# EvoLife

Laboratório desktop 2D de vida e evolução artificial, feito em Python.
O objetivo futuro é investigar evolução com mutações e dados.
**A implementação atual vai até a Sprint 3:** criaturas se movimentam,
buscam comida, gastam energia, morrem e geram descendentes por reprodução
assexuada. A população começa com dez e pode aumentar ou diminuir.
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
preto. As criaturas procuram alimento, refletem nas bordas, podem reproduzir
e morrer; a comida consumida desaparece e novos pontos surgem pelo tempo
simulado. Feche pelo botão da janela,
pressione **Esc** ou use **Ctrl+C** no terminal para sair.
Esses são os únicos comandos implementados nesta sprint.

## Movimento e sobrevivência

Comece por `evolife/creature.py`: cada criatura guarda x, y, direção em radianos,
velocidade em pixels/s, energia, visão e eficiência. Com direção zero, velocidade 40 e `dt=0.5`,
a posição `(100, 100)` vira `(120, 100)`, conforme o PRD. O raio de 7 pixels
entra no cálculo das bordas. `Creature.update` trata o movimento; `World.update`
coordena busca, alimentação, metabolismo, idade, nascimentos e mortes.

`World` cria dez criaturas e 75 alimentos e atualiza o domínio sem Pygame.
`Renderer` desenha o estado sem atualizá-lo. `main.py` acumula o tempo medido
pelo relógio e avança o mundo em passos de 1/60 s, independentemente de quantos
quadros são desenhados. A configuração reúne velocidades iniciais de 25 a
90 pixels/s e uma semente interna padrão 42, sem novos controles de usuário.

A visão inicial é 100 pixels e a eficiência é 1,0. Esses atributos simples
são copiados nos descendentes, sem mutação. A criatura segue o alimento mais próximo dentro da visão. Sem
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
## Reprodução e ciclo de vida

A criatura pode reproduzir quando sua idade chega a 10 segundos, sua energia
é pelo menos 110 e o cooldown está encerrado. Esses requisitos são avaliados
depois de comer e pagar o metabolismo do passo. O progenitor transfere 45
pontos ao filhote e espera 10 segundos até poder reproduzir novamente.
O nascimento conserva a energia disponível naquele instante.

O filhote nasce próximo ao progenitor e dentro das bordas, com energia 45,
idade zero, novo ID e geração do progenitor +1. Copia velocidade, visão e
eficiência sem mutações. Passa a agir apenas no próximo passo lógico.
IDs nunca são reutilizados no experimento; `World` guarda os totais de
nascimentos e mortes. A população inicial não conta como nascimento.

Não há HUD nesta sprint: os contadores estão disponíveis no domínio e nos
testes. Estrutura genética, mutações, painel, CSV e controles aguardam suas
sprints. Com população zerada, a aplicação continua funcionando e repondo
comida, sem recriar criaturas automaticamente.

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

Os **103 testes** passaram com Python 3.14.4, pygame-ce 2.5.8 e pytest 9.1.1.
Incluem busca, consumo, competição, fórmula de energia, teto, remoção de
mortos, reposição, extinção e os comportamentos das sprints anteriores.
Também verificam idade, cooldown, bloqueios de reprodução, conservação de
energia no nascimento, posição, IDs, geração, eventos e determinismo.
Veja a [demonstração de nascimentos da Sprint 3](docs/media/sprint3.gif):
configuração padrão, seed 42, dez criaturas e 75 alimentos iniciais, energia
100, idade zero, passos de 1/60 s. Em 60 s simulados ocorreram 28 nascimentos
e 5 mortes; população máxima 34 e final 33. O GIF dura 15 s e exibe a execução
a 4x. Legendas e anéis de nascimento foram adicionados somente à mídia,
renderizada fora da tela; as regras de energia e reprodução são as reais.
O usuário executou manualmente o EvoLife da Sprint 3 no Ubuntu e não identificou
erros. Esse relato complementa os 103 testes automatizados anteriores, cujos
resultados foram preservados.

A [demonstração de alimentação da Sprint 2](docs/media/sprint2.gif) mostra:
cena preparada com uma criatura de energia 30, mostrando busca e recuperação.
O GIF foi renderizado fora da tela; suas legendas de energia são exclusivas
da demonstração e não fazem parte da interface atual.

A [demonstração da Sprint 1](docs/media/sprint1.gif), validada com X11 naquela
sprint, e o [vídeo da Sprint 0](docs/media/sprint0.mp4) foram preservados.
Na Sprint 2 o usuário executou manualmente aplicação e testes no Ubuntu sem
identificar erros. Na Sprint 3 os testes usam SDL dummy e o GIF foi renderizado
fora da tela; não houve execução com driver gráfico de desktop pelo agente.
Resultados e limites estão em
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
evolife/creature.py       Movimento, busca, energia e ciclo básico
evolife/world.py          População, reprodução, morte, totais e reposição
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
da Sprint 2 foi aprovada e integrada pelo PR #3 (3b75b6e). Sprint 3 autorizada
com entrega técnica concluída e aguardando revisão. Sprint 4 não autorizada;
commits, pushes e merges continuam exigindo autorização explícita.
