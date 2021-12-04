import pytest
from platemap import Plate, parseEchoSurveyXML, add_volume
import xmltodict
import json


def clearWell(plate, well):
    plate.contents[well]["total_volume"] = 0.0
    plate.contents[well]["composition"] = {}


def updateVolumesFromEchoSurvey(plate, volumeSurvey):
    for volumeUpdateDict in volumeSurvey:
        if len(plate.contents[volumeUpdateDict["well"]]["composition"]) == 0:
            add_volume(
                destination_plate=plate,
                destination_well=volumeUpdateDict["well"],
                volume=volumeUpdateDict["volume"],
                volume_id="unknown",
            )
        elif len(plate.contents[volumeUpdateDict["well"]]["composition"]) == 1:
            liquidID = plate.contents[volumeUpdateDict["well"]]["composition"].keys()[0]
            clearWell(plate, volumeUpdateDict["well"])
            add_volume(
                destination_plate=plate,
                destination_well=volumeUpdateDict["well"],
                volume=volumeUpdateDict["volume"],
                volume_id=liquidID,
            )
        else:
            add_volume(
                destination_plate=plate,
                destination_well=volumeUpdateDict["well"],
                volume=volumeUpdateDict["volume"],
                volume_id=liquidID,
            )
    return


def test_can_update_volumes_from_xml():
    """
    Tests 6 plate well is built correctly

    """
    volumeSurvey = [{"well": "A1", "volume": 29.831}]
    plate = Plate(size=6, well_volume=50)
    updateVolumesFromEchoSurvey(plate, volumeSurvey)
    assert plate.contents == {
        "A1": {
            "id": "A1",
            "total_volume": 29.831,
            "composition": {"unknown": {"volume": 29.831, "concentration": None}},
        },
        "B1": {"id": "B1", "total_volume": 0.0, "composition": {}},
        "A2": {"id": "A2", "total_volume": 0.0, "composition": {}},
        "B2": {"id": "B2", "total_volume": 0.0, "composition": {}},
        "A3": {"id": "A3", "total_volume": 0.0, "composition": {}},
        "B3": {"id": "B3", "total_volume": 0.0, "composition": {}},
    }


def test_can_parse_xml():
    """
    Tests 6 plate well is built correctly

    """
    data = parseEchoSurveyXML(
        "tests/data_for_tests/E5XX-1508_Survey_Source Plate[1](UnknownBarCode).xml"
    )
    assert data == [
        {"well": "A3", "volume": 29.831},
        {"well": "C3", "volume": 29.771},
        {"well": "E3", "volume": 29.191},
        {"well": "G3", "volume": 30.092},
        {"well": "I3", "volume": 29.911},
        {"well": "K3", "volume": 30.312},
        {"well": "M3", "volume": 30.132},
        {"well": "O3", "volume": 29.791},
        {"well": "A4", "volume": 30.572},
        {"well": "C4", "volume": 30.192},
        {"well": "E4", "volume": 30.052},
        {"well": "G4", "volume": 30.272},
        {"well": "I4", "volume": 28.35},
    ]
