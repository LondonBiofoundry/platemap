import string
import xmltodict
import json

from platemap.PlateUtils import add_volume
from platemap.plate import Plate


def updateVolumesFromEchoSurveyFile(plate: Plate, filepath: string):
    surveryData = parseEchoSurveyXML(filepath)
    updateVolumesFromEchoSurveyData(plate, surveryData)


def clearWell(plate, well):
    plate.contents[well]["total_volume"] = 0.0
    plate.contents[well]["composition"] = {}


def updateVolumesFromEchoSurveyData(plate, volumeSurvey):
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


def parseEchoSurveyXML(filename):
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
        "volume": float(record["SurveyFluidVolume"]["#text"]),
    }


def getBodyRecordInfo(body):
    surveyData = map(mapBodyRecordInfo, body)
    surveyList = list(surveyData)
    return surveyList
