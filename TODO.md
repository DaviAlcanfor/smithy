# TODO

## Menu interativo com `questionary`

Rodar `smithy` sem argumento nenhum abre um menu de seleção com as setinhas, em vez de
imprimir o help do argparse. Escolhe o tipo, pergunta o nome, cria.

```
? Que tipo de projeto? (setas para navegar)
❯ 🐍 python
  🦀 rust
  🐹 go
```

Como fazer: em `cli.py`, quando `argv` estiver vazio, chamar um `interactive.py` novo
que monta as opções a partir de `PROJECTS` e `PROJECT_ICONS` e devolve o mesmo
`(project_type, name)` que o comando `new` já usa. O resto do fluxo não muda.

Pontos a resolver antes:

- **Custa a primeira dependência do projeto.** `questionary` traz `prompt_toolkit` (e
  `wcwidth`) junto. Hoje `dependencies = []`, e o README tem um badge dizendo isso —
  os dois precisam mudar. É o real preço da funcionalidade; o resto é barato.
- **Sem TTY** (pipe, CI, `smithy | cat`) o `questionary` não funciona. Nesse caso cair
  no help do argparse, como hoje.
- Manter `smithy new python foo` funcionando igual. O menu é atalho, não substituição.

## Adiado

- Publicar o projeto criado no GitHub. Explicitamente deixado para uma versão futura.
- Não há testes automatizados. A verificação até agora foi manual.

## Decisões tomadas sem spec

A spec original foi cortada em `## registry.py`. Estes pontos foram decididos por
conta própria e são os primeiros candidatos a revisão:

- **CLI: argparse.** Escolhido por ser stdlib e manter o projeto sem dependências.
- **`registry.py` é só o dict `PROJECTS`**, mapeando `ProjectType` para instâncias de
  `BaseProject`. A spec dizia apenas "Dict".
- **`config.py`** define só `projects_dir`, lido de `SMITHY_PROJECTS_DIR` com padrão
  `~/Projects`. Não há arquivo de configuração.
- **Comandos da CLI:** `new`, `install`, `list`.
- **`scripts/install.sh`** instala o Smithy via `uv tool install`.
- O dict de ícones se chama `PROJECT_ICONS`.
- `projects/` não tem `__init__.py`, seguindo a estrutura dada. Verificado: funciona
  como namespace package, inclusive instalado via wheel.

## Pendências das linguagens

- `java` e `php` nunca foram executados de ponta a ponta — a máquina de
  desenvolvimento não tem `javac`, `mvn`, `php` nem `composer`. Só houve validação
  estática (XML e JSON bem formados).
- `astro` depende dos flags do `create-astro` (`--template`, `--yes`, `--skip-houston`),
  que mudam entre versões. Se quebrar, é aqui.
- `java` gera `Main.java` no pacote default, para não ter que converter o nome do
  projeto em nome de pacote válido.
- C e C++ têm `.clang-format` e `.clangd` idênticos, duplicados nos dois arquivos.
  Cada projeto ser autocontido pareceu melhor que um módulo compartilhado, mas é
  discutível.
