import questionary

from smithy.enums import ProjectType
from smithy.icons import PROJECT_ICONS
from smithy.registry import PROJECTS


def prompt_new_project() -> tuple[ProjectType, str] | None:
    """Ask for a project type and a name, or None if the user cancels."""
    project_type = _choose_project_type()
    if project_type is None:
        return None
    name = _ask_project_name()
    if name is None:
        return None
    return project_type, name.strip()


def _choose_project_type() -> ProjectType | None:
    choices = [
        questionary.Choice(
            title=f"{PROJECT_ICONS[project_type]}  {project_type}",
            value=project_type,
        )
        for project_type in PROJECTS
    ]
    return questionary.select("Que tipo de projeto?", choices=choices).ask()


def _ask_project_name() -> str | None:
    return questionary.text("Nome do projeto:", validate=_validate_name).ask()


def _validate_name(name: str) -> bool | str:
    stripped = name.strip()
    if not stripped:
        return "O nome não pode ser vazio."
    if "/" in stripped or stripped in {".", ".."}:
        return "O nome não pode conter '/'."
    return True
