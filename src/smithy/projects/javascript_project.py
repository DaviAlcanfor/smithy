from pathlib import Path

from smithy.base_project import BaseProject
from smithy.command import Command
from smithy.enums import ProjectType

INDEX_JS = """\
console.log("Hello, World!");
"""


class JavaScriptProject(BaseProject):
    project_type = ProjectType.JAVASCRIPT
    icon = "📜"
    install_commands = (Command("sudo dnf install -y nodejs npm"),)

    def create(self, path: Path, name: str) -> None:
        root = path / name
        root.mkdir(parents=True)
        (root / "index.js").write_text(INDEX_JS)
        Command("npm init -y").run(cwd=root)
