# Demonstração genética — Sprint 4

Cenário controlado: `World(seed=42)` com todos os parâmetros oficiais
padrão. Área 800 × 600; dez criaturas na geração 0, energia 100,
idade/cooldown zero; velocidades iniciais sorteadas entre 25 e 90,
visão 100 e eficiência 1. Comida inicial 75, reposição 1/s até 125.
3600 passos de 1/60 s, totalizando 60 s lógicos.

Reprodução: idade ≥10 s, energia ≥110 após metabolismo e cooldown
encerrado; transferência 45, filhote com energia 45, espera 10 s.
Cada gene: chance 12%, normal centrada em zero, desvio de 8% da
amplitude (speed 5,2; vision 10; efficiency 0,032); valores limitados
às faixas do PRD. Nenhuma regra foi alterada para produzir nascimentos.

Resultado: **26 nascimentos**, **6 mortes**,
população máxima **34**, final **30**; geração
máxima observada **3**.

Genes na ordem `(speed, vision, efficiency)`, arredondados a seis casas.
IDs e genes foram capturados no nascimento, inclusive de progenitores
que morreram depois. 'Nenhum' indica ausência de mudança no valor;
um sorteio de mutação com variação nula ou limitada pode não alterá-lo.

| Tempo (s) | Progenitor | Descendente | Geração | Genes do progenitor | Genes do descendente | Genes alterados |
| --- | --- | --- | --- | --- | --- | --- |
| 10.000000 | 0 | 10 | 1 | (39.508698, 100.000000, 1.000000) | (39.508698, 100.000000, 1.000000) | nenhum |
| 10.000000 | 1 | 11 | 1 | (30.651024, 100.000000, 1.000000) | (30.651024, 100.000000, 1.000000) | nenhum |
| 10.000000 | 2 | 12 | 1 | (57.848094, 100.000000, 1.000000) | (57.848094, 100.000000, 1.000000) | nenhum |
| 10.000000 | 3 | 13 | 1 | (60.421196, 100.000000, 1.000000) | (60.421196, 100.000000, 1.000000) | nenhum |
| 10.000000 | 4 | 14 | 1 | (25.422419, 100.000000, 1.000000) | (25.422419, 100.000000, 1.000000) | nenhum |
| 10.000000 | 5 | 15 | 1 | (35.106167, 100.000000, 1.000000) | (25.000000, 100.000000, 1.029832) | speed, efficiency |
| 10.000000 | 6 | 16 | 1 | (31.286564, 100.000000, 1.000000) | (31.286564, 100.000000, 1.000000) | nenhum |
| 10.000000 | 7 | 17 | 1 | (72.432566, 100.000000, 1.000000) | (72.432566, 100.000000, 1.000000) | nenhum |
| 10.000000 | 8 | 18 | 1 | (60.882641, 100.000000, 1.000000) | (62.677782, 100.000000, 1.000000) | speed |
| 10.000000 | 9 | 19 | 1 | (62.527889, 100.000000, 1.000000) | (58.525581, 100.000000, 1.000000) | speed |
| 20.000000 | 6 | 20 | 1 | (31.286564, 100.000000, 1.000000) | (31.286564, 100.000000, 1.000000) | nenhum |
| 20.000000 | 7 | 21 | 1 | (72.432566, 100.000000, 1.000000) | (71.510785, 100.000000, 1.000000) | speed |
| 20.000000 | 8 | 22 | 1 | (60.882641, 100.000000, 1.000000) | (60.882641, 100.000000, 1.024843) | efficiency |
| 20.000000 | 9 | 23 | 1 | (62.527889, 100.000000, 1.000000) | (62.527889, 100.000000, 1.000000) | nenhum |
| 20.000000 | 13 | 24 | 2 | (60.421196, 100.000000, 1.000000) | (60.421196, 100.000000, 1.000000) | nenhum |
| 20.000000 | 18 | 25 | 2 | (62.677782, 100.000000, 1.000000) | (62.677782, 100.000000, 1.000000) | nenhum |
| 20.000000 | 19 | 26 | 2 | (58.525581, 100.000000, 1.000000) | (58.525581, 100.000000, 1.000000) | nenhum |
| 30.000000 | 13 | 27 | 2 | (60.421196, 100.000000, 1.000000) | (60.421196, 100.000000, 1.000000) | nenhum |
| 30.300000 | 3 | 28 | 1 | (60.421196, 100.000000, 1.000000) | (60.421196, 100.000000, 1.000000) | nenhum |
| 31.216667 | 2 | 29 | 1 | (57.848094, 100.000000, 1.000000) | (57.848094, 100.000000, 1.000000) | nenhum |
| 33.166667 | 18 | 30 | 2 | (62.677782, 100.000000, 1.000000) | (62.677782, 100.000000, 1.000000) | nenhum |
| 39.000000 | 0 | 31 | 1 | (39.508698, 100.000000, 1.000000) | (39.508698, 100.000000, 1.002073) | efficiency |
| 41.550000 | 24 | 32 | 3 | (60.421196, 100.000000, 1.000000) | (60.421196, 100.000000, 1.000000) | nenhum |
| 43.166667 | 18 | 33 | 2 | (62.677782, 100.000000, 1.000000) | (62.677782, 100.000000, 0.978295) | efficiency |
| 53.616667 | 19 | 34 | 2 | (58.525581, 100.000000, 1.000000) | (58.525581, 100.000000, 1.050678) | efficiency |
| 57.216667 | 25 | 35 | 3 | (62.677782, 100.000000, 1.000000) | (62.677782, 100.000000, 1.022780) | efficiency |

Exemplo de linhagem: **8 → 18 → 25 → 35**, gerações **0 → 1 → 2 → 3**.
O ID 18 herdou visão/eficiência e teve variação em speed; o ID 25
herdou todos os valores; o ID 35 herdou speed/vision e teve variação
em efficiency. A execução não apresentou mudança em vision, embora
esse gene use a mesma regra independente, validada pelos testes.

Reprodução do relatório, na raiz com o .venv ativado:

```bash
python -m scripts.demonstrate_genetics
```

A [mídia da Sprint 4](media/sprint4.gif) contém 225 quadros a 15 FPS,
15 s de mídia para 60 s lógicos (4x). Renderização fora da tela,
sem janela de desktop; legendas e anéis existem somente na mídia.
Para regenerar, com ffmpeg disponível:

```bash
python -m scripts.demonstrate_genetics --gif docs/media/sprint4.gif
```

Limites: demonstração de herança e variação em uma execução; não prova
adaptação nem favorecimento causal de genes. Sem coleta de médias,
HUD ou exportação CSV; não é um experimento comparativo de seleção.
A inspeção manual no desktop e a validação Windows estavam pendentes no
momento da geração deste relatório.

Atualização posterior: o usuário relatou execução da aplicação e da suíte
da Sprint 4 no Ubuntu sem identificar erros; a revisão estática externa após
o commit/push para develop não identificou problemas bloqueantes. Esse relato
é separado dos 192 testes executados pelo Codex na entrega técnica. A execução
Windows permanece pendente. A atualização documental não altera os dados da
demonstração acima; o script reproduz o relatório original, sem esta nota.
Detalhes em [PROJECT_STATE.md](PROJECT_STATE.md).
