import os
from dataclasses import dataclass
from pathlib import Path

PROJECTS_DIR_ENV = "SMITHY_PROJECTS_DIR"
DEFAULT_PROJECTS_DIR = Path.home() / "Projects"


@dataclass(frozen=True)
class Config:
    projects_dir: Path = DEFAULT_PROJECTS_DIR

    @classmethod
    def from_env(cls) -> "Config":
        raw = os.environ.get(PROJECTS_DIR_ENV)
        if not raw:
            return cls()
        return cls(projects_dir=Path(raw).expanduser())
