import pytest
from platemap import Plate, add_volume, remove_volume


def test_remove_volume():
    """
    Tests 6 plate well is built correctly

    """
    plate96 = Plate(size=6, well_volume=20000, deadspace=1000)
    add_volume(plate96, "A1", 10000, "water")
    remove_volume(plate96, "A1", 2000)
    assert plate96["A1"] == {
        "id": "A1",
        "total_volume": 8000,
        "composition": {"water": {"volume": 8000, "concentration": None}},
    }


def test_appoach_deadspace():
    """
    Tests 6 plate well is built correctly

    """
    plate96 = Plate(size=6, well_volume=20000, deadspace=1000)
    add_volume(plate96, "A1", 5000, "water")
    remove_volume(plate96, "A1", 4000)
    assert plate96["A1"] == {
        "id": "A1",
        "total_volume": 1000,
        "composition": {
            "water": {"volume": 1000, "concentration": None},
        },
    }
    with pytest.raises(ValueError):
        remove_volume(plate96, "A1", 100)


def test_division_multiple_components():
    """
    Tests 6 plate well is built correctly

    """
    plate96 = Plate(size=6, well_volume=20000, deadspace=1000)
    add_volume(plate96, "A1", 3000, "water")
    add_volume(plate96, "A1", 2000, "juice")
    remove_volume(plate96, "A1", 1000)
    assert plate96["A1"] == {
        "id": "A1",
        "total_volume": 4000,
        "composition": {
            "water": {"volume": 2400.0, "concentration": None},
            "juice": {"volume": 1600.0, "concentration": None},
        },
    }
    remove_volume(plate96, "A1", 2000)
    assert plate96["A1"] == {
        "id": "A1",
        "total_volume": 2000,
        "composition": {
            "water": {"volume": 1200.0, "concentration": None},
            "juice": {"volume": 800.0, "concentration": None},
        },
    }


def test_recurring_values_in_division():
    plate96 = Plate(size=6, well_volume=20000, deadspace=1000)
    add_volume(plate96, "A1", 2000, "water")
    add_volume(plate96, "A1", 1000, "juice")
    remove_volume(plate96, "A1", 2000)
    assert plate96["A1"] == {
        "id": "A1",
        "total_volume": 1000,
        "composition": {
            "water": {"volume": 666.6666666666667, "concentration": None},
            "juice": {"volume": 333.33333333333337, "concentration": None},
        },
    }
