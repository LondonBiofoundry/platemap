---
id: add_volume
title: Add Volume
---

## Add volume to singular wells

you can add volume using the plate utility function `add_volume`

```python
from platemap import add_volume
```

When adding volume to wells in platemap adding a liquid id is predered and utilities can track proportions of different volumes through dilutions, transfers, dispensions and aspirations.

```python
from platemap import Plate, add_volume
plate6 = Plate(size = 6, well_volume = 50000, deadspace = 10000)

add_volume(
    destination_plate = plate6
    destination_well = 'A1',
    volume = 20000,
    volume_id = 'water'
)

print(plate96["A1"])

> {
    "id": "A1",
    "total_volume": 20000,
    "composition": {"water": {"volume": 20000, "concentration": None}},
}
```

:::tip

You can access contents of wells as above by using plate96['A1'] instead of using standard plate96.contents['A1']

:::
