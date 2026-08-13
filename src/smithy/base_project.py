from abc import ABC, abstractmethod
from pathlib import Path

from smithy.command import Command
from smithy.enums import ProjectType


class BaseProject(ABC):
    project_type: ProjectType
    icon: str
    install_commands: tuple[Command, ...] = ()

    @abstractmethod
    def create(self, path: Path, name: str) -> None:
        """Create the project named `name` inside the directory `path`."""
