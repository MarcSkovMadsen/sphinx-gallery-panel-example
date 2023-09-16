# sphinx-gallery-panel-example

An example of a minimal sphinx-gallery using Panel used for the discussion in
[holoviz/discourse#6035](https://discourse.holoviz.org/t/how-to-use-sphinx-gallery-with-panel/6035)

## Build the project

```bash
sphinx-build -b html docs docs/_build/html
```

## Serve the project

You can start a web server to view the project locally using

```bash
python -m http.server -d docs/_build/html/
```

The project is available at [http://localhost:8000](http://localhost:8000).

## Rebuild

Remove the `autoexamples` folder and build again.

```bash
rm -rf docs/auto_examples/;sphinx-build -b html docs docs/_build/html
```

## Creating this repository from scratch

If you want to create this example repository from scratch

Install the Python dependencies

```python
python -m venv .venv
source .venv/bin/activate # linux. Use similar command for windows or macos
pip install -r requirements.txt
```

Create the Sphinx docs folder

```bash
mkdir docs
cd docs
sphinx-quickstart
```

Create the [examples](examples) folder. Remember to include docstrings in your example files.
The docstrings should be in restructered text format and include a header.

Configure and use Sphinx-Gallery as described [here](https://sphinx-gallery.github.io/stable/getting_started.html#configure-and-use-sphinx-gallery)