# AGENTS.md

Smithy is a Python CLI that scaffolds new projects and installs the toolchain each
one needs. Target platform is Fedora — package installs go through `dnf`.

## Layout

- `src` layout. The package is `smithy`; always import absolutely (`from smithy.command import Command`).
- One project class per file under `src/smithy/projects/`, named `<lang>_project.py`.
- `projects/` has no `__init__.py` by design — it is a namespace package.

## Command discipline

This is the rule the codebase is built around. Do not relax it.

- A `Command` is **exactly one process**. Never `shell=True`, never `bash -c`, never
  `&&`, `|`, `>` or `;` inside the command string.
- A multi-step operation is multiple `Command` objects, not one clever string.
- The string is parsed with `shlex.split()`. An empty result raises `ValueError("Comando vazio")`.
- `run()` prints the command (via `shlex.join`) before executing, then calls
  `subprocess.run(self.args, cwd=cwd, check=True)`. Failures propagate — do not swallow them.

## Adding a project type

1. Add the member to `ProjectType` in `enums.py`.
2. Add the emoji to `PROJECT_ICONS` in `icons.py`.
3. Create `projects/<lang>_project.py` with a `BaseProject` subclass defining
   `project_type`, `icon`, `install_commands` and `create()`.
4. Register the class in `registry.py`.

`create()` comes in three shapes; pick the one that fits the language:

- **Tool-driven** — a single `Command` does the whole job. See `RustProject`
  (`cargo new`), `PythonProject` (`uv init --lib`) and `AstroProject`.
- **File-driven** — no such tool exists, so `create()` makes the directory and writes
  the files itself. See `CppProject`, `CProject` and `JavaProject`.
- **Hybrid** — `create()` writes the sources, then runs a tool that only works from
  inside the project directory, via `Command.run(cwd=root)`. See `GoProject`
  (`go mod init`), the Node projects (`npm init -y`) and `PhpProject`.

Keep file contents as module-level template constants, and split the writing into
small helpers rather than letting `create()` grow into one long method.

## Code style

- Type hints on every signature, including `-> None`.
- Small functions with a single responsibility. `CppProject._write_sources` /
  `_write_tooling` is the reference for how to break up a `create()` that grows.
- No redundant comments and no dead code. Add a docstring only when the name alone
  does not carry the meaning.

## Scope

All ten `ProjectType` members have a class behind them. `PROJECT_ICONS` and `PROJECTS`
are expected to hold the same keys — `smithy list` still marks a type as "ainda não
implementado" if a class is missing, which is what you will see mid-way through adding
a language.

Publishing a created project to GitHub is out of scope for this version. Do not
implement it without being asked.
