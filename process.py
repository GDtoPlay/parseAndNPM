# -*- coding: utf8 -*-
from packet_read import *
from classify import *
from classtype_module import *
import json
printlist=[]

def debugInfo(payload, classifyResult, count):
    dataDic = dict()
    dataDic["Language"] = classifyResult['lang']
    dataDic["AttackType"] = classifyResult['attackType']
    dataDic["Payload"] = payload
    '''
    datalist.append( "[*]DEBUG Info {}".format(count))
    datalist.append("Language   | {}".format(classifyResult['lang']))
    datalist.append("AttackType | {}".format(classifyResult['attackType']))
    datalist.append("Packet     | {}".format(payload))
    '''
    printlist.append(json.dumps(dataDic))
    #print ""
    '''
    if type == "SQL":
        print "Language / Attack type | {lang} : {attackType}".format(lang=classifyResult['lang'], attackType=classifyResult['attackType'])
        contentType = parseContentType(payload)
        if checkPOST(contentType):
            parameter = parseParameter(payload, "POST")
            print "[*]Param :", parameter
        else:
            parameters = parseParameter(payload, "GET")
            for parameter in parameters:
                try:
                    print "Param | {name} : {value}".format(name=parameter['name'], value=parameter['value'])
                except:
                    print payload
            print ""
    '''

def checkResult(classifyResult, check):
    if classifyResult['lang'] != check and classifyResult['lang'] != "RESPONSE":
        return True
    return False


def testDataMake():
    debug = 1   # 디버깅 관련 변수입니다. 값이 1이면 분류 실패 시 원인을 파악하기 위해 패킷을 출력합니다.
    test = 1    # host 기반으로 분류를 할지 결정하는 변수입니다. 1이면 직접 언어와 공격 유형을 분류하며 0이면 host 기반으로 분류합니다.
    count = 0

    payloads = pcapFileRead()
    nPayloads = []
    if test:
        # newClassify함수를 테스트합니다.
        if debug == 1:
            # 분류 실패 시 디버깅 함수를 실행합니다.
            for payload in payloads:
                classifyResult = newClassify(payload)

                if not checkResult(classifyResult, "unknown"):
                    count += 1
                    debugInfo(payload, classifyResult, count)

                lannum = readLanguage(classifyResult)

                dictList = excmodule(lannum, classifyResult, payload)
                valList = []
                if dictList:
                    for valDict in dictList:
                        valList.append(valDict['value'])
                if valList:
                    nPayloads.append([valList, classifyResult['attackType']])     # [value list, attack type]

        else:
            for payload in payloads:
                classifyResult = newClassify(payload)
                lannum = readLanguage(classifyResult)

                dictList = excmodule(lannum, classifyResult, payload)
                valList = []
                if dictList:
                    for valDict in dictList:
                        valList.append(valDict['value'])
                if valList:
                    nPayloads.append([valList, classifyResult['attackType']])     # [value list, attack type]

    else:
        # host를 기반으로 분류하는 classify함수를 이용합니다.
        for payload in payloads:
            classifyResult = classify(payload)
            lannum = readLanguage(classifyResult)

            dictList = excmodule(lannum, classifyResult, payload)
            valList = []
            if dictList:
                for valDict in dictList:
                    valList.append(valDict['value'])
            if valList:
                nPayloads.append([valList, classifyResult['attackType']])          # [value list, attack type]

    #이후 special char를 통해 npm을 만들어야 함
    p=open('test.txt','w',encoding='utf-8')
    p.write(str(nPayloads))
    p.close()

def trainDataMake():
    debug = 1   # 디버깅 관련 변수입니다. 값이 1이면 분류 실패 시 원인을 파악하기 위해 패킷을 출력합니다.
    test = 1    # host 기반으로 분류를 할지 결정하는 변수입니다. 1이면 직접 언어와 공격 유형을 분류하며 0이면 host 기반으로 분류합니다.
    count = 0

    fileCount = 0

    fileLoc = "pcapFolder/train"
    fileList = os.listdir(fileLoc)
    pcapFiles = []
    for file in fileList:
        if ".pcap" in file:
            pcapFiles.append(file)

    for pFile in pcapFiles:
        payloads = pcapSingleRead(fileLoc, pFile)
        target = ""                             #학습 데이터가 어떤 공격에 대한 학습 데이터인지

        if "xss" in pFile or "XSS" in pFile:
            target = "XSS"

        elif "sql" in pFile or "SQL" in pFile:
            target = "SQLI"

        if target == "":
            print("None target pcap file")
            print(fileLoc + "/" + pFile)
            continue

        fileCount = fileCount + 1

        nPayloads = []
        if test:
            # newClassify함수를 테스트합니다.
            if debug == 1:
                # 분류 실패 시 디버깅 함수를 실행합니다.
                for payload in payloads:
                    classifyResult = newClassify(payload)

                    if not checkResult(classifyResult, "unknown"):
                        count += 1
                        debugInfo(payload, classifyResult, count)

                    lannum = readLanguage(classifyResult)

                    dictList = excmodule(lannum, classifyResult, payload)
                    valList = []
                    if dictList:
                        for valDict in dictList:
                            valList.append(valDict['value'])
                    if valList:
                        if classifyResult['attackType'] == target:
                            nPayloads.append([valList, target])     # [value list, attack type]

            else:
                for payload in payloads:
                    classifyResult = newClassify(payload)
                    lannum = readLanguage(classifyResult)

                    dictList = excmodule(lannum, classifyResult, payload)
                    valList = []
                    if dictList:
                        for valDict in dictList:
                            valList.append(valDict['value'])
                    if valList:
                        if classifyResult['attackType'] == target:
                            nPayloads.append([valList, target])     # [value list, attack type]

        else:
            # host를 기반으로 분류하는 classify함수를 이용합니다.
            for payload in payloads:
                classifyResult = classify(payload)
                lannum = readLanguage(classifyResult)

                dictList = excmodule(lannum, classifyResult, payload)
                valList = []
                if dictList:
                    for valDict in dictList:
                        valList.append(valDict['value'])
                if valList:
                    if classifyResult['attackType'] == target:
                        nPayloads.append([valList, target])          # [value list, attack type]

        #이후 special char를 통해 npm을 만들어야 함
        p=open(target + '_' + str(fileCount) + '_train.txt','w',encoding='utf-8')
        p.write(str(nPayloads))
        p.close()

def printList():
    p=open('test.json','w',encoding='utf-8')
    totalJson = toJson(printlist)
    p.write(totalJson)
    p.close()

testDataMake()
