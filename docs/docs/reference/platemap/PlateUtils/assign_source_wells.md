---
sidebar_label: assign_source_wells
title: platemap.PlateUtils.assign_source_wells
---

#### assign\_source\_wells

```python
def assign_source_wells(plate: Plate, input_dict: Dict[str, float], fill_to: int = None, alternate_wells=False)
```

Assign source wells to a plate on bulk through a dictionary of input reagent id&#x27;s and their respective volumes.

**Arguments**:

- `plate` _Plate_ - target plate in which to fill with reagents from the input_dict,
- `input_dict` _Dict[str, float]_ - A dictionary of reagent names and their corresponding volumes,
- `fill_to` _Dict[str, float]_ - Amount to fill to in each well. If None, fill to the maximum volume.
- `alternate_wells` _boolean_ - Whether to use every other well in the plate. Sometimes useful for 384 well plates.

