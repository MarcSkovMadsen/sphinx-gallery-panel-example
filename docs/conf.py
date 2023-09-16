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
import param

class PanelReprHTML(param.Parameterized):
    max_height=param.Integer(1000, bounds=(0,None))
    embed = param.Boolean(True)

    def __init__(self, object):
        self._object = object

    def _get_html(self):
        out = StringIO()
        self._object.save(out, embed=self.embed)
        out.seek(0)
        return escape(out.read())
    
    def _repr_html_(self):
        html = self._get_html()    
        uid = str(uuid4())       
        return f"""
<script>
function resizeIframe(uid){{
    setTimeout(() => {{
        var iframe = document.getElementById(uid);
        iframe.width = iframe.contentWindow.document.body.scrollWidth + 25;
        iframe.height = Math.min(iframe.contentWindow.document.body.scrollHeight + 10, {self.max_height});
        console.log(iframe.height)
    }}, "100");
    
}}
</script>        
<iframe id="{uid}" srcdoc='{html}' frameBorder='0' onload='resizeIframe("{uid}")'></iframe>
"""

def _repr_html_(self):
    return PanelReprHTML(self)._repr_html_()

def add_repr_html():
    pn.viewable.Viewable._repr_html_=_repr_html_

PanelReprHTML.max_height=600
add_repr_html()