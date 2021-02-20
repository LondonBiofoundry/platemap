import pytest
from platemap import Plate, add_volume, transfer


def test_add_volume():
    """
    Tests 6 plate well is built correctly

    """
    plate6 = Plate(size=6, well_volume=20000, deadspace=1000)
    add_volume(plate6, "A1", 5000, "water")
    assert plate6["A1"] == {
        "id": "A1",
        "total_volume": 5000,
        "composition": {"water": {"volume": 5000, "concentration": None}},
    }
    transfer(plate6, "A1", plate6, "B1", 2500)
    assert plate6["A1"] == {
        "id": "A1",
        "total_volume": 2500.0,
        "composition": {"water": {"volume": 2500.0, "concentration": None}},
    }
    assert plate6["B1"] == {
        "id": "B1",
        "total_volume": 2500.0,
        "composition": {"water": {"volume": 2500.0, "concentration": None}},
    }
    assert plate6.contents == {
        "A1": {
            "id": "A1",
            "total_volume": 2500.0,
            "composition": {"water": {"volume": 2500.0, "concentration": None}},
        },
        "B1": {
            "id": "B1",
            "total_volume": 2500.0,
            "composition": {"water": {"volume": 2500.0, "concentration": None}},
        },
        "A2": {"id": "A2", "total_volume": 0.0, "composition": {}},
        "B2": {"id": "B2", "total_volume": 0.0, "composition": {}},
        "A3": {"id": "A3", "total_volume": 0.0, "composition": {}},
        "B3": {"id": "B3", "total_volume": 0.0, "composition": {}},
    }


def test_transfer_source_contains_multiple_liquids():
    plate6 = Plate(size=6, well_volume=20000, deadspace=1000)
    add_volume(plate6, "A1", 6000, "water")
    add_volume(plate6, "A1", 2000, "juice")
    assert plate6.contents == {
        "A1": {
            "id": "A1",
            "total_volume": 8000.0,
            "composition": {
                "water": {"volume": 6000, "concentration": None},
                "juice": {"volume": 2000, "concentration": None},
            },
        },
        "B1": {"id": "B1", "total_volume": 0.0, "composition": {}},
        "A2": {"id": "A2", "total_volume": 0.0, "composition": {}},
        "B2": {"id": "B2", "total_volume": 0.0, "composition": {}},
        "A3": {"id": "A3", "total_volume": 0.0, "composition": {}},
        "B3": {"id": "B3", "total_volume": 0.0, "composition": {}},
    }
    transfer(plate6, "A1", plate6, "B1", 2000)
    assert plate6.contents == {
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
