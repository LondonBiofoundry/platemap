---
sidebar_label: add_volume
title: platemap.PlateUtils.add_volume
---

#### add\_volume

```python
add_volume(destination_plate: Plate, destination_well: str, volume: float, volume_id: str, volume_concentration: int = None)
```

Add volume to a well of a plate object

**Arguments**:

- `destination_plate` _Plate_ - target plate in which volume will be added to,
- `destination_well` _str_ - target well in which volume will be added to,
- `volume` _float_ - volume of liquid to add to the specified well,
- `volume_id` _str_ - identifier of liquid to be added to specified well,
- `volume_concentration` _int_ - concentraion of liquid to be added to specified well,
  

**Raises**:

- `ValueError` - if volume well added exceeds well capacity

