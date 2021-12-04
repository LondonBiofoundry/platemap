import pytest
from platemap import Plate, parseEchoSurveyXML, add_volume
import xmltodict
import json

from platemap.PlateUtils.parse_echo_volume_survey import updateVolumesFromEchoSurveyData


def test_can_update_volumes_from_xml():
    """
    Tests 6 plate well is built correctly

    """
    volumeSurvey = [{"well": "A1", "volume": 29.831}]
    plate = Plate(size=6, well_volume=50)
    updateVolumesFromEchoSurveyData(plate, volumeSurvey)
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
