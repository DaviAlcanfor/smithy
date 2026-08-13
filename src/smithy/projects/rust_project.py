from pathlib import Path

from smithy.base_project import BaseProject
from smithy.command import Command
from smithy.enums import ProjectType


class RustProject(BaseProject):
    project_type = ProjectType.RUST
    icon = "🦀"
    install_commands = (Command("sudo dnf install -y rust cargo"),)

    def create(self, path: Path, name: str) -> None:
        Command(f"cargo new {path / name}").run()
