---
id: installation
title: Getting Started
---

## Install platemap

To install platemap from pypi

```bash
$ pip install platemap
```

To install from github

```bash
$ git clone https://github.com/Benedict-Carling/spanish-conjugator.git
```

```bash
cd platemap
```

```bash
python setup.py install
```

## Create your first plate 🎉

It's a simple as

```python
import platemap
my_96_well_plate = platemap.Plate(size=96, rows=8, columns=12)
```

:::tip

To save time, for standard plate sizes [6, 24, 96, 384, 1536] you dont need to specify columns and rows

:::

Or even simpler as

```python
import platemap
my_96_well_plate = platemap.Plate(size=96)
```
