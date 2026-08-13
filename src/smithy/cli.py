import argparse
import subprocess
import sys
from collections.abc import Sequence
from pathlib import Path

from smithy.base_project import BaseProject
from smithy.config import Config
from smithy.enums import ProjectType
from smithy.icons import PROJECT_ICONS
from smithy.interactive import prompt_new_project
from smithy.registry import PROJECTS


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="smithy",
        description="Cria projetos novos com as ferramentas prontas.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    new = subparsers.add_parser("new", help="cria um projeto novo")
    _add_project_type_argument(new)
    new.add_argument("name", help="nome do projeto")
    new.add_argument(
        "-p",
        "--path",
        type=Path,
        help="diretório onde criar o projeto (padrão: SMITHY_PROJECTS_DIR)",
    )

    install = subparsers.add_parser(
        "install", help="instala as ferramentas de um tipo de projeto"
    )
    _add_project_type_argument(install)

    subparsers.add_parser("list", help="lista os tipos de projeto")

    return parser


def _add_project_type_argument(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "project_type",
        type=ProjectType,
        choices=sorted(PROJECTS),
        metavar="tipo",
        help=f"um de: {', '.join(sorted(PROJECTS))}",
    )


def create_project(project: BaseProject, path: Path, name: str) -> None:
    path.mkdir(parents=True, exist_ok=True)
    print(f"{project.icon} criando {name} em {path}")
    project.create(path, name)


def install_toolchain(project: BaseProject) -> None:
    print(f"{project.icon} instalando ferramentas de {project.project_type}")
    for command in project.install_commands:
        command.run()


def list_project_types() -> None:
    for project_type, icon in PROJECT_ICONS.items():
        suffix = "" if project_type in PROJECTS else "  (ainda não implementado)"
        print(f"{icon}  {project_type}{suffix}")


def run_command(args: argparse.Namespace) -> int:
    if args.command == "list":
        list_project_types()
        return 0

    project = PROJECTS[args.project_type]
    if args.command == "install":
        install_toolchain(project)
        return 0

    path = args.path or Config.from_env().projects_dir
    create_project(project, path, args.name)
    return 0


def run_interactive() -> int:
    """Menu shown when `smithy` runs with no arguments."""
    if not sys.stdin.isatty():
        build_parser().print_help()
        return 1

    choice = prompt_new_project()
    if choice is None:
        return 1

    project_type, name = choice
    create_project(PROJECTS[project_type], Config.from_env().projects_dir, name)
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    arguments = list(sys.argv[1:] if argv is None else argv)
    try:
        if not arguments:
            return run_interactive()
        return run_command(build_parser().parse_args(arguments))
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"erro: {error}", file=sys.stderr)
        return 1
