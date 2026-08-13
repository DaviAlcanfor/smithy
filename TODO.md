# TODO

## Adiado

- Publicar o projeto criado no GitHub. Explicitamente deixado para uma versão futura.
  Ideia: flag `--github [nome]` no `new` — cria o repo e já linka com a pasta do
  projeto. Via `gh repo create <nome> --source=. --private --push`, que faz repo,
  remote e push numa chamada só (requer `gh` instalado e autenticado; sem ele, avisar
  e seguir com o projeto local). Nome padrão = nome do projeto.
- Não há testes automatizados. A verificação até agora foi manual.

## Decisões tomadas sem spec

A spec original foi cortada em `## registry.py`. Estes pontos foram decididos por
conta própria e são os primeiros candidatos a revisão:

- **CLI: argparse**, com `questionary` só para o menu interativo. O projeto deixou de
  ter zero dependências quando o menu entrou.
- **`registry.py` é só o dict `PROJECTS`**, mapeando `ProjectType` para instâncias de
  `BaseProject`. A spec dizia apenas "Dict".
- **`config.py`** define só `projects_dir`, lido de `SMITHY_PROJECTS_DIR` com padrão
  `~/Projects`. Não há arquivo de configuração.
- **Comandos da CLI:** `new`, `install`, `list`. Sem argumentos abre o menu; sem TTY
  cai no help do argparse com exit 1.
- **O menu só cria projetos**, não instala toolchain — `install` continua explícito.
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
