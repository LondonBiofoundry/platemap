---
sidebar_label: transfer
title: platemap.PlateUtils.transfer
---

#### transfer

```python
def transfer(source_plate: Plate, source_well: str, destination_plate: Plate, destination_well: str, volume: int)
```

Transfer volume from one well within a plate object to another well within a plate object

**Arguments**:

- `source_plate` _Plate_ - source plate in which volume will be taken from,
- `source_well` _str_ - source well in which volume will be taken from,
- `destination_plate` _Plate_ - target plate in which volume will be added to,
- `destination_well` _str_ - target well in which volume will be added to,
- `volume` _float_ - volume of liquid to add to the specified well,
  

**Raises**:

- `ValueError` - if volume in destination well added exceeds well capacity or volume in source
  well will drop below deadspace

