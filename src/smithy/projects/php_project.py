import json
from pathlib import Path

from smithy.base_project import BaseProject
from smithy.command import Command
from smithy.enums import ProjectType

INDEX_PHP = """\
<?php

declare(strict_types=1);

require __DIR__ . '/vendor/autoload.php';

use App\\Greeter;

echo Greeter::greet() . PHP_EOL;
"""

GREETER_PHP = """\
<?php

declare(strict_types=1);

namespace App;

final class Greeter
{
    public static function greet(): string
    {
        return 'Hello, World!';
    }
}
"""


def _composer_manifest(name: str) -> str:
    manifest = {
        "name": f"example/{name.lower()}",
        "type": "project",
        "require": {"php": ">=8.2"},
        "autoload": {"psr-4": {"App\\": "src/"}},
    }
    return json.dumps(manifest, indent=4) + "\n"


class PhpProject(BaseProject):
    project_type = ProjectType.PHP
    icon = "🐘"
    install_commands = (Command("sudo dnf install -y php php-cli composer"),)

    def create(self, path: Path, name: str) -> None:
        root = path / name
        root.mkdir(parents=True)
        self._write_sources(root)
        (root / "composer.json").write_text(_composer_manifest(name))
        Command("composer install").run(cwd=root)

    def _write_sources(self, root: Path) -> None:
        source_dir = root / "src"
        source_dir.mkdir()
        (source_dir / "Greeter.php").write_text(GREETER_PHP)
        (root / "index.php").write_text(INDEX_PHP)
