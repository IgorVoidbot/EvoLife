# Plano de sprints

Fonte: `EvoLife_PRD_Roadmap.md`, versão 1.0. O documento original permanece
inalterado. A cadência sugerida é semanal; os critérios de aceite orientam
a conclusão, sem impor datas. Somente a Sprint 0 está autorizada nesta sessão.

| Sprint | Esforço do PRD | Entrega / portão de aceite | Status |
| --- | --- | --- | --- |
| 0 | 2–3 h | Repositório, venv, dependências, README; janela 800 × 600 abre, redesenha e fecha | Entrega técnica concluída; commit suspenso |
| 1 | 4–6 h | 10 criaturas se movem por tempo decorrido; bordas verificadas | Não iniciada; aguarda autorização |
| 2 | 6–8 h | Comida, busca, consumo, energia, morte e reposição | Não iniciada |
| 3 | 5–7 h | Idade, cooldown, reprodução e transferência de energia | Não iniciada |
| 4 | 6–8 h | Genes herdáveis, mutação limitada e gerações; MVP 0.1 | Não iniciada |
| 5 | 4–6 h | Indicadores, médias, amostras e exportação CSV | Não iniciada |
| 6 | 3–5 h | Pausa, reinício, passo único e repetibilidade por semente | Não iniciada |
| 7 | 5–8 h | Testes, estabilidade por 15 minutos, mídia e release 1.0 | Não iniciada |
| 8 | 5–9 h | Predadores e ambientes, após a versão 1.0 | Backlog opcional |
| 9 | 8–15+ h | Controlador neural com hipótese e comparação, após 1.0 | Backlog opcional |

## Sprint 0 — contrato desta sessão

- Reutilizar o Git existente, sem reinicializar ou fazer commits.
- Preservar Python 3.14 e `.venv`; instalar pygame-ce 2.5.8 e pytest apenas
  como pacotes pré-compilados, sem instalar componentes no sistema operacional.
- Entregar janela preta de 800 × 600, loop responsivo e saída com Esc/fechar.
- Criar README e .gitignore, instruções para ambos os CLIs e documentação.
- Registrar testes e dificuldades na memória e atualizar o quadro de tarefas.

A tarefa `chore: iniciar projeto EvoLife` do PRD fica suspensa até autorização
explícita. O commit não é um pré-requisito para verificar o código nesta sessão.
A demonstração prevista no PRD é um vídeo de 5 segundos; sua produção e a
avaliação visual devem aparecer separadas dos resultados automatizados.

**Evidências desta entrega:** sete testes aprovados com SDL dummy, verificação
automatizada com janela real X11 (374 quadros em 6,29 s e encerramento sem erro)
e [vídeo de 5 segundos](media/sprint0.mp4). Não houve avaliação manual por uma
pessoa; os resultados e limites estão registrados na memória compartilhada.

## Próximo portão

Somente após autorização para a Sprint 1, começar com uma `Creature`, movimento
por `dt` e teste de `(100, 100)` para `(120, 100)` em 0,5 s a 40 pixels/s.
Depois tratar bordas e gerar as outras nove criaturas. Não iniciar agora.
