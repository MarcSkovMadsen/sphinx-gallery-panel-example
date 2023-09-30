"""
Hello World
===========

This is a basic Panel *hello world* example `Title <http://www.google.com>`_ 
"""
import panel as pn

pn.extension()
out = pn.panel("Hello World")
out.servable()

# sphinx_gallery_thumbnail_path = '_static/thumbnails/hello_world.png'