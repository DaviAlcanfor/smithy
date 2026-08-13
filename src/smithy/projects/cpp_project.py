from pathlib import Path

from smithy.base_project import BaseProject
from smithy.command import Command
from smithy.enums import ProjectType

CMAKELISTS = """\
cmake_minimum_required(VERSION 3.20)
project({name} LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

add_executable({name} src/main.cpp)
"""

MAIN_CPP = """\
#include <iostream>

int main() {
    std::cout << "Hello, World!\\n";
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


class CppProject(BaseProject):
    project_type = ProjectType.CPP
    icon = "⚙️"
    install_commands = (
        Command("sudo dnf install -y gcc-c++ clang clang-tools-extra cmake make"),
    )

    def create(self, path: Path, name: str) -> None:
        root = path / name
        root.mkdir(parents=True)
        self._write_sources(root)
        self._write_tooling(root, name)

    def _write_sources(self, root: Path) -> None:
        source_dir = root / "src"
        source_dir.mkdir()
        (source_dir / "main.cpp").write_text(MAIN_CPP)

    def _write_tooling(self, root: Path, name: str) -> None:
        (root / "CMakeLists.txt").write_text(CMAKELISTS.format(name=name))
        (root / ".clang-format").write_text(CLANG_FORMAT)
        (root / ".clangd").write_text(CLANGD)
