# Instruções de trabalho — EvoLife

Este arquivo é o ponto de entrada comum para Codex CLI e OpenCode CLI.
As instruções usam arquivos Markdown e comandos Python comuns; não dependem
de plugins, configurações privadas ou memória exclusiva de um CLI.

## Antes de trabalhar

1. Leia este arquivo e `docs/PROJECT_STATE.md` em cada nova sessão.
2. Consulte `docs/TASKS.md`, `docs/SPRINTS.md` e `docs/ARCHITECTURE.md`.
3. Leia as seções pertinentes de `EvoLife_PRD_Roadmap.md`, a especificação
   original, e confira `git status --short` antes de editar.
4. Confirme o escopo autorizado e as pendências da sessão anterior.

## Limites vigentes

- Trabalhe somente na Sprint 0. A Sprint 1 depende de autorização explícita
  do usuário, mesmo depois de a Sprint 0 estar pronta.
- Preserve arquivos existentes e mudanças do usuário. Nunca altere o PRD.
- Não faça commits, tags, pushes ou publicação sem autorização explícita.
  A tarefa de commit do PRD fica suspensa por determinação do usuário.
- Preserve o Python global 3.14 e o `.venv` existente. Não use sudo, não
  instale bibliotecas no sistema operacional e não altere permissões.
- Use `pygame-ce==2.5.8`, que fornece `import pygame`; não instale também
  a distribuição `pygame`. `pytest` é dependência de desenvolvimento.
- Instale dependências apenas como pacotes pré-compilados, usando
  `--only-binary=:all:`. Diante de erro, apresente a mensagem completa e
  registre a dificuldade antes de tentar outras alterações no ambiente.
- Informe bloqueios antes de solicitar ampliação de permissões. Não use
  soluções alternativas para contornar uma negativa.
- Não crie agentes auxiliares sem solicitação explícita do usuário.

## Memória compartilhada

`docs/PROJECT_STATE.md` é a fonte comum de continuidade entre agentes e CLIs.
Mantenha nele a sprint autorizada, implementação atual, ambiente validado,
decisões e motivos, comandos e resultados de testes, dificuldades, pendências
e próxima ação. Não registre segredos ou informações pessoais.

Ao concluir uma tarefa, atualize seu status em `docs/TASKS.md`. Antes de
encerrar a sessão, atualize `docs/PROJECT_STATE.md`; não declare um teste
aprovado sem executá-lo. Diferencie teste automatizado sem tela, verificação
com driver gráfico e inspeção manual pelo usuário. Não dependa do histórico
da conversa para transmitir restrições ao próximo agente.

Se o usuário autorizar trabalho simultâneo, combine a propriedade dos arquivos
antes de editar e escolha um responsável pela consolidação da memória. Releia
o estado antes de escrever para preservar os registros de outras sessões.

## Código e validação

- Prefira Python, Pygame e biblioteca padrão; explique novas dependências.
- Centralize as configurações atuais em `evolife/config.py`.
- Mantenha funções pequenas, nomes claros e importação sem efeitos colaterais.
- Nas próximas sprints autorizadas, mantenha domínio independente do Pygame,
  tempo lógico fixo de 1/60 s e gerador aleatório próprio do mundo.
- Crie apenas componentes necessários à sprint vigente. Não crie classes de
  criaturas, mundo, alimentos, genética ou métricas antecipadamente.
- Valide o comportamento afetado com testes úteis e registre seus limites.
- Documente em português; use nomes de código em inglês.

## Comandos (na raiz, após ativar o `.venv`)

```bash
python -m pip install --only-binary=:all: --no-cache-dir -r requirements-dev.txt
python -c "import pygame; print(pygame.version.ver)"
python main.py
python -m pytest -q
python -m pip check
```

No Linux, ative com `source .venv/bin/activate`; no PowerShell,
com `.venv\Scripts\Activate.ps1`. Os testes configuram SDL `dummy` sem
abrir uma janela no desktop. A avaliação visual usa `python main.py`.
