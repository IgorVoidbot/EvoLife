# EvoLife — PRD e Plano de Sprints

**Produto:** EvoLife — Simulador de Vida e Evolução Artificial  
**Versão do documento:** 1.0  
**Data:** 11 de outubro de 2026  
**Status:** Planejamento inicial  
**Responsável:** Desenvolvedor individual  
**Stack proposta:** Python 3 + Pygame + biblioteca padrão; pytest para testes  
**Plataforma inicial:** Desktop (Linux; portável para Windows)  
**Custo planejado:** R$ 0 em licenças e serviços

> **Princípio do projeto:** cada sprint deve terminar com uma mudança que possa ser vista, executada ou medida. Concluir uma simulação simples vale mais que começar uma IA avançada e não terminar.

## 1. Resumo executivo

EvoLife é um laboratório interativo em 2D no qual criaturas autônomas se movimentam, procuram alimento, gastam energia, morrem e geram descendentes. Cada criatura possui características herdáveis. Pequenas mutações e a sobrevivência diferencial podem alterar essas características ao longo das gerações.

O projeto combina **diversão e descoberta** (observar um mundo vivo) com **aprendizado técnico** (Python, orientação a objetos, simulação, algoritmos, testes, métricas e, futuramente, inteligência artificial). A primeira versão deve rodar inteiramente no computador do desenvolvedor, sem servidor, APIs pagas ou equipamentos de VR.

**Entrega central:** um ambiente em que seja possível iniciar uma população, observar seu ciclo de vida e verificar, com dados, como suas características mudam ao longo do tempo.

**Não confundir:** evolução genética ocorre *entre gerações* por hereditariedade, mutação e seleção; aprendizado individual ocorre *durante a vida* de uma criatura. EvoLife implementará evolução primeiro. Redes neurais e aprendizado serão experimentos posteriores, não dependências do MVP.

### 1.1 Marcos de entrega

| Marco | Quando | Resultado demonstrável |
| --- | --- | --- |
| Protótipo visual | Fim da Sprint 1 | 10 criaturas se movem e respeitam as bordas. |
| Ecossistema básico | Fim da Sprint 2 | Criaturas encontram comida, gastam energia e morrem. |
| População dinâmica | Fim da Sprint 3 | Nascimentos e mortes alteram a população. |
| **MVP Evolutivo** | **Fim da Sprint 4** | Descendentes herdam genes com mutação; gerações podem ser observadas. |
| Laboratório mensurável | Fim da Sprint 6 | Métricas, controles, sementes e experimentos repetíveis. |
| **Versão 1.0** | **Fim da Sprint 7** | Projeto testado, documentado e pronto para demonstrar no GitHub. |

## 2. Problema e oportunidade

Muitos projetos de estudo concentram o esforço em infraestrutura ou formulários e oferecem pouco retorno visual no começo. EvoLife deve converter conceitos de programação em fenômenos observáveis: fome, busca, crescimento populacional, competição por recursos e mudanças nas características herdáveis.

O desafio de produto é manter a simulação **simples o bastante para terminar**, mas **rica o bastante para gerar perguntas novas**. Exemplos: criaturas mais rápidas sobrevivem melhor? Visão maior compensa o custo energético? O que acontece quando a comida fica escassa? Os resultados são hipóteses a investigar, não conclusões pré-programadas.

## 3. Público, usuário e proposta de valor

**Usuário primário:** estudante/desenvolvedor solo interessado em programação, simulações, IA e mundos virtuais.  
**Usuário secundário:** pessoa que acessa o repositório e quer executar, entender ou reproduzir um experimento.  
**Proposta de valor:** aprender sistemas complexos construindo um mundo observável, incremental, local e gratuito.

### 3.1 Histórias de usuário

| ID | Como usuário, quero… | Para… | Prioridade |
| --- | --- | --- | --- |
| US-01 | abrir uma janela e ver criaturas se movendo | confirmar rapidamente que o mundo está vivo | P0 |
| US-02 | ver criaturas encontrando e consumindo comida | observar sobrevivência sem controlar indivíduos | P0 |
| US-03 | ver nascimento, morte e geração de descendentes | acompanhar a dinâmica populacional | P0 |
| US-04 | observar genes herdados e pequenas mutações | testar evolução ao longo das gerações | P0 |
| US-05 | acompanhar população e valores médios dos genes | diferenciar impressão visual de evidência | P1 |
| US-06 | pausar, reiniciar e mudar parâmetros | realizar experimentos interativos | P1 |
| US-07 | repetir o mesmo experimento usando uma semente | comparar regras com maior confiabilidade | P1 |
| US-08 | exportar medições e consultar instruções | estudar resultados e mostrar o projeto | P1 |
| US-09 | testar predadores e ambientes diferentes | ampliar a complexidade do ecossistema | P2 |
| US-10 | experimentar um controlador neural | investigar aprendizado, sem confundi-lo com evolução | P2 |

## 4. Objetivos, métricas e limites

### 4.1 Objetivos do produto

1. Produzir feedback visual já na primeira sprint de implementação.
2. Simular movimento, comida, energia, morte e reprodução sem intervenções manuais.
3. Implementar transmissão de genes, mutação configurável e identificação de geração.
4. Oferecer dados para analisar mudanças da população sem alegar que toda mudança é adaptação.
5. Manter o projeto compreensível, testável, executável localmente e publicável no GitHub.

### 4.2 Critérios de sucesso da versão 1.0

- Executar no Linux com instruções de instalação claras e sem serviços externos.
- Rodar uma simulação de **15 minutos** sem travamento ou exceções não tratadas, inclusive se ocorrer extinção.
- Reproduzir, com a mesma configuração e semente, os mesmos eventos em testes automatizados de simulação com passo de tempo fixo.
- Com uma configuração de demonstração ajustada, observar **ao menos 5 nascimentos** em até 5 minutos simulados (sem prometer que toda configuração gera sobrevivência).
- Exibir contadores de vivos, nascimentos, mortes e geração máxima; registrar médias de pelo menos velocidade e visão.
- Passar nos testes de borda, energia, morte, reprodução, limites dos genes e determinismo.
- Conter README com capturas ou GIF, instruções de uso, decisões técnicas e explicação das regras.

### 4.3 Fora de escopo até a versão 1.0

Sem VR, Unity, mundo 3D, multiplayer, serviços web, banco de dados, aprendizado por reforço, redes neurais, sistemas biológicos realistas ou simulação de milhares de agentes. Qualquer ideia dessas vai ao **Backlog de Experimentos** e não interrompe o escopo da sprint atual.

## 5. Experiência do usuário

### 5.1 Tela principal

Janela **800 × 600 pixels** em fundo escuro, com criaturas representadas por círculos, alimentos representados por pontos verdes e um painel de indicadores. O movimento deve ser visível sem depender de sprites ou arte externa. Cores e tamanhos precisam diferenciar comida de criaturas; oferecer rótulos no painel para não depender somente de cores.

### 5.2 Fluxo principal

1. Abrir EvoLife e carregar a configuração padrão.
2. Iniciar uma população com 10 criaturas e alimento inicial.
3. Acompanhar criaturas procurando alimento, perdendo energia e, se houver recursos, reproduzindo-se.
4. Observar indicadores de população, nascimentos, mortes e características médias.
5. Pausar ou reiniciar a simulação com uma semente conhecida; experimentar alterações de parâmetros.
6. Salvar um arquivo CSV e analisar os resultados fora do aplicativo.

### 5.3 Comandos planejados

| Comando | Ação | Entrega |
| --- | --- | --- |
| Espaço | Pausar/continuar | Sprint 6 |
| R | Reiniciar com a configuração e semente atuais | Sprint 6 |
| N | Avançar um passo de simulação quando pausado | Sprint 6 |
| + / - | Alterar velocidade da simulação | Sprint 6 |
| H | Mostrar/ocultar ajuda | Sprint 6 |
| Esc / fechar janela | Encerrar com segurança | Sprint 0 |

Os atalhos só serão considerados concluídos quando aparecerem na ajuda e no README.

## 6. Regras de domínio: especificação inicial

Os valores a seguir são **parâmetros iniciais de design**, não constantes científicas. Devem ficar em `config.py` e poderão ser calibrados após testes. A meta é gerar um ecossistema interessante e observável.

### 6.1 Mundo e tempo

- Área inicial: 800 × 600 pixels; posição como números de ponto flutuante `(x, y)`.
- Janela renderizada até 60 quadros por segundo, mas o motor lógico avança em **passos fixos de 1/60 segundo**. Renderização e atualização da simulação são separadas.
- Semente pseudoaleatória (`seed`) configurável. A simulação usa uma instância própria de gerador aleatório, para facilitar repetibilidade.
- Nascimentos e mortes devem ser aplicados de maneira segura, sem modificar a coleção percorrida no mesmo laço.
- Cada criatura permanece dentro das bordas; na primeira versão, reflete a direção ao chegar nelas.

### 6.2 Criatura

| Atributo | Tipo / regra | Observação |
| --- | --- | --- |
| `id` | inteiro único | Não reutilizar identificadores no mesmo experimento. |
| `x`, `y` | `float` | Coordenadas do mundo. |
| `direction` | ângulo em radianos | Pode mudar durante a busca. |
| `energy` | `float`, de 0 até 130 | Se chegar a 0, morre. |
| `age_seconds` | `float` | Aumenta a cada passo lógico. |
| `generation` | inteiro ≥ 0 | Filhote = geração do progenitor + 1. |
| `speed` | gene: 25 a 90 pixels/s | Maior velocidade pode custar mais energia. |
| `vision` | gene: 35 a 160 pixels | Maior visão pode custar mais energia. |
| `efficiency` | gene: 0,8 a 1,2 | Multiplicador do gasto energético; menor = mais eficiente. |
| `reproduction_cooldown` | segundos | Evita reprodução contínua. |

**Movimento:** procurar o alimento visível mais próximo. Se não houver comida no raio de visão, caminhar na direção atual e sortear uma nova direção após um intervalo de 1 a 3 segundos. O algoritmo é intencionalmente simples: **buscar comida não é aprendizado de máquina**.

**Energia:** começar com 100. Como regra inicial, gasto por segundo = `(0,55 + 0,012 × speed + 0,003 × vision) × efficiency`; multiplicar pelo tempo decorrido. Comer repõe 45 pontos, até o máximo de 130. Ajustar esses valores somente mediante experimentos registrados.

**Morte:** remover a criatura da população quando energia ≤ 0. Morte por velhice é opcional e fica desativada inicialmente, para não confundir a seleção por recursos.

### 6.3 Alimento

- Início com 75 unidades, distribuídas pseudoaleatoriamente.
- Cada unidade consumida desaparece quando uma criatura chega a uma distância de colisão (`raio_criatura + raio_comida`).
- Reposição padrão: 1 unidade por segundo de tempo simulado, até 125 unidades existentes.
- Caso a semente gere comida na posição de uma criatura, a interação é válida e deve ser processada normalmente.
- Taxa de reposição pode ser reduzida em experimentos posteriores para estudar escassez.

### 6.4 Reprodução e hereditariedade

- Reprodução **assexuada**, sem parceiro, para reduzir a complexidade inicial.
- Critérios: idade ≥ 10 segundos, energia ≥ 110 e tempo de espera da reprodução encerrado.
- Ao reproduzir: progenitor transfere 45 pontos de energia para o filhote, cuja energia inicial será 45; aplicar espera de 10 segundos ao progenitor. Isso evita criar energia do nada durante o nascimento.
- Filhote nasce próximo ao progenitor, dentro dos limites do mapa, com novo `id`, `generation = parent.generation + 1` e genes copiados do progenitor.
- Cada gene possui **12% de chance de mutação** por nascimento; se ocorrer, aplicar uma variação aleatória pequena (distribuição normal de desvio padrão ≈ 8% da amplitude permitida do gene). Restringir ao intervalo permitido.
- A mutação não tem objetivo nem direção planejada: pode melhorar, piorar ou não alterar o desempenho no ambiente.
- Sem cruzamento genético na versão 1.0. Essa extensão só entra se a versão simples estiver estável.

### 6.5 O que conta como evolução?

Observar variação genética herdável e mudanças na distribuição de genes ao longo de múltiplas gerações. Uma alteração na média sozinha não prova adaptação; pode resultar de acaso, tamanho populacional pequeno ou mudança de condições. Comparações devem considerar semente, ambiente, tempo de simulação e múltiplas execuções quando possível.

## 7. Requisitos funcionais e aceitação

| ID | Requisito funcional | Prioridade | Critério de aceitação | Sprint |
| --- | --- | --- | --- | --- |
| RF-01 | Abrir e encerrar janela sem erros | P0 | Janela abre, redesenha e fecha sem exceção. | 0 |
| RF-02 | Criar e mover 10 criaturas automaticamente | P0 | Posições mudam no tempo sem entradas do usuário. | 1 |
| RF-03 | Impedir saída dos limites do mundo | P0 | Após colisão, coordenadas permanecem na área válida. | 1 |
| RF-04 | Gerar comida e detectar a mais próxima dentro da visão | P0 | Criatura dentro do alcance se dirige a um alimento. | 2 |
| RF-05 | Consumir alimento e atualizar energia | P0 | Comida desaparece e energia aumenta sem ultrapassar 130. | 2 |
| RF-06 | Consumir energia e remover criaturas mortas | P0 | Energia diminui; criatura com energia ≤ 0 deixa de atualizar/desenhar. | 2 |
| RF-07 | Gerar descendentes mediante regras | P0 | Nascimento respeita idade, energia, transferência e espera. | 3 |
| RF-08 | Herdar genes e aplicar mutações dentro dos limites | P0 | Genes copiados ou modificados segundo probabilidade e limites. | 4 |
| RF-09 | Rastrear identificador e geração | P0 | IDs únicos; cada filhote recebe geração do progenitor + 1. | 4 |
| RF-10 | Mostrar indicadores populacionais | P1 | Tela mostra vivos, nascimentos, mortes e geração máxima. | 5 |
| RF-11 | Registrar médias genéticas ao longo do tempo | P1 | Amostras registram pelo menos velocidade e visão médias. | 5 |
| RF-12 | Exportar CSV | P1 | Arquivo tem cabeçalho, tempos crescentes e dados utilizáveis. | 5 |
| RF-13 | Pausar, avançar um passo e reiniciar | P1 | Estado só muda conforme comando; reinício limpa contadores. | 6 |
| RF-14 | Configurar parâmetros e semente | P1 | Nova execução lê configurações e pode ser repetida. | 6 |
| RF-15 | Distribuir README, testes e mídia de demonstração | P1 | Terceiro consegue instalar e rodar seguindo instruções. | 7 |
| RF-16 | Predadores e novos ambientes | P2 | Experimento opcional isolado do escopo 1.0. | 8+ |
| RF-17 | Controlador neural opcional | P2 | Experimento compara regras fixas e controlador neural. | 9+ |

## 8. Requisitos não funcionais

| ID | Categoria | Requisito / validação |
| --- | --- | --- |
| RNF-01 | Custo | Executar offline, com software gratuito e sem APIs pagas. |
| RNF-02 | Portabilidade | Linux suportado inicialmente; nenhuma regra de domínio pode depender do sistema operacional. |
| RNF-03 | Desempenho | Meta de renderização fluida com cerca de 100 criaturas no hardware de desenvolvimento; medir antes de prometer um FPS fixo. |
| RNF-04 | Consistência | Usar tempo lógico fixo e fonte de aleatoriedade controlada. |
| RNF-05 | Qualidade | Separar motor de simulação, desenho, regras e configuração; ter testes de unidade para regras críticas. |
| RNF-06 | Manutenibilidade | Preferir nomes descritivos, funções curtas, tipos simples e ausência de números mágicos. |
| RNF-07 | Usabilidade | Estado da simulação e atalhos visíveis; possibilidade de pausar e reiniciar. |
| RNF-08 | Dados | Exportação local em CSV; não coletar dados pessoais. |
| RNF-09 | Robustez | Encerrar corretamente mesmo com população zerada; nenhuma divisão por zero ao calcular médias. |

## 9. Arquitetura proposta

**Abordagem:** motor de simulação separado da interface Pygame. Isso permite testar movimento, energia e reprodução sem abrir uma janela. Começar simples e evitar microsserviços, banco de dados e frameworks web.

```text
EvoLife/
├── main.py                   # Loop de aplicação e entrada
├── requirements.txt          # Dependências mínimas
├── README.md                 # Execução, regras e exemplos
├── .gitignore
├── evolife/
│   ├── __init__.py
│   ├── config.py             # Parâmetros ajustáveis
│   ├── world.py              # Ciclo de atualização e população
│   ├── creature.py           # Estado e ações da criatura
│   ├── food.py               # Estado do alimento
│   ├── genetics.py           # Herança, mutação e limites
│   ├── metrics.py            # Coleta e exportação CSV
│   └── renderer.py           # Exibição Pygame e HUD
├── tests/
│   ├── test_movement.py
│   ├── test_energy.py
│   ├── test_reproduction.py
│   ├── test_genetics.py
│   └── test_determinism.py
└── experiments/              # CSVs e anotações opcionais
```

**Componentes e responsabilidade:**

- `Creature`: contém posição, estado, genes e decisões simples de movimento; não conhece Pygame.
- `World`: mantém criaturas/alimentos, avança o tempo lógico, resolve colisões e agenda nascimentos/mortes.
- `Genetics`: aplica herança, sorteio de mutações e valida limites.
- `Metrics`: transforma estados do mundo em registros e exporta CSV.
- `Renderer`: converte o estado do mundo em círculos, textos e indicadores.
- `Config`: reúne constantes e parâmetros, incluindo `seed`.

**Contrato de atualização sugerido:** `world.update(dt: float) -> None` e `creature.update(dt: float, world_state) -> None`. Antes de implementar a estrutura toda, manter apenas o que a sprint atual precisa. A lista completa é um mapa de chegada, não uma obrigação para a Sprint 1.

### 9.1 Dados persistidos

CSV por experimento, com colunas: `simulation_seconds`, `seed`, `population`, `births_total`, `deaths_total`, `generation_max`, `speed_mean`, `vision_mean`, `efficiency_mean`, `food_count`. Registrar valores agregados a cada 5 segundos simulados. Se não houver criaturas, médias devem ficar vazias no CSV (ou usar um marcador consistente e documentado), nunca provocar erro.

## 10. Planejamento ágil: sprints de execução

**Cadência sugerida:** 1 sprint por semana, com **5 a 8 horas de estudo/desenvolvimento**. Ajustar à rotina; a conclusão dos critérios de aceite importa mais que o calendário. Estimativa base: **8 sprints (0 a 7), aproximadamente 35 a 51 horas**, além de experimentos opcionais. Não desenvolver novas funcionalidades enquanto os critérios da sprint atual estiverem abertos.

### Sprint 0 — Fundação do projeto (2 a 3 horas)

**Objetivo:** ter uma aplicação que executa e um repositório organizado.

**Tarefas:**
1. Criar repositório Git `evolife` e arquivo `.gitignore` de Python.
2. Criar ambiente virtual e instalar `pygame` e `pytest`.
3. Criar `main.py` com janela 800 × 600, loop de eventos e encerramento correto.
4. Criar `README.md` com ideia, instalação e comando para executar.
5. Fazer commit `chore: iniciar projeto EvoLife`.

**Pronto quando:** janela preta abre, continua responsiva e fecha sem erro; outra pessoa consegue seguir o README.

**Demonstração:** vídeo de 5 segundos da janela iniciando e encerrando.

### Sprint 1 — Primeira vida: movimento autônomo (4 a 6 horas)

**Objetivo:** ver criaturas se movimentando sozinhas.

**Tarefas:**
1. Implementar `Creature` com `x`, `y`, `direction`, `speed` e `energy`.
2. Criar um método `update(dt)` para alterar posição.
3. Desenhar a criatura como círculo usando Pygame.
4. Gerar 10 criaturas com posições e direções iniciais diferentes.
5. Fazer reflexão ou correção de posição nas bordas.
6. Criar testes simples de movimento com `dt` conhecido e limites.

**Pronto quando:** 10 círculos se movem sem teclado; nenhum escapa do mundo; o movimento não depende da velocidade de renderização.

**Demonstração:** GIF de 15 segundos. **Commit:** `feat: adicionar movimento autonomo das criaturas`.

**Não fazer ainda:** comida, herança, redes neurais, sprites ou menu.

### Sprint 2 — Sobrevivência: fome e alimento (6 a 8 horas)

**Objetivo:** transformar movimento em comportamento de sobrevivência.

**Tarefas:**
1. Criar classe/estrutura `Food` e espalhar 75 alimentos no mapa.
2. Implementar busca pelo alimento mais próximo dentro do raio de visão.
3. Fazer criatura se dirigir ao alimento detectado; caso contrário, vagar.
4. Detectar colisão, remover alimento e aumentar energia até o teto.
5. Deduzir energia por segundo e retirar criaturas com energia zerada.
6. Repor alimentos até o limite; testar consumo e morte.

**Pronto quando:** uma criatura procura comida visível, ganha energia ao comer e morre quando fica sem energia; mundo continua funcionando com 0 criaturas.

**Demonstração:** observar uma criatura com fome comer e recuperar energia. **Commit:** `feat: implementar alimento e metabolismo`.

### Sprint 3 — Ciclo de vida: reprodução (5 a 7 horas)

**Objetivo:** permitir que a população se renove.

**Tarefas:**
1. Adicionar idade e espera entre reproduções.
2. Criar condição de reprodução por energia e idade.
3. Transferir energia para o filhote e posicioná-lo próximo ao progenitor.
4. Criar identificadores únicos e registrar nascimentos/mortes.
5. Garantir que nascimentos/mortes não alterem a lista durante iteração.
6. Testar casos em que não há energia ou idade suficiente.

**Pronto quando:** surgem novos indivíduos espontaneamente, sem reprodução infinita no mesmo instante; população pode aumentar ou diminuir.

**Demonstração:** gravação de uma população crescendo e depois oscilando. **Commit:** `feat: implementar reproducao e ciclo de vida`.

### Sprint 4 — Evolução genética: primeiro MVP (6 a 8 horas)

**Objetivo:** implementar herança e mutação entre gerações.

**Tarefas:**
1. Agrupar `speed`, `vision` e `efficiency` em uma estrutura de genes.
2. Fazer descendentes herdarem os genes do progenitor.
3. Aplicar probabilidade de mutação por gene e limitar os valores.
4. Adicionar geração do indivíduo e rastrear relação com progenitor via `parent_id` opcional.
5. Garantir que o custo de energia de velocidade/visão afete a sobrevivência.
6. Testar herança sem mutação, limites com mutação e incremento de geração.

**Pronto quando:** existem ao menos duas gerações em um cenário preparado, com genes herdados e eventuais mutações; parâmetros são configuráveis.

**Demonstração:** inspecionar genes de progenitor e filhote. **Marco:** **MVP EvoLife 0.1**. **Commit:** `feat: adicionar heranca genetica e mutacoes`.

### Sprint 5 — Observabilidade: dados e história da população (4 a 6 horas)

**Objetivo:** tornar mudanças evolutivas mensuráveis.

**Tarefas:**
1. Criar contadores de população, nascimentos, mortes e geração máxima.
2. Calcular médias dos genes nas criaturas vivas.
3. Exibir indicadores simples na tela.
4. Amostrar métricas a cada 5 segundos simulados.
5. Exportar CSV por execução e criar teste de cabeçalho e linhas.
6. Realizar dois experimentos com sementes diferentes e anotar observações.

**Pronto quando:** usuário lê indicadores sem acessar o código; CSV é aberto em planilha ou pandas; extinção não causa divisão por zero.

**Demonstração:** mostrar HUD e gráfico feito a partir do CSV. **Commit:** `feat: adicionar metricas e exportacao csv`.

### Sprint 6 — Laboratório: controles e repetibilidade (3 a 5 horas)

**Objetivo:** transformar a simulação em ferramenta de experimentos.

**Tarefas:**
1. Implementar pausa/continuação, reinício e passo único.
2. Criar ajuda simples com atalhos.
3. Tornar semente, quantidade de alimento e taxa de reposição configuráveis.
4. Garantir separação entre renderização e tempo de simulação.
5. Adicionar teste de repetibilidade com semente e sequência fixa de passos.
6. Documentar um protocolo: hipótese → parâmetro → semente → resultado.

**Pronto quando:** duas execuções com mesma configuração/seed produzem mesma evolução do estado em testes; a pausa interrompe o tempo lógico.

**Demonstração:** repetir um experimento e obter os mesmos indicadores. **Commit:** `feat: adicionar controles e execucoes reproduziveis`.

### Sprint 7 — Qualidade, documentação e lançamento (5 a 8 horas)

**Objetivo:** fechar um projeto apresentável, não apenas um experimento local.

**Tarefas:**
1. Revisar tratamento de extinção, limites do mundo e valores de energia/genes.
2. Executar testes automatizados; corrigir erros e remover código morto.
3. Executar teste de estabilidade de 15 minutos e registrar observações.
4. Atualizar README: requisitos, instalação, comandos, regras, limitações e exemplos.
5. Gravar GIF ou vídeo curto; adicionar screenshots e resultados de 1 experimento.
6. Criar release/tag `v1.0.0` no GitHub e registrar ideias futuras em `BACKLOG.md`.

**Pronto quando:** qualquer visitante com Python consegue executar pelo README; testes passam e há uma demonstração do ciclo de vida e evolução.

**Demonstração:** release público e vídeo de 30–60 segundos. **Commit:** `docs: preparar release 1.0 do EvoLife`.

### Sprint 8 — Extensão opcional: predadores e ambiente (5 a 9 horas)

**Só iniciar após concluir a versão 1.0.** Criar predadores, fuga, estações ou regiões do mapa com diferentes recursos. Manter experimentos isolados, comparar com o comportamento da versão 1.0 e medir o custo de desempenho.

### Sprint 9 — Extensão opcional: cérebro artificial (8 a 15+ horas)

**Só iniciar após a versão 1.0 e a definição de uma hipótese.** Trocar a regra de busca fixa por uma pequena rede neural ou política aprendida. Definir entradas (distância/direção do alimento, energia), saídas (virar, acelerar), método de treino e comparativo com a estratégia original. Evitar prometer consciência ou inteligência geral: trata-se de um controlador experimental.

### 10.1 Quadro compacto de acompanhamento

| Sprint | Entrega | Esforço estimado | Portão de conclusão |
| --- | --- | --- | --- |
| 0 | Estrutura e janela | 2–3 h | Abre e fecha sem erro |
| 1 | Criaturas se movendo | 4–6 h | Movimento e bordas testados |
| 2 | Comida e energia | 6–8 h | Comer, morrer e repor alimento |
| 3 | Reprodução | 5–7 h | Filhotes nascem com regras válidas |
| 4 | **MVP: evolução** | 6–8 h | Herança, mutações e gerações |
| 5 | Métricas e CSV | 4–6 h | HUD e dados exportáveis |
| 6 | Controles e sementes | 3–5 h | Experimento repetível |
| 7 | **Release 1.0** | 5–8 h | Testes, README e demonstração |
| 8+ | Predadores / redes neurais | Opcional | Não bloquear o lançamento |

## 11. Backlog e gestão do trabalho

**Colunas recomendadas no Notion ou GitHub Projects:** Ideias → Próxima sprint → Em andamento → Em teste → Concluído. Limitar **Em andamento a uma tarefa**. Nunca adicionar uma nova funcionalidade direto em andamento: primeiro registrar a ideia no backlog.

**Modelo de cartão de tarefa:**

```text
Título: [S1] Implementar atualização de posição
Objetivo: criatura se mover com base em dt
Entrada: posição, direção, velocidade, dt
Saída: nova posição
Critério: dt=1 e speed=40 deslocam 40 pixels na direção definida
Dependências: classe Creature
Evidência: teste e GIF
Status: A fazer
```

**Definição de pronto para qualquer tarefa:** código executa, comportamento esperado foi verificado, não quebra funcionalidades anteriores, há commit com mensagem clara e uma frase descrevendo o que foi aprendido. Não é necessário refatorar o projeto inteiro a cada sprint.

### 11.1 Git e colaboração futura

- Branch principal `main` sempre executável; branches pequenas `feature/movement`, `feature/food` se ajudarem na organização.
- Uma mudança de comportamento por commit sempre que viável.
- Issues com rótulos `sprint-1`, `bug`, `experiment` e `documentation`.
- Uma captura de tela/GIF a cada sprint para manter histórico visual do avanço.

## 12. Estratégia de testes

| Cenário | Dado | Quando | Então |
| --- | --- | --- | --- |
| Movimento | posição (100,100), velocidade 40 e direção leste | `update(1.0)` | `x` aumenta 40, `y` não muda, sem borda. |
| Bordas | criatura junto à borda direita | tenta avançar para fora | posição final permanece válida. |
| Energia | energia 100, parâmetros fixos | passa 1 segundo simulado | energia diminui conforme a fórmula documentada. |
| Alimentação | criatura em contato com 1 alimento | mundo avança | alimento some e energia aumenta até o teto. |
| Morte | energia próxima de zero | energia chega a zero | criatura é removida e morte contabilizada uma vez. |
| Reprodução bloqueada | idade 2 s ou energia 50 | tenta reproduzir | nenhum descendente é criado. |
| Reprodução válida | idade 20 s, energia 120, cooldown zerado | reproduz | filhote tem 45 energia; progenitor perde 45. |
| Mutação | genes perto dos limites | mutação sorteada | valores permanecem nos intervalos definidos. |
| Herança | chance de mutação configurada para 0 | cria filhote | genes do filhote coincidem com os do progenitor. |
| Determinismo | mesma seed e mesma sequência de `dt` fixo | roda duas simulações | estados e contadores coincidem. |
| Extinção | zero criaturas vivas | coleta métricas e desenha | nenhum erro ou divisão por zero. |

**Testes automáticos:** preferir `pytest` para regras puras. **Testes manuais:** verificar legibilidade, fluidez, atalhos, consumo de recursos e gravação de CSV. Registrar eventuais desvios e fazer a correção na mesma sprint ou abrir issue de bug.

## 13. Riscos, decisões e mitigação

| Risco | Impacto | Mitigação |
| --- | --- | --- |
| Escopo crescer até virar um MMORPG/VR | Não terminar a versão básica | Travar o escopo 1.0; ideias vão para backlog. |
| Começar por IA ou rede neural | Atrasar a primeira entrega visível | Movimento e sobrevivência usam regras simples antes de ML. |
| Parâmetros levam a extinção rápida | Pouco tempo para observar evolução | Criar cenário de demonstração com alimento abundante; registrar ajustes. |
| Crescimento populacional sem limites | Queda de FPS e memória | Medir população, estabelecer limite de segurança configurável se necessário. |
| Confundir movimento dirigido com aprendizagem | Conclusões incorretas | Documentar regras, hereditariedade e aprendizado separadamente. |
| Resultados variarem de execução para execução | Difícil comparar experimentos | Usar seed, tempo fixo e registro de parâmetros. |
| Perder motivação em refatorações | Abandono | Uma entrega visual por sprint e tarefas com menos de 2 horas, quando possível. |
| Dependências/instalação em máquinas diferentes | Dificuldade de execução | Ambiente virtual, requirements e README verificado do zero. |

## 14. Protocolo mínimo para experimentos evolutivos

**Pergunta:** mais alimento favorece velocidade ou visão?  
**Hipótese:** em uma condição específica, maior velocidade poderá aumentar encontros com comida, mas seu custo energético pode reduzir a vantagem.  
**Variável alterada:** taxa de reposição de alimento (ex.: 1,0 vs. 0,4 unidade/segundo).  
**Constantes:** população inicial, espaço, parâmetros de mutação, duração e conjunto de sementes.  
**Execução:** usar várias sementes por condição quando houver tempo; registrar 5 a 10 minutos simulados por execução.  
**Medições:** população, mortes, nascimentos, velocidade média e visão média ao longo do tempo.  
**Interpretação:** comparar curvas e variabilidade; não concluir causalidade de um único episódio.  
**Registro:** salvar CSV com nome da condição e anotar os parâmetros no README ou caderno de experimentos.

## 15. Dependências, instalação e ambiente

**Pré-requisitos:** Python 3 instalado e `venv` disponível. Recomenda-se rodar no Ubuntu com ambiente virtual. Os comandos abaixo são o caminho planejado; serão verificados na Sprint 0.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pygame pytest
python main.py
```

Após validar versões no computador de desenvolvimento, registrar dependências no `requirements.txt`. Evitar dependências extras sem justificativa. CSV será implementado com `csv` da biblioteca padrão; análises externas podem usar pandas opcionalmente, mas não deve ser obrigatório para executar o jogo.

## 16. Decisões de produto e critérios de mudança

**Decisões tomadas:** desktop 2D, Pygame, regras simples, reprodução assexuada, genes velocidade/visão/eficiência, primeiro MVP na Sprint 4, sem backend ou 3D antes da versão 1.0.

**Decisões em aberto, sem bloquear o início:** calibrar fome e disponibilidade de comida, limite máximo de população, visualização de genes por indivíduo, preferência de paleta visual e onde armazenar capturas dos experimentos. Resolver somente quando chegarem à sprint correspondente.

**Mudança de escopo:** propor a funcionalidade, explicar benefício, esforço estimado e impacto na sprint. Se não for necessária para seu critério de conclusão, registrar como ideia futura.

## 17. Primeira sessão de trabalho — próxima ação concreta

Começar a **Sprint 0**, com a meta de abrir uma janela Pygame. Quando isso estiver funcionando, iniciar a **Sprint 1** criando **uma única `Creature`** com cinco atributos (`x`, `y`, `direction`, `speed`, `energy`) e um método `update(dt)` que atualiza posição sem sair da tela. Só depois gerar as outras nove criaturas.

**Checklist de hoje:**

- [ ] Criar pasta `EvoLife` e repositório Git.
- [ ] Criar ambiente virtual e instalar Pygame.
- [ ] Abrir e fechar uma janela 800 × 600 sem erros.
- [ ] Fazer o primeiro commit.
- [ ] Registrar a próxima tarefa: implementar `Creature`.

**Pergunta técnica inicial para orientar a implementação:** se a posição inicial é `(100, 100)`, a velocidade é `40 pixels/segundo` e a criatura aponta para a direita, qual deve ser a posição após `0,5 segundo`? **Resposta esperada: `(120, 100)`**. Esse exemplo será o primeiro teste do movimento por tempo decorrido.

---

**Regra de ouro do EvoLife:** primeiro fazer nascer; depois fazer sobreviver; então fazer reproduzir; só depois medir evolução e experimentar IA.
