from smithy.base_project import BaseProject
from smithy.enums import ProjectType
from smithy.projects.cpp_project import CppProject
from smithy.projects.python_project import PythonProject
from smithy.projects.rust_project import RustProject

PROJECTS: dict[ProjectType, BaseProject] = {
    ProjectType.PYTHON: PythonProject(),
    ProjectType.RUST: RustProject(),
    ProjectType.CPP: CppProject(),
}
