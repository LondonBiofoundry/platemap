---
sidebar_label: find_next_well
title: platemap.PlateUtils.find_next_well
---

#### find\_well

```python
def find_well(target_plate: Plate, target_volume_id: str, target_volume: int)
```

Finds the next available well for a specific reagent-id that has sufficient volume defined by the third input argument.

**Arguments**:

- `target_plate` _Plate_ - The target plate to analyse.
- `target_volume_id` _str_ - The regaent ID that you are looking for.
- `target_volume` _int_ - The volume that you are looking to take.

