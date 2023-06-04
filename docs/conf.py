# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'srecli'
copyright = '2023, Shibhikkiran D'
author = 'Shibhikkiran D'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autodoc.typehints",
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# config to get package build version to be populated in docs
from importlib import metadata
PACKAGE_VERSION = metadata.version('srecli')
version = release = PACKAGE_VERSION


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# config for making sphinx-apidoc run as part of the Read the Docs build process
if os.environ.get("READTHEDOCS") == "True":
    from pathlib import Path

    PROJECT_ROOT = Path(__file__).parent.parent
    PACKAGE_ROOT = PROJECT_ROOT / "src" / "srecli"

    def run_apidoc(_):
        from sphinx.ext import apidoc
        apidoc.main([
            "--force",
            "--implicit-namespaces",
            "--module-first",
            "--seperate",
            "-o",
            str(PROJECT_ROOT / "docs" / "reference"),
            str(PACKAGE_ROOT),
            str(PACKAGE_ROOT / "*.c"),
            str(PACKAGE_ROOT / "*.so"),
        ])

    def setup(app):
        app.connect("builder-inited", run_apidoc)

