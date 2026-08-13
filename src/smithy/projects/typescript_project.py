from pathlib import Path

from smithy.base_project import BaseProject
from smithy.command import Command
from smithy.enums import ProjectType

INDEX_TS = """\
const greeting: string = "Hello, World!";

console.log(greeting);
"""

TSCONFIG_JSON = """\
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "node16",
    "moduleResolution": "node16",
    "rootDir": "src",
    "outDir": "dist",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true
  },
  "include": ["src"]
}
"""


class TypeScriptProject(BaseProject):
    project_type = ProjectType.TYPESCRIPT
    icon = "🌐"
    install_commands = (Command("sudo dnf install -y nodejs npm"),)

    def create(self, path: Path, name: str) -> None:
        root = path / name
        root.mkdir(parents=True)
        self._write_sources(root)
        Command("npm init -y").run(cwd=root)
        Command("npm install --save-dev typescript @types/node").run(cwd=root)

    def _write_sources(self, root: Path) -> None:
        source_dir = root / "src"
        source_dir.mkdir()
        (source_dir / "index.ts").write_text(INDEX_TS)
        (root / "tsconfig.json").write_text(TSCONFIG_JSON)
