# Distribution Metadata Review

`distribution-metadata-review` generates a deterministic review report for Python package metadata. It highlights package identity, Python compatibility, dependency counts, script entry points, and missing optional classifiers.

## Setup

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .
python -m unittest discover -v
dist-meta-review --summary
```


## Report

The report is stable across runs and contains:

- normalized package name and version;
- supported Python range;
- runtime dependency count;
- console-script names;
- metadata completeness notes.

The package uses standard setuptools packaging and has no runtime dependencies.
