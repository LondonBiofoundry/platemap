---
id: transfer_volume
title: Transfer Volume
---

Transfering Volume maintain well proportions through liquid id's as below

```python
from platemap import Plate, add_volume, transfer
plate6 = Plate(size=6, well_volume=20000, deadspace=1000)

add_volume(plate6, "A1", 6000, "water")
add_volume(plate6, "A1", 2000, "juice")

transfer(plate6, "A1", plate6, "B1", 2000)

print(plate6.contents)

> {
    "A1": {
        "id": "A1",
        "total_volume": 6000.0,
        "composition": {
            "water": {"volume": 4500.0, "concentration": None},
            "juice": {"volume": 1500.0, "concentration": None},
        },
    },
    "B1": {
        "id": "B1",
        "total_volume": 2000.0,
        "composition": {
            "water": {"volume": 1500.0, "concentration": None},
            "juice": {"volume": 500.0, "concentration": None},
        },
    },
    "A2": {"id": "A2", "total_volume": 0.0, "composition": {}},
    "B2": {"id": "B2", "total_volume": 0.0, "composition": {}},
    "A3": {"id": "A3", "total_volume": 0.0, "composition": {}},
    "B3": {"id": "B3", "total_volume": 0.0, "composition": {}},
}
```
