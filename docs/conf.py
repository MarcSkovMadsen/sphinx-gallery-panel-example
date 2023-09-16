# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Awesome Panel'
copyright = '2023, Marc Skov Madsen'
author = 'Marc Skov Madsen'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_gallery.gen_gallery',
]

sphinx_gallery_conf = {
     'examples_dirs': '../examples',   # path to your example scripts
     'gallery_dirs': 'auto_examples',  # path to where to save gallery generated output
     'ignore_pattern': 'scr'
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']

# Configure sphinx-gallery for panel

import panel as pn
from uuid import uuid4
from io import StringIO
from html import escape

class PanelScraper():
    def __init__(self, object):
        self._object = object

    def _get_html(self):
        out = StringIO()
        self._object.save(out, embed=False)
        out.seek(0)
        return escape(out.read())
    
    def _repr_html_(self):
        html = self._get_html()    
        uid = str(uuid4())       
        return f"""
<script>
function resizeIframe(){{
    setTimeout(() => {{
        var iframe = document.getElementById("{uid}");
        iframe.width = iframe.contentWindow.document.body.scrollWidth + 10;
        iframe.height = iframe.contentWindow.document.body.scrollHeight + 10;    
    }}, "10");
    
}}
</script>        
<iframe id="{uid}" srcdoc='{html}' frameBorder='0' onload='resizeIframe(this)'></iframe>
"""

def _repr_html_(self):
    return PanelScraper(self)._repr_html_()

def configure_sphinx_gallery():
    pn.viewable.Viewable._repr_html_=_repr_html_

configure_sphinx_gallery()