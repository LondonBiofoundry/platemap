import pytest
from platemap import Plate
import xmltodict
import json


def parseXML(filename):
    with open(filename, "r") as f:
        data = f.read()
    o = xmltodict.parse(data)
    output = json.dumps(o)
    parsed = json.loads(output)
    body = getJsonReportBody(parsed)
    surveyData = getBodyRecordInfo(body)
    return surveyData


def getJsonReportBody(data):
    body = data["report"]["reportbody"]["record"]
    return body


def mapBodyRecordInfo(record):
    return {
        "well": record["SrcWell"]["#text"],
        "volume": record["SurveyFluidVolume"]["#text"],
    }


def getBodyRecordInfo(body):
    surveyData = map(mapBodyRecordInfo, body)
    surveyList = list(surveyData)
    print(surveyList)
    return surveyList


def test_build_6_well_plate():
    """
    Tests 6 plate well is built correctly

    """
    data = parseXML(
        "tests/data_for_tests/E5XX-1508_Survey_Source Plate[1](UnknownBarCode).xml"
    )
    assert data == [
        {"well": "A3", "volume": "29.831"},
        {"well": "C3", "volume": "29.771"},
        {"well": "E3", "volume": "29.191"},
        {"well": "G3", "volume": "30.092"},
        {"well": "I3", "volume": "29.911"},
        {"well": "K3", "volume": "30.312"},
        {"well": "M3", "volume": "30.132"},
        {"well": "O3", "volume": "29.791"},
        {"well": "A4", "volume": "30.572"},
        {"well": "C4", "volume": "30.192"},
        {"well": "E4", "volume": "30.052"},
        {"well": "G4", "volume": "30.272"},
        {"well": "I4", "volume": "28.35"},
    ]
