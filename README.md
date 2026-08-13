<div align="center">

# 🔨 Smithy

**Forje projetos novos com as ferramentas já prontas.**

Uma CLI que cria a estrutura do projeto *e* instala o toolchain que ele precisa —
num comando só, sem template engine, sem dependência nenhuma.

![Python](https://img.shields.io/badge/python-3.11%2B-3776AB?logo=python&logoColor=white)
![Fedora](https://img.shields.io/badge/fedora-dnf-51A2DA?logo=fedora&logoColor=white)
![Dependências](https://img.shields.io/badge/dependências-zero-2ea44f)
![Status](https://img.shields.io/badge/status-MVP-orange)

</div>

---

## O que é

Começar um projeto novo é sempre o mesmo ritual: lembrar o comando do `cargo`, achar
qual pacote do `dnf` traz o `clangd`, escrever o `CMakeLists.txt` do zero de novo.
O Smithy encapsula esse ritual por linguagem.

Cada tipo de projeto sabe duas coisas: **como se instalar** (`smithy install`) e **como
se criar** (`smithy new`). Adicionar uma linguagem nova é escrever uma classe com essas
duas respostas.

## Instalação

```sh
git clone https://github.com/DaviAlcanfor/smithy.git
cd smithy
./scripts/install.sh
```

O script usa `uv tool install`, então o binário `smithy` fica disponível no PATH sem
mexer no Python do sistema. Requer Python 3.11+.

## Uso

| Comando | O que faz |
| --- | --- |
| `smithy list` | Lista os tipos de projeto e quais já estão implementados |
| `smithy install <tipo>` | Instala o toolchain do tipo via `dnf` |
| `smithy new <tipo> <nome>` | Cria o projeto |
| `smithy new <tipo> <nome> -p <dir>` | Cria em um diretório específico |

```sh
$ smithy install cpp
⚙️ instalando ferramentas de cpp
sudo dnf install -y gcc-c++ clang clang-tools-extra cmake make

$ smithy new cpp calculadora
⚙️ criando calculadora em /home/voce/Projects
```

Sem `-p`, o projeto vai para `$SMITHY_PROJECTS_DIR` — padrão `~/Projects`.

## Tipos suportados

| | Tipo | Como é criado | Toolchain (`dnf`) |
| :-: | --- | --- | --- |
| 🐍 | `python` | `uv init --lib` | `uv` |
| 🦀 | `rust` | `cargo new` | `rust`, `cargo` |
| 🐹 | `go` | `main.go` + `go mod init` | `golang` |
| ☕ | `java` | `pom.xml` + `src/main/java/Main.java` | `java-latest-openjdk-devel`, `maven` |
| ⚙️ | `c` | CMake + clangd, arquivos gerados | `gcc`, `clang`, `clang-tools-extra`, `cmake`, `make` |
| ⚙️ | `cpp` | CMake + clangd, arquivos gerados | `gcc-c++`, `clang`, `clang-tools-extra`, `cmake`, `make` |
| 📜 | `javascript` | `index.js` + `npm init -y` | `nodejs`, `npm` |
| 🌐 | `typescript` | `tsconfig.json` + `npm install -D typescript` | `nodejs`, `npm` |
| 🚀 | `astro` | `npm create astro@latest` (template minimal) | `nodejs`, `npm` |
| 🐘 | `php` | `composer.json` PSR-4 + `composer install` | `php`, `php-cli`, `composer` |

Projetos C e C++ nascem prontos para o editor: `CMakeLists.txt` com
`compile_commands.json` habilitado, `.clang-format` e um `.clangd` já apontando para
`build/`.

## Como funciona

O núcleo é a classe `Command`, e ela tem uma regra rígida: **um `Command` é exatamente
um processo**. Nada de `shell=True`, `bash -c` ou `&&` escondido numa string. A string
passa por `shlex.split()` e vai direto para o `subprocess.run(..., check=True)`; toda
operação de vários passos é uma sequência de `Command`, não uma string esperta.

Cada linguagem é uma subclasse de `BaseProject` que declara `install_commands` e
implementa `create()`, em uma de duas formas:

- **Tool-driven** — a própria linguagem já tem um scaffolder, e `create()` é um
  `Command` só (`cargo new`, `uv init`).
- **File-driven** — não existe esse comando, então `create()` escreve os arquivos
  (o caso do C++).

## Estrutura

```
src/smithy/
├── cli.py            # argparse: new, install, list
├── command.py        # Command — um processo, sem shell
├── base_project.py   # BaseProject (ABC)
├── registry.py       # ProjectType -> instância de projeto
├── config.py         # SMITHY_PROJECTS_DIR
├── enums.py          # ProjectType
├── icons.py          # emoji por tipo
└── projects/         # uma classe por linguagem
```

## Desenvolvimento

Convenções em [AGENTS.md](AGENTS.md) — leia antes de adicionar uma linguagem. Pendências
e decisões em aberto em [TODO.md](TODO.md).

Rodar sem instalar:

```sh
PYTHONPATH=src python3 -m smithy list
```

## Roadmap

- Menu interativo ao rodar `smithy` sem argumentos
- Publicar o projeto criado direto no GitHub
