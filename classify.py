# -*- coding: utf8 -*-
# 공격 유형 및 언어 정의 코드
# 단순히 HOST만 파싱하여 정의합니다.
# 사용 방법 : 해당 classify.py를 import한 후, json으로 파싱한 결과를 인자로 주어 classify() 함수를 사용하시면 됩니다. 결과는 {'lang' : 'SQL', 'type' : 'SQLI'} 와 같습니다.

# hostInfo 변수에서 공격 유형과 공격을 진행할 host를 정의합니다.
# 정의한 hostInfo 변수는 classifyAttack 함수에서 사용합니다.
# 예를 들면 아래와 같습니다.
# a.com -> SQL Injection
# b.com -> XSS
# c.com -> File Upload
# host와 공격 유형의 인덱스를 동일하게 하여 정의하시면 됩니다.
import urllib.parse
#from urllib import unquote

hostInfo = {'host' : [], 'attack' : []}
hosts = ['a.com', 'b.com', 'c.com']
attack = ['SQLI', 'XSS', 'FileUpload']

fileUploadInfo = {'host' : [], 'lang' : []}

def defineHostInfo(host, attackType):
    hostInfo['host'].append(host)
    hostInfo['attack'].append(attackType)

def initHostInfo(hostInfo, hosts, attack):
    for i in range(len(hosts)):
        defineHostInfo(hosts[i], attack[i])

def isArray(value):
    if isinstance(value, list):
        return True
    return False

def checkResponse(payload):
    if "HTTP" in payload['Method'] or payload['Method'] == '':
        return True
    return False

def parseHost(payload):
    # Host를 파싱하여 반환합니다.
    if "Host" in payload:
        return payload['Host']

    if "dstIp" in payload:
        return payload['dstIP']

def parseContentType(payload):
    # Content-Type을 파싱하여 반환합니다.
    if 'Content-Type' in payload:
        return payload['Content-Type']
    return ''

def parseMethod(payload):
    return payload['Method']

def checkGET(payload):
    # GET Method인지 확인합니다.
    if parseMethod(payload) == 'GET':
        return True

    contentType = parseContentType(payload)

    if contentType == '':
        return True
    return False

def checkPOST(payload):
    # POST Method인지 확인합니다.
    if parseMethod(payload) == 'POST':
        return True

    if 'Content-Type' not in payload:
        return False

    contentType = parseContentType(payload)

    if contentType == 'application/x-www-form-urlencoded':
        return True
    return False

def checkSQL(data):
    # SQL인지 확인합니다. 인자는 GET 파라미터 or POST의 body입니다.
    # SQL은 대/소문자 구분이 없으므로 data를 소문자로 만들어 검사합니다.
    sqlPatterns = ['select', 'union', 'update', 'insert', 'delete', 'drop', 'group_concat', 'database()', 'information_schema', 'sleep', 'benchmark', 'or', 'and', '--', 'order']
    sqlPatterns.append('||') # Javascript와 혼동이 발생할 수도 있지만 다른 방안이 생각 안나서 우선 사용하였습니다.
    sqlPatterns.append('&&') # Javascript와 혼동이 발생할 수도 있지만 다른 방안이 생각 안나서 우선 사용하였습니다.

    if isArray(data):
        # GET 파라미터라 배열인 경우 각 인자의 value로 확인합니다.
        for i in range(len(data)):
            tmp = data[i]['value'].lower()
            for sqlPattern in sqlPatterns:
                if tmp.find(sqlPattern) != -1:
                    return True
        return False

    else:
        data = data.lower()
        for sqlPattern in sqlPatterns:
            if data.find(sqlPattern) != -1:
                return True
        return False


def checkJS(data):
    # javascript인지 확인합니다. 인자는 GET 파라미터 or POST의 body입니다.
    jsPatterns = ['location.href', 'document.cookie', 'alert', '<script>', '</script>', 'fromCharCode', 'javascript:']

    if isArray(data):
        # GET 파라미터라 배열인 경우 각 인자의 value로 확인합니다.
        for i in range(len(data)):
            tmp = data[i]['value']
            for jsPattern in jsPatterns:
                if tmp.find(jsPattern) != -1:
                    return True
        return False

    for jsPattern in jsPatterns:
        if data.find(jsPattern) != -1:
            return True
    return False

def checkTag(body):
    # php인지 확인합니다.
    if body.find('<?php') != -1 and body.find('?>'):
        return 'PHP'

    if body.find('<?') != -1 and body.find('?>'):
        return 'PHP'

    if body.find('<?=') != -1 and body.find('?>'):
        return 'PHP'

    # jsp인지 확인합니다.
    if body.find('<%=') != -1 and body.find('%>'):
        return 'JSP'

    if body.find('<%!') != -1 and body.find('%>'):
        return 'JSP'

    # asp인지 확인합니다.
    if body.find('<%') != -1 and body.find('%>'):
        # <% %> 는 jsp와 asp에서 공통으로 나타나므로 ;를 확인합니다.
        # ;가 있다면 jsp이며 없다면 asp입니다. 지금은 단순히 ;가 존재하는지로 판단합니다.
        if body.find(';') == -1:
            return 'ASP'
        return 'JSP'

    return ''

def checkFunction(body):
    # 태그로 확인하지 못했다면 고유 함수로 확인합니다.
    phpFunctions = ['phpinfo', 'shell_exec', 'popen', 'passthru']
    jspFunctions = ['runtime.getruntime()', 'getruntime', 'runtime']
    aspFunctions = ['createobject', 'run(', 'eval request(', 'execute request(']

    for phpFunction in phpFunctions:
        if body.find(phpFunction) != -1:
            return 'PHP'

    for jspFunction in jspFunctions:
        if body.find(jspFunction) != -1:
            return 'JSP'

    for aspFunction in aspFunctions:
        if body.find(aspFunction) != -1:
            return 'ASP'

def classifyAttack(host):
    # 만약 정의되지 않은 host라면 attackType은 'unknown'입니다.
    if host not in hostInfo['host']:
        return 'unknown'

    # host를 처음부터 비교하며 host에 맞는 공격 유형을 return 합니다.
    for i in range(len(hostInfo['host'])):
        if host == hostInfo['host'][i]:
            return hostInfo['attack'][i]

    # 예외 발생 시 error를 반환합니다.
    return 'error'

def parseBoundary(contentType):
    if contentType.find('boundary=') != -1:
        return contentType.split('boundary=')[1]
    return ''

def parseFormData(payload):
    contentType = parseContentType(payload)
    boundary = parseBoundary(contentType)
    data = payload['Data'].replace('--' + boundary, '').replace('--\r\n', '')
    data = data.split('\r\n\r\n')
    result = []
    for i in range(0, len(data), 2):
        argument = {'name' : '', 'value' : ''}
        argument['name'] = data[i].split('name=')[1][1:-1]
        argument['value'] = urllib.parse.unquote(data[i + 1])
        result.append(argument)

    return result

def parseParameter(payload, method):
    if method == 'GET':
        # Method가 GET이라면 각 인자를 가공하여 반환합니다.
        result = []

        # Method가 GET이지만 인자가 없는 경우 빈 배열을 반환합니다.
        if payload['URL'].find('?') == -1:
            return result

        data = payload['URL'].split('?')[1]
        parameters = data.split('&')

        for parameter in parameters:
            argument = {'name' : '', 'value' : ''}
            argument['name'] = parameter.split('=')[0]
            parse = urllib.parse.parse_qsl(parameter)
            if parse == []:
                argument['value'] = ''
            else:
                argument['value'] = parse[0][1]
            result.append(argument)

        return result

    if method == 'POST':
        # Method가 POST라면 body를 반환합니다.
        # form-data 형식이라면 form을 파싱하여 반환합니다.
        if "multipart/form-data" in parseContentType(payload):
            return parseFormData(payload)

        if 'body' in payload:
            return payload['body']

        if 'Data' in payload:
            return payload['Data']
        return ''



def classifyUploadLanguage(payload):
    if "body" not in payload:
            return 'unknown'

    body = parseParameter(payload, "POST")
    tagResult = checkTag(body)
    if tagResult != '':
        return tagResult

    functionResult = checkFunction(body)
    if functionResult != '':
        return functionResult

    return 'unknown'

def classifyLanguage(payload, attackType):
    # 만약 공격 유형이 unknown이라면 language도 unknown입니다.
    if attackType == 'unknown':
        return 'unknown'

    if attackType == 'SQLI':
        return 'SQL'

    if attackType == 'XSS':
        return 'JS'

    if attackType == 'FileUpload':
        language = classifyUploadLanguage(payload)
        #language = 'PHP'
        return language

def classify(payload):
    # 결과를 반환할 변수이며 {'lang' : 'SQL', 'attackType' : 'SQLI'}와 같은 형태로 반환됩니다.
    result = {'lang' : '', 'attackType' : ''}

    # hostInfo 변수를 정의합니다.
    initHostInfo(hostInfo, hosts, attack)

    # host를 파싱하여 공격을 분류합니다.
    host = parseHost(payload)
    result['attackType'] = classifyAttack(host)

    # attackType으로 언어를 정의합니다.
    result['lang'] = classifyLanguage(payload, result['attackType'])

    return result

def newClassifyAttack(language):
    # 언어를 판단하지 못했다면 공격 유형도 'unknown' 입니다.
    if language == 'unknown':
        return 'unknown'

    # 언어가 SQL이라면 공격 유형은 SQL Injection입니다.
    if language == 'SQL':
        return 'SQLI'

    # 언어가 Java Script라면 공격 유형은 XSS입니다.
    if language == 'JS':
        return 'XSS'

    # 앞서 분류되지 않았다면 공격 유형은 File Upload입니다.
    return 'FileUpload'

def newClassifyLanguage(payload):
    if checkGET(payload):
        # GET 파라미터로 SQL or XSS를 판단합니다.
        parameter = parseParameter(payload, "GET")
        if checkSQL(parameter):
            return 'SQL'

        if checkJS(parameter):
            return 'JS'

        return 'unknown'    # 판단 실패 시 'unknown'을 반환합니다.

    elif checkPOST(payload):
        # POST 파라미터로 SQL or XSS를 판단합니다.
        parameter = parseParameter(payload, "POST")

        if checkSQL(parameter):
            return 'SQL'

        if checkJS(parameter):
            return 'JS'

        return 'unknown'    # 판단 실패 시 'unknown'을 반환합니다.

    return classifyUploadLanguage(payload)

def newClassify(payload):
    result = {'lang' : '', 'attackType' : ''}

    # Response 패킷을 처리합니다.
    if checkResponse(payload):
        result['lang'] = "RESPONSE"
        result['attackType'] = "NONE"
        return result

    result['lang'] = newClassifyLanguage(payload)
    result['attackType'] = newClassifyAttack(result['lang'])

    return result
