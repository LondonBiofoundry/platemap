---
id: creating_plates_1
title: Creating Plates
---

## Standard Plate Dimensions

Plates can be created from size attribute if the user requires standand 2:3 ratio plates, this functionallity is implemented for plate sizes of <code>[6, 24, 96, 384, 1536]</code>

| Plate Instance                | Rows | Columns |
| ----------------------------- | ---- | ------- |
| `plate6 = Plate(size = 6)`    | 2    | 3       |
| `plate6 = Plate(size = 24)`   | 4    | 6       |
| `plate6 = Plate(size = 96)`   | 8    | 12      |
| `plate6 = Plate(size = 384`   | 16   | 24      |
| `plate6 = Plate(size = 1536)` | 32   | 48      |

## Non-Standard Plate Dimensions

Plates can be created of any number or rows or columns by further adding rows and columns attributes when initiating the plate class.

```python
from platemap import Plate
plate_100_wells = Plate(size = 100, rows = 10, columns = 10)
```

## Setting `well_volume`

Some utility functions available for the Plate class require `well_volume` to be set to ensure wells are dont overflow, the well_volume is designed to reflect nanoliters however as long as you stay consistent, you can use any volume units you like.

Once assigned it becomes an accessible attribute of the class for reference, and use by utility functions.

```python
from platemap import Plate
plate_6_well = Plate(size = 6, well_volume = 50000)
print('Capacity per well of plate is: ',plate_6_well.well_volume)
```

```bash
>>> Capacity per well of plate is: 50000
```

## Setting `deadspace`

Deadspace is the unaccessable / unusable / lost volume within each well.

Some utility functions available for the Plate class require `deadspace` to be set to ensure wells aren't aspirated when they can't, the deadspace is designed to reflect nanoliters however as long as you stay consistent, you can use any volume units you like.

Once assigned it becomes an accessible attribute of the class for reference, and use by utility functions.

```python
from platemap import Plate
plate_6_well = Plate(size = 6, well_volume = 50000, deadspace = 10000)
print('Usable volume per well of plate is: ',plate_6_well.well_volume - plate_6_well.deadspace)
```

```bash
>>> Usable volume per well of plate is: 40000
```
