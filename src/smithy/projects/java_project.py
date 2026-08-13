from pathlib import Path

from smithy.base_project import BaseProject
from smithy.command import Command
from smithy.enums import ProjectType

POM_XML = """\
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.example</groupId>
  <artifactId>{name}</artifactId>
  <version>1.0-SNAPSHOT</version>

  <properties>
    <maven.compiler.release>21</maven.compiler.release>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
  </properties>
</project>
"""

MAIN_JAVA = """\
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
"""


class JavaProject(BaseProject):
    project_type = ProjectType.JAVA
    icon = "☕"
    install_commands = (
        Command("sudo dnf install -y java-latest-openjdk-devel maven"),
    )

    def create(self, path: Path, name: str) -> None:
        root = path / name
        root.mkdir(parents=True)
        self._write_sources(root)
        (root / "pom.xml").write_text(POM_XML.format(name=name))

    def _write_sources(self, root: Path) -> None:
        source_dir = root / "src" / "main" / "java"
        source_dir.mkdir(parents=True)
        (source_dir / "Main.java").write_text(MAIN_JAVA)
