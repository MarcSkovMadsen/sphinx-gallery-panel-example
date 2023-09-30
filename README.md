# Sphinx Gallery - Panel Example

An example of a minimal [sphinx-gallery](https://sphinx-gallery.github.io/stable/index.html) that works with [Panel](https://panel.holoviz.org/).

![Panel Sphinx Gallery](assets/images/panel-sphinx-gallery.png)

![Panel Sphinx Example](assets/images/panel-sphinx-gallery-example.png)

See

- the feature request in [panel#5519](https://github.com/holoviz/panel/issues/5519)
- the discussion in [holoviz/discourse#6035](https://discourse.holoviz.org/t/how-to-use-sphinx-gallery-with-panel/6035)

for more context.

## Install the project

```bash
git clone https://github.com/MarcSkovMadsen/sphinx-gallery-panel-example.git
cd sphinx-gallery-panel-example
python -m venv .venv
source .venv/bin/activate # linux. Use similar command for windows or macos
pip install -r requirements.txt
```

## Serve the examples

```bash
panel serve examples/*.py examples/**/*.py --autoreload 
```

## Develop the gallery

### Build

```bash
sphinx-build -b html docs docs/_build/html
```

### Serve

You can start a web server to view the project locally using

```bash
python -m http.server -d docs/_build/html/
```

The project is available at [http://localhost:8000](http://localhost:8000).

### Rebuild

Remove the `docs/examples` folder and build again.

```bash
rm -rf docs/examples/;sphinx-build -b html docs docs/_build/html
```
