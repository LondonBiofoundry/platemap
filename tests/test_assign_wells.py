import pytest
from platemap import Plate, assign_source_wells


def test_recurring_values_in_division():
    plate6 = Plate(size=6, well_volume=50000, deadspace=20000)
    assign_source_wells(plate6, {"water": 40000, "juice": 30000}, fill_to=40000)
    assert plate6.contents == {
        "A1": {
            "id": "water",
            "total_volume": 40000.0,
            "composition": {"water": {"volume": 40000, "concentration": None}},
        },
        "B1": {
            "id": "water",
            "total_volume": 40000.0,
            "composition": {"water": {"volume": 40000, "concentration": None}},
        },
        "A2": {
            "id": "juice",
            "total_volume": 40000.0,
            "composition": {"juice": {"volume": 40000, "concentration": None}},
        },
        "B2": {
            "id": "juice",
            "total_volume": 40000.0,
            "composition": {"juice": {"volume": 40000, "concentration": None}},
        },
        "A3": {"id": "A3", "total_volume": 0.0, "composition": {}},
        "B3": {"id": "B3", "total_volume": 0.0, "composition": {}},
    }
