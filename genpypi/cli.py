import os
import sys
import shutil
from pathlib import Path
import click

TEMPLATE_DIR = Path(__file__).parent / "templates"

def create_project_structure(package_name: str):
    """Create the basic project structure."""
    project_dir = Path(package_name)
    src_dir = project_dir / package_name
    
    # Create directories
    os.makedirs(src_dir, exist_ok=True)
    os.makedirs(project_dir / "tests", exist_ok=True)
    
    # Copy templates
    # Main package __init__.py
    shutil.copy(
        TEMPLATE_DIR / "src_init.py",
        src_dir / "__init__.py"
    )
    
    # Root level files
    files_to_copy = {
        "setup.py": "setup.py",
        "README.md": "README.md",
        "LICENSE": "LICENSE",
        "gitignore": ".gitignore"
    }
    
    for template, dest in files_to_copy.items():
        with open(TEMPLATE_DIR / template, "r") as f:
            content = f.read()
            content = content.replace("{{ package_name }}", package_name)
        with open(project_dir / dest, "w") as f:
            f.write(content)
    
    # Create GitHub workflow directory and file
    workflow_dir = project_dir / ".github" / "workflows"
    os.makedirs(workflow_dir, exist_ok=True)
    
    with open(TEMPLATE_DIR / "publish.yml", "r") as f:
        workflow_content = f.read().replace("{{ package_name }}", package_name)
    
    with open(workflow_dir / "publish.yml", "w") as f:
        f.write(workflow_content)

@click.command()
@click.argument("package_name")
def main(package_name):
    """Generate a Python project structure ready for PyPI publication."""
    try:
        create_project_structure(package_name)
        click.echo(f"Successfully created project: {package_name}")
    except Exception as e:
        click.echo(f"Error creating project: {e}", err=True)
        sys.exit(1)