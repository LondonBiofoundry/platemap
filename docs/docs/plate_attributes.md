---
id: plate_attributes
title: Using Plate Attributes
---

## Rows -- and columns ||

The rows and columns attributes contain a list of the row and column id's respectively

```python
from platemap import Plate
example_96_well_plate = Plate(size = 96, deadspace = 10000, well_volume = 50000)
```

```python
print(example_96_well_plate.rows)
> ['A','B','C','D','E','F','G','H']
```

```python
print(example_96_well_plate.colunms)
> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
```

## Well ID's

A list of all well id's can be obtained with

```python
print(example_96_well_plate.wells)
> ["A1","B1","C1","D1","E1","F1","G1","H1",
   "A2","B2","C2","D2","E2","F2","G2","H2",
   "A3","B3","C3","D3","E3","F3","G3","H3",
   "A4","B4","C4","D4","E4","F4","G4","H4",
   "A5","B5","C5","D5","E5","F5","G5","H5",
   "A6","B6","C6","D6","E6","F6","G6","H6",
   "A7","B7","C7","D7","E7","F7","G7","H7",
   "A8","B8","C8","D8","E8","F8","G8","H8",
   "A9","B9","C9","D9","E9","F9","G9","H9",
   "A10","B10","C10","D10","E10","F10","G10","H10",
   "A11","B11","C11","D11","E11","F11","G11","H11",
   "A12","B12","C12","D12","E12","F12","G12","H12"]
```
