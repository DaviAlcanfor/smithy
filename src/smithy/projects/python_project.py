from pathlib import Path

from smithy.base_project import BaseProject
from smithy.command import Command
from smithy.enums import ProjectType


class PythonProject(BaseProject):
    project_type = ProjectType.PYTHON
    icon = "🐍"
    install_commands = (Command("sudo dnf install -y uv"),)

    def create(self, path: Path, name: str) -> None:
        Command(f"uv init --lib {path / name}").run()
