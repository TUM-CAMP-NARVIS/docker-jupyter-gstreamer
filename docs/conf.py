# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "docker-stacks"
copyright = "2022, Project Jupyter"
author = "Project Jupyter"

# The short X.Y version
version = "latest"

# The full version, including alpha/beta/rc tags
release = "latest"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# File above was generated using sphinx 4.3.2 with this command:
# sphinx-quickstart --project "docker-stacks" --author "Project Jupyter" -v "latest" -r "latest" -l en --no-sep --no-makefile --no-batchfile
# These are custom options for this project

html_theme = "sphinx_book_theme"
html_title = "Docker Stacks documentation"
html_logo = "_static/jupyter-logo.svg"
html_theme_options = {
    "path_to_docs": "docs",
    "repository_url": "https://github.com/jupyter/docker-stacks",
    "use_edit_page_button": True,
    "use_issues_button": True,
    "use_repository_button": True,
    "use_download_button": True,
}

extensions = ["myst_parser", "sphinx_copybutton"]
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
pygments_style = "sphinx"

# MyST configuration reference: https://myst-parser.readthedocs.io/en/latest/sphinx/reference.html
myst_heading_anchors = 3

linkcheck_ignore = [
    r".*github\.com.*#",  # javascript based anchors
    r"https://docs.github\.com/.*",  # 403 error
    r"http://127\.0\.0\.1:49153/.*",  # example
    r"https://mybinder\.org/v2/gh/.*",  # lots of 500 errors
]

linkcheck_allowed_redirects = {
    r"https://results\.pre-commit\.ci/latest/github/jupyter/docker-stacks/master": r"https://results\.pre-commit\.ci/run/github/.*",  # Latest master CI build
    r"https://github\.com/jupyter/docker-stacks/issues/new.*": r"https://github\.com/login.*",  # GitHub wants user to be logon to use this features
    r"https://github\.com/orgs/jupyter/teams/docker-image-maintainers/members": r"https://github\.com/login.*",
}