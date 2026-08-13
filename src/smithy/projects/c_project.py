from pathlib import Path

from smithy.base_project import BaseProject
from smithy.command import Command
from smithy.enums import ProjectType

CMAKELISTS = """\
cmake_minimum_required(VERSION 3.20)
project({name} LANGUAGES C)

set(CMAKE_C_STANDARD 17)
set(CMAKE_C_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

add_executable({name} src/main.c)
"""

MAIN_C = """\
#include <stdio.h>

int main(void) {
    printf("Hello, World!\\n");
    return 0;
}
"""

CLANG_FORMAT = """\
BasedOnStyle: LLVM
IndentWidth: 4
ColumnLimit: 100
"""

CLANGD = """\
CompileFlags:
  CompilationDatabase: build
"""


class CProject(BaseProject):
    project_type = ProjectType.C
    icon = "⚙️"
    install_commands = (
        Command("sudo dnf install -y gcc clang clang-tools-extra cmake make"),
    )

    def create(self, path: Path, name: str) -> None:
        root = path / name
        root.mkdir(parents=True)
        self._write_sources(root)
        self._write_tooling(root, name)

    def _write_sources(self, root: Path) -> None:
        source_dir = root / "src"
        source_dir.mkdir()
        (source_dir / "main.c").write_text(MAIN_C)

    def _write_tooling(self, root: Path, name: str) -> None:
        (root / "CMakeLists.txt").write_text(CMAKELISTS.format(name=name))
        (root / ".clang-format").write_text(CLANG_FORMAT)
        (root / ".clangd").write_text(CLANGD)
