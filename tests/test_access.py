import pytest
from platemap import Plate


def test_build_6_well_plate():
    """
    Tests 6 plate well is built correctly

    """
    plate6 = Plate(size=6)
    for index in plate6.wells:
        assert plate6[index] == {"id": index, "total_volume": 0, "composition": {}}
