from pathlib import Path

from smithy.base_project import BaseProject
from smithy.command import Command
from smithy.enums import ProjectType


class AstroProject(BaseProject):
    project_type = ProjectType.ASTRO
    icon = "🚀"
    install_commands = (Command("sudo dnf install -y nodejs npm"),)

    def create(self, path: Path, name: str) -> None:
        target = path / name
        Command(
            f"npm create astro@latest {target} -- "
            "--template minimal --install --no-git --skip-houston --yes"
        ).run()
