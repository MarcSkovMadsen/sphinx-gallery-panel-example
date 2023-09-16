# sphinx-gallery-panel-example

An example of a sphinx-gallery using Panel

## Build the project

```bash
sphinx-build -b html docs/source/ docs/build/html
```

## Starting from scratch

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

Create the [examples](examples) folder

Configure and use Sphinx-Gallery as described [here](https://sphinx-gallery.github.io/stable/getting_started.html#configure-and-use-sphinx-gallery)