# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PK4ADI Calculator'
copyright = '2024, SJ'
author = 'SJ'
release = '0.1.4.d'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'recommonmark']

templates_path = ['_templates']
exclude_patterns = []

# -- Options for locale output -------------------------------------------------

# multi-language docs
language = 'en'
locale_dirs = ['../locales/']   # path is example but recommended.
gettext_compact = False  # optional.
gettext_uuid = True  # optional


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
