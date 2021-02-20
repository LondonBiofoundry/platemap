---
sidebar_label: plate
title: platemap.plate
---

## Plate Objects

```python
class Plate()
```

Class for Plate objects.

Generate a structure to handle plates and contents of wells

**Attributes**:

- `size` _int_ - Number of wells within the plate.
- `id` _str_ - Unique identification of the plate object.
- `deadspace` _int_ - Volume of unaccessable / unreachable liquid within each well
- `rows` _list_ - row labels within plate e.g. [&#x27;A&#x27;,&#x27;B&#x27;...]
- `columns` _list_ - column labels within plate e.g. [1,2,3,4...]
- `well_volume` _int_ - volume of liquid within each well

#### \_\_init\_\_

```python
 | __init__(size: int, id: str = uuid.uuid4(), deadspace: int = None, rows: int = None, columns: int = None, well_volume: int = None)
```

Initiation object of Plate objects.

Plate can be initiated which just size without rows and columns if size
is of regular 2:3 ratio one of [6, 24, 96, 384, 1536]

**Arguments**:

- `size` _int_ - Number of wells within the plate.
- `id` _str_ - Unique identification of the plate object.
- `deadspace` _int_ - Volume of unaccessable / unreachable liquid within each well
- `rows` _int_ - number of rows within the plate
- `columns` _int_ - number of columns within the plate
- `well_volume` _int_ - volume of liquid within each well
  

**Raises**:

- `ValueError` - If rows or columns is a not a postive integer, or if rows and columns are
  not supplied and size is not regular 2:3 ratio.

#### \_\_getitem\_\_

```python
 | __getitem__(k)
```

Return e.g. well A1&#x27;s dict when calling myplate[&quot;A1&quot;].

#### set\_well\_id

```python
 | set_well_id(well: str, id: str)
```

Set id of individual wells

#### set\_well\_volume

```python
 | set_well_volume(well: str, volume: int)
```

Set volume of individual wells

#### update\_well\_composition

```python
 | update_well_composition(well: str, volume: int, volume_id: str, volume_concentration: int = None)
```

Update composition of individual wells

