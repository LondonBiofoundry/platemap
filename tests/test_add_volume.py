import pytest
from platemap import Plate, add_volume


def test_add_volume():
    """
    Tests 6 plate well is built correctly

    """
    plate96 = Plate(size=6, well_volume=20000)
    add_volume(plate96, "A1", 5000, "water")
    assert plate96["A1"] == {
        "id": "A1",
        "total_volume": 5000,
        "composition": {"water": {"volume": 5000, "concentration": None}},
    }
    add_volume(plate96, "A1", 5000, "water")
    assert plate96["A1"] == {
        "id": "A1",
        "total_volume": 10000,
        "composition": {"water": {"volume": 10000, "concentration": None}},
    }


def test_add_multiple_volumes():
    """
    Tests 6 plate well is built correctly

    """
    plate96 = Plate(size=6, well_volume=20000)
    add_volume(plate96, "A1", 5000, "water")
    assert plate96["A1"] == {
        "id": "A1",
        "total_volume": 5000,
        "composition": {"water": {"volume": 5000, "concentration": None}},
    }
    add_volume(plate96, "A1", 2000, "juice")
    assert plate96["A1"] == {
        "id": "A1",
        "total_volume": 7000,
        "composition": {
            "water": {"volume": 5000, "concentration": None},
            "juice": {"volume": 2000, "concentration": None},
        },
    }


def test_add_too_much_volume():
    """
    Tests 6 plate well is built correctly

    """
    plate96 = Plate(size=6, well_volume=20000)
    with pytest.raises(ValueError):
        add_volume(plate96, "A1", 40000, "water")
