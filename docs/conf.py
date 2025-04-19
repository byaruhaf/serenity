# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import sys
from datetime import datetime

project = "Serenity"
copyright = "2025, Franklin Byaruhanga"
author = "Franklin Byaruhanga"

year = datetime.now().year
if year > 2024:
    copyright = f"2024-{year}, {author}"
else:
    copyright = f"2024, {author}"

sys.path.append("../src")
import serenity  # noqa: E402

release = serenity.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = "alabaster"
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
