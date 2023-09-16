# sphinx-gallery-panel-example

An example of a sphinx-gallery using Panel

## Build the project

```bash
sphinx-build -b html docs/source/ docs/build/html
```

## Starting from scratch

If you want to create this example repository from scratch

Create the Sphinx Project

```bash
python -m venv .venv
source .venv/bin/activate # linux. Use similar command for windows or macos
pip install -r requirements.txt
mkdir docs
cd docs
sphinx-quickstart
```


