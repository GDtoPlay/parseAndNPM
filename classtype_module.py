# -*- coding: utf8 -*-
import json
import csv

classtype = ['PHP','SQL','JS','ASP']
def readLanguage(payload):
    # language를 읽어와 해당 언어의 index를 반환합니다.
    # for i in payload:
    #    Lan = i['lang']
    Lan = payload['lang']
    if Lan in classtype:
        return classtype.index(Lan)

def PostParse(Data, Content):
    params = []
    if 'multipart' in Content:
        token = Content.split('boundary=')
        boundary = token[-1]
        DataTokens = Data.split('--' + boundary)
        for token in DataTokens[:-1]:
            try:
                if len(token) <= 2 : continue
                nameStart = token.find('name="') + 6 #6 == len('name="')
                nameEnd = nameStart + token[nameStart:].find('"')
                name = token[nameStart:nameEnd]
                val = token.split("\r\n")[-2]
                if name or val:
                    params.append({'name': name, 'value': val})
            except:
                continue

    elif 'json' in Content:
        pass

    elif 'x-www-form-urlencoded' in Content:
        tokens = Data.split('&')
        for token in tokens:
            var = token.split('=')
            if len(var) > 1:
                params.append({'name': var[0], 'value': var[1]})

    return params



def GetParseParamsData(Referer, URL, Data, Method, Content):
    params = []
    parseLocReferer = Referer.find('?')
    parseLocURL = URL.find('?')

    parseReferer = ''
    parseURL = ''

    if parseLocReferer != -1:
        parseReferer = Referer[parseLocReferer + 1:]

    if parseLocURL != -1:
        parseURL = URL[parseLocURL + 1:]

    if parseLocReferer != -1:
        tokens = parseReferer.split('&')
        for token in tokens:
            var = token.split('=')
            if len(var) > 1:
                params.append({'name': var[0], 'value': var[1]})

    if parseLocURL != -1:
        tokens = parseURL.split('&')
        for token in tokens:
            var = token.split('=')
            if len(var) > 1:
                params.append({'name': var[0], 'value': var[1]})

    if Method == 'POST':
        postParams = PostParse(Data, Content)
        params = params + postParams

    return params



def excmodule(lannum, classifyResult, payload):
    #readLanguage에서 읽어낸 index를 기반으로 언어별 모듈을 실행합니다.
    #각 언어별로 모듈을 실행하는 코드가 들어갈 예정입니다.
    if lannum == 0:
        #excute php module
        pass
    if lannum == 1:
        if classifyResult['attackType'] == "SQLI":
            #exe SQLI
            params = GetParseParamsData(payload['Referer'],payload['URL'],payload['Data'],payload['Method'],payload['Content-Type'])
            return params
            pass
        #excute sql module
        pass
    if lannum == 2:
        if classifyResult['attackType'] == "XSS":
            #exe XSS
            params = GetParseParamsData(payload['Referer'],payload['URL'],payload['Data'],payload['Method'],payload['Content-Type'])
            return params
            pass
        #excute jsp module
        pass
    if lannum == 3:
        #excute asp module
        pass
    # 이후 언어별 모듈 추가 필요합니다.
