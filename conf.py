# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add any paths to sys.path if your modules are outside the root
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Cash App Taxes – Free Tax Filing Guide'
copyright = '2025, Cash App Taxes'
author = 'Cash App Taxes Support Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Sphinx extensions (leave blank or add as needed)
extensions = []

# Allow reStructuredText raw HTML
raw_enabled = True

# Templates and patterns to ignore
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Theme (you can switch to 'sphinx_rtd_theme' or another as needed)
# html_theme = 'sphinx_rtd_theme'

# Basic page info
html_title = "Cash App Taxes – How to File Free Taxes With Cash App"
html_short_title = "Cash App Taxes Filing Guide"
html_favicon = 'favicon.ico'  # Place your favicon in _static or root

# Hide "View page source"
html_show_sourcelink = False

# Allow unsafe raw HTML in .rst files
html_allow_unsafe = True

# Theme customization
html_theme_options = {
    'show_powered_by': False,
}

# Static assets (if any)
# html_static_path = ['_static']
