"""
Hello Plotly
============

This is a *hello world* Plotly example
"""
import panel as pn
import numpy as np
import plotly.graph_objs as go

pn.extension('plotly', design="bootstrap")

xx = np.linspace(-3.5, 3.5, 100)
yy = np.linspace(-3.5, 3.5, 100)
x, y = np.meshgrid(xx, yy)
z = np.exp(-(x-1)**2-y**2)-(x**3+y**4-x/5)*np.exp(-(x**2+y**2))

surface = go.Surface(z=z)
layout = go.Layout(
    title='Plotly 3D Plot',
    autosize=False,
    width=500,
    height=500,
    margin=dict(t=50, b=50, r=50, l=50)
)

fig = dict(data=[surface], layout=layout)

plotly_pane = pn.pane.Plotly(fig)
plotly_pane.servable()

# sphinx_gallery_thumbnail_path = '_static/thumbnails/hello_plotly.png'