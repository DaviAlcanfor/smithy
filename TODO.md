# TODO

## Decisões tomadas sem spec

A spec original foi cortada em `## registry.py`. Estes pontos foram decididos por
conta própria e são os primeiros candidatos a revisão:

- **CLI: argparse.** Escolhido por ser stdlib e manter o projeto sem dependências.
  Trocar por click/typer mexe só em `cli.py` e em `pyproject.toml`.
- **`registry.py` é só o dict `PROJECTS`**, mapeando `ProjectType` para instâncias de
  `BaseProject`. A spec dizia apenas "Dict".
- **`config.py`** define só `projects_dir`, lido de `SMITHY_PROJECTS_DIR` com padrão
  `~/Projects`. Não há arquivo de configuração.
- **Comandos da CLI:** `new`, `install`, `list`. `new` e `install` só aceitam tipos
  implementados; `list` mostra os 10.
- **`scripts/install.sh`** instala o Smithy via `uv tool install`.
- O dict de ícones se chama `PROJECT_ICONS`.
- `projects/` não tem `__init__.py`, seguindo a estrutura dada. Verificado: funciona
  como namespace package, inclusive instalado via wheel.

## Tipos de projeto sem classe

Presentes em `ProjectType` e `PROJECT_ICONS`, sem subclasse de `BaseProject`:

`go`, `java`, `c`, `javascript`, `typescript`, `astro`, `php`

Cada um precisa de `install_commands` (dnf) e `create()` — tool-driven ou file-driven,
ver AGENTS.md. Fora do MVP de propósito; implementar só quando pedido.

## Adiado

- Publicar o projeto criado no GitHub. Explicitamente deixado para uma versão futura.
- Não há testes automatizados. A verificação até agora foi manual.
