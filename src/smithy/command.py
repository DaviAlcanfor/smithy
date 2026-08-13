import shlex
import subprocess
from pathlib import Path


class Command:
    """A single process invocation, never routed through a shell."""

    def __init__(self, command: str) -> None:
        args = shlex.split(command)
        if not args:
            raise ValueError("Comando vazio")
        self.args: list[str] = args

    def __str__(self) -> str:
        return shlex.join(self.args)

    def __repr__(self) -> str:
        return f"Command({str(self)!r})"

    def run(self, cwd: Path | None = None) -> None:
        print(self)
        subprocess.run(self.args, cwd=cwd, check=True)
