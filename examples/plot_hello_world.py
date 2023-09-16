"""
Hello World
===========

This is a Panel *hello world* example
"""
import panel as pn

pn.extension()
out = pn.panel("Hello World")

from scraper import PanelScraper
PanelScraper(out)