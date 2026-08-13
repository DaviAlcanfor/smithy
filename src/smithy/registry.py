from smithy.base_project import BaseProject
from smithy.enums import ProjectType
from smithy.projects.astro_project import AstroProject
from smithy.projects.c_project import CProject
from smithy.projects.cpp_project import CppProject
from smithy.projects.go_project import GoProject
from smithy.projects.java_project import JavaProject
from smithy.projects.javascript_project import JavaScriptProject
from smithy.projects.php_project import PhpProject
from smithy.projects.python_project import PythonProject
from smithy.projects.rust_project import RustProject
from smithy.projects.typescript_project import TypeScriptProject

PROJECTS: dict[ProjectType, BaseProject] = {
    ProjectType.PYTHON: PythonProject(),
    ProjectType.RUST: RustProject(),
    ProjectType.GO: GoProject(),
    ProjectType.JAVA: JavaProject(),
    ProjectType.C: CProject(),
    ProjectType.CPP: CppProject(),
    ProjectType.JAVASCRIPT: JavaScriptProject(),
    ProjectType.TYPESCRIPT: TypeScriptProject(),
    ProjectType.ASTRO: AstroProject(),
    ProjectType.PHP: PhpProject(),
}
