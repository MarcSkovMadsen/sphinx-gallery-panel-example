"""
Multiple Outputs
================

This example shows that multiple outputs are supported

Try the live app `here <https://www.google.com>`_ 
"""
import panel as pn

pn.extension("plotly")

# %%
# First example
out = pn.panel("Hello World")
out

# %%
# Second example
import numpy as np
import plotly.graph_objs as go

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