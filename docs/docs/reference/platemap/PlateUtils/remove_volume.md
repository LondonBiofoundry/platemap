---
sidebar_label: remove_volume
title: platemap.PlateUtils.remove_volume
---

#### remove\_volume

```python
def remove_volume(target_plate: Plate, target_well: str, volume: int)
```

Remove volume from a well of a plate object

**Arguments**:

- `target_plate` _Plate_ - target plate in which volume will be removed from,
- `target_well` _str_ - target well in which volume will be removed from,
- `volume` _float_ - volume of liquid to add to the specified well,
  

**Raises**:

- `ValueError` - if volume well added passes well deadspace

