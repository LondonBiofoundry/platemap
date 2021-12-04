import xmltodict
import json


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
        "volume": record["SurveyFluidVolume"]["#text"],
    }


def getBodyRecordInfo(body):
    surveyData = map(mapBodyRecordInfo, body)
    surveyList = list(surveyData)
    print(surveyList)
    return surveyList
