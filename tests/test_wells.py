import pytest
from platemap import Plate


def test_build_6_well_plate():
    """
    Tests 6 plate well is built correctly

    """
    plate6 = Plate(size=6)
    assert plate6.size == 6
    assert plate6.rows == ["A", "B"]
    assert plate6.columns == [1, 2, 3]
    assert plate6.wells == ["A1", "B1", "A2", "B2", "A3", "B3"]
    assert plate6.well_volume == None
    assert plate6.deadspace == None


def test_build_12_well_plate():
    """
    Tests 6 plate well is built correctly

    """
    plate6 = Plate(size=12, rows=3, columns=4)
    assert plate6.size == 12
    assert plate6.rows == ["A", "B", "C"]
    assert plate6.columns == [1, 2, 3, 4]
    assert plate6.wells == [
        "A1",
        "B1",
        "C1",
        "A2",
        "B2",
        "C2",
        "A3",
        "B3",
        "C3",
        "A4",
        "B4",
        "C4",
    ]
    assert plate6.well_volume == None
    assert plate6.deadspace == None


def test_build_24_well_plate():
    """
    Tests 6 plate well is built correctly

    """
    plate6 = Plate(size=24)
    assert plate6.size == 24
    assert plate6.rows == ["A", "B", "C", "D"]
    assert plate6.columns == [1, 2, 3, 4, 5, 6]
    assert plate6.wells == [
        "A1",
        "B1",
        "C1",
        "D1",
        "A2",
        "B2",
        "C2",
        "D2",
        "A3",
        "B3",
        "C3",
        "D3",
        "A4",
        "B4",
        "C4",
        "D4",
        "A5",
        "B5",
        "C5",
        "D5",
        "A6",
        "B6",
        "C6",
        "D6",
    ]
    assert plate6.well_volume == None
    assert plate6.deadspace == None


def test_build_24_well_plate():
    """
    Tests 6 plate well is built correctly

    """
    plate6 = Plate(size=24)
    assert plate6.size == 24
    assert plate6.rows == ["A", "B", "C", "D"]
    assert plate6.columns == [1, 2, 3, 4, 5, 6]
    assert plate6.wells == [
        "A1",
        "B1",
        "C1",
        "D1",
        "A2",
        "B2",
        "C2",
        "D2",
        "A3",
        "B3",
        "C3",
        "D3",
        "A4",
        "B4",
        "C4",
        "D4",
        "A5",
        "B5",
        "C5",
        "D5",
        "A6",
        "B6",
        "C6",
        "D6",
    ]
    assert plate6.well_volume == None
    assert plate6.deadspace == None


def test_build_48_well_plate():
    """
    Tests 6 plate well is built correctly

    """
    plate6 = Plate(size=48, rows=6, columns=8)
    assert plate6.size == 48
    assert plate6.rows == ["A", "B", "C", "D", "E", "F"]
    assert plate6.columns == [1, 2, 3, 4, 5, 6, 7, 8]
    assert plate6.well_volume == None
    assert plate6.deadspace == None


def test_build_96_well_plate():
    """
    Tests 6 plate well is built correctly

    """
    plate6 = Plate(size=96)
    assert plate6.size == 96
    assert plate6.rows == ["A", "B", "C", "D", "E", "F", "G", "H"]
    assert plate6.columns == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    assert plate6.wells == [
        "A1",
        "B1",
        "C1",
        "D1",
        "E1",
        "F1",
        "G1",
        "H1",
        "A2",
        "B2",
        "C2",
        "D2",
        "E2",
        "F2",
        "G2",
        "H2",
        "A3",
        "B3",
        "C3",
        "D3",
        "E3",
        "F3",
        "G3",
        "H3",
        "A4",
        "B4",
        "C4",
        "D4",
        "E4",
        "F4",
        "G4",
        "H4",
        "A5",
        "B5",
        "C5",
        "D5",
        "E5",
        "F5",
        "G5",
        "H5",
        "A6",
        "B6",
        "C6",
        "D6",
        "E6",
        "F6",
        "G6",
        "H6",
        "A7",
        "B7",
        "C7",
        "D7",
        "E7",
        "F7",
        "G7",
        "H7",
        "A8",
        "B8",
        "C8",
        "D8",
        "E8",
        "F8",
        "G8",
        "H8",
        "A9",
        "B9",
        "C9",
        "D9",
        "E9",
        "F9",
        "G9",
        "H9",
        "A10",
        "B10",
        "C10",
        "D10",
        "E10",
        "F10",
        "G10",
        "H10",
        "A11",
        "B11",
        "C11",
        "D11",
        "E11",
        "F11",
        "G11",
        "H11",
        "A12",
        "B12",
        "C12",
        "D12",
        "E12",
        "F12",
        "G12",
        "H12",
    ]
    assert plate6.well_volume == None
    assert plate6.deadspace == None
