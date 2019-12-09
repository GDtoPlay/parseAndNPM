# -*- coding: utf8 -*-
import sys
import os
from scapy.all import *
import zlib
import json
import csv

def toJson(outList):
    outJson = "["
    firstFlag = True
    for dic in outList:
        if firstFlag:
            outJson = outJson + json.dumps(dic, indent=4, sort_keys=True)
            firstFlag = False

        else:
            outJson = outJson + ",\n"
            outJson = outJson + json.dumps(dic, indent=4, sort_keys=True)


    outJson = outJson + "]"

    return outJson

def csvFileRead():
    fileLoc = "csvFolder"
    fileList = os.listdir(fileLoc)
    csvFiles = []
    for file in fileList:
        if ".csv" in file:
            csvFiles.append(file)

    for cFile in csvFiles:
        f = open(fileLoc + "/" + cFile, encoding='utf-8')
        rdr = list(csv.reader(f))
        firstLine = rdr[0]

        sourceLoc = 0
        destinationLoc = 0
        infoLoc = 0
        colCount = 0

        for col in firstLine:
            if col == "Source":
                sourceLoc = colCount
            elif col == "Destination":
                destinationLoc = colCount
            elif col == "Info":
                infoLoc = colCount

            colCount = colCount + 1

        pList =[]

        for packet in rdr[1:]:
            pDict = dict()

            pDict["srcIP"] = packet[sourceLoc]
            pDict["dstIP"] = packet[destinationLoc]

            pInfo = processHTTP(packet[infoLoc].encode())
            for k,v in pInfo.items():
                pDict[k] = v

            pList.append(pDict)

    return pList
        #print(toJson(pList))

def pcapFileRead():
    fileLoc = "pcapFolder"
    fileList = os.listdir(fileLoc)
    pcapFiles = []
    for file in fileList:
        if ".pcap" in file:
            pcapFiles.append(file)

    for pFile in pcapFiles:
        pkt = rdpcap(fileLoc + "/" + pFile)

        pList =[]

        for packet in pkt:
            layer = packet.payload
            pDict = dict()

            while layer:
                layerName = layer.name

                if layerName == "IP":
                    pDict["srcIP"] = layer.src
                    pDict["dstIP"] = layer.dst

                if layerName == "TCP":
                    pDict["sport"] = layer.sport
                    pDict["dport"] = layer.dport


                if layerName == "Raw":
                    result = processHTTP(layer.load)
                    for k,v in result.items():
                        pDict[k] = v

                layer = layer.payload

                if "Method" in pDict or "body" in pDict:

                    # body만 있고 Method가 없는 경우가 있어서 초기화하였습니다.
                    if "Method" not in pDict:
                        pDict['Method'] = ''
                    pList.append(pDict)

    return pList
        #print(toJson(pList))

def processHTTP(data):
    headDict = dict()


    rawPacket = bytes(data)
    try:
        firstLine = (data.decode("utf8")).splitlines()[0]
    except:
        firstLine = (data.decode("iso-8859-1")).splitlines()[0]

    httpMethod = ["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH", "HTTP"]
    isHttp = False


    for method in httpMethod:
        if firstLine.startswith(method):

            if method == "GET":
                headDict["Method"] = firstLine.split()[0]
                headDict["URL"] = firstLine.split()[1]

            elif method == "POST":
                headDict["Method"] = firstLine.split()[0]
                headDict["URL"] = firstLine.split()[1]

            elif method == "HTTP":
                headDict["Method"] = firstLine.split()[0]
                headDict["Status"] = firstLine.split()[1]

            else:
                headDict["Method"] = firstLine.split()[0]
            isHttp = True

    if isHttp:
        try:
            httpHeaders = rawPacket[:rawPacket.index(b"\r\n\r\n")+2]
        except:
            httpHeaders = rawPacket

        try:
            httpContentParse = dict(re.findall(r"(?P<key>.*?): (?P<value>.*?)\r\n", httpHeaders.decode("utf8")))

            if "Content-Type" in httpContentParse.keys():
                payload = ""
                tempPayload = rawPacket[rawPacket.index(b"\r\n\r\n")+4:]
                try:
                    if "Content-Encoding" in httpContentParse.keys():
                        if httpContentParse["Content-Encoding"] == "gzip":
                            payload = zlib.decompress(tempPayload, 16+zlib.MAX_WBITS)
                        elif httpContentParse["Content-Encoding"] == "deflate":
                            payload = zlib.decompress(tempPayload)
                        else:
                            payload = tempPayload.decode("utf8")
                    else:
                        payload = tempPayload.decode("utf8")
                except:
                    pass


                httpContentParse["Data"] = payload

            httpContentParse.update(headDict)
            return httpContentParse

        except:
            return dict()

    else:
        try:
            headDict['body'] = data.decode('utf-8')
        except:
            headDict['body'] = data

        return headDict

