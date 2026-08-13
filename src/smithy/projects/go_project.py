from pathlib import Path

from smithy.base_project import BaseProject
from smithy.command import Command
from smithy.enums import ProjectType

MAIN_GO = """\
package main

import "fmt"

func main() {
\tfmt.Println("Hello, World!")
}
"""


class GoProject(BaseProject):
    project_type = ProjectType.GO
    icon = "🐹"
    install_commands = (Command("sudo dnf install -y golang"),)

    def create(self, path: Path, name: str) -> None:
        root = path / name
        root.mkdir(parents=True)
        (root / "main.go").write_text(MAIN_GO)
        Command(f"go mod init {name}").run(cwd=root)
