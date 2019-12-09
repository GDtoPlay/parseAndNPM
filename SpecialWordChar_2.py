# -*- coding: utf-8 -*-
# Author : Jin Kim
# e-mail : jinkim@seculayer.co.kr
# Powered by Seculayer © 2017-2018 AI Core Team, Intelligence R&D Center.
######################################################################################
###### import modules ######
### python basic
import re
import urllib.parse as decode
from operator import itemgetter

### MLPS
#from apeflow_test.data_generator.ConvertAbstract import ConvertAbstract

######################################################################################
# class : SpecialWordChar_2
SWupper_arr = [
        ['ZGlzcGF0Y2hlci5IdHRwU2VydmxldFJlcXVlc3Q'],['amF2YS5sYW5nLlByb2Nlc3NCdWlsZGVy'],['amF2YS5pby5JbnB1dFN0cmVhbVJlYWRlcg'],['amF2YS5pby5GaWxlT3V0cHV0U3RyZWFt'],
        ['amF2YS5pby5CdWZmZXJlZFdyaXRlcg'],['ZGlzcGF0Y2hlci5IdHRwU2VydmxldFJlc3BvbnNl'],['aWZjb25maWc'],['bmV0c3RhdCAt'],['cHMgLQ'],['bHNtb2Qg'],['bmV0c3RhdCA'],
        ['ZGYg'],['dGNwZHVtcCA'],['cGVybCA'],['d2dldCA'],['YmFzaCA'],['Y2Qg'],['dm1zdGF0IA'],['bHNvZiA'],['Zgly'],['ZWNobyA'],['bmMgLQ'],['cGluZyA'],['c2h1dGRvd24g'],
        ['a2lsbCA'],['dW5hbWUg'],['cHdk'],['bWtkaXIg'],['cm0gLQ'],['dmkg'],['bXYg'],['Y2htb2Qg'],['dG91Y2gg'],['bHMg'],['Y2F0IA'],['Y2F0Pg'],['c3UgLQ'],['d2hvYW1p'],
        ['dG9wIC0'],['ZGF0ZQ'],['cGFzc3dk'],['c3R0eSA'],['cm1kaXIg'],['bG4g'],['Y3Ag'],['Y2hvd24g'],['Y2hncnAg'],['dW1hc2sg'],['bW9yZSA'],['aGVhZCA'],
        ['dGFpbCA'],['d2Mg'],['Y3V0IA'],['c29ydCA'],['c3BsaXQg'],['Z3JlcCA'],['ZmluZCA']
      ]

class SpecialWordChar_1:#ConvertAbstract):
    def __init__(self, max_len, preprocessing_type):
      self.max_len = max_len
      self.preprocessing_type = preprocessing_type

      SWtoken_Arr = [
      [ # Basic
        ['alert', 'a', 0], ['alter', 'b', 0], ['and', 'c', 0], ['between', 'd', 0], ['cmd', 'e', 0],
        ['commit', 'f', 0], ['count', 'g', 0], ['exec', 'h', 0], ['from', 'i', 0], ['href', 'j', 0],
        ['insert', 'k', 0], ['into', 'l', 0], ['objectclass', 'm', 0], ['onmouseover', 'n', 0],
        ['script', 'o', 0], ['select', 'p', 0], ['shell', 'q', 0], ['table', 'r', 0], ['union', 's', 0],
        ['upper', 't', 0], ['or', 'u', 0], ['order', 'v', 0], ['passwd', 'w', 0], ['password', 'x', 0],
        ['where', 'y', 0], ['winnt', 'z', 0], ['onload', 'A', 0], ['cookie', 'B', 0], ['phpmyadmin', 'C', 0],
        ['wget', 'D', 0], ['curl', 'E', 0],
        #######################
        ['accept :', 'F', 0], ['0 %', 'G', 0], ['% 0a', 'H', 0], ['/ c', 'I', 0], ['cn =', 'J', 0],
        ['= - craw', 'K', 0], ['document . cookie', 'L', 0], ['etc / passwd', 'M', 0], ['# include', 'N', 0],
        ['javascript :', 'O', 0], ['mail =', 'P', 0], ['path / child', 'Q', 0], ['url =', 'R', 0],
        ['user - agent', 'S', 0], ['content - type', 'T', 0], ['information - schema', 'U', 0],
        ['bash _ history', 'V', 0],
      ],
      [  # FD
        ['etc', 'A', 0], ['opt', 'A', 0], ['proc', 'A', 0], ['root', 'A', 0], ['usr', 'A', 0],
        ['var', 'B', 0], ['inetpub', 'B', 0], ['recycle', 'B', 0], ['apache', 'B', 0], ['documents', 'B', 0],
        ['and', 'C', 0], ['settings', 'C', 0], ['home', 'C', 0], ['log', 'C', 0], ['logs', 'C', 0],
        ['minint', 'D', 0], ['mysql', 'D', 0], ['nginx', 'D', 0], ['php', 'D', 0], ['program', 'D', 0],
        ['files', 'E', 0], ['programfiles', 'E', 0], ['sysprep', 'E', 0], ['system', 'E', 0],
        ['volume', 'E', 0],
        ['information', 'F', 0], ['users', 'F', 0], ['wamp', 'F', 0], ['windows', 'F', 0], ['winnt', 'F', 0],
        ['xampp', 'G', 0], ['web', 'G', 0], ['inf', 'G', 0], ['config', 'G', 0], ['include', 'G', 0],
        ['inc', 'H', 0], ['sites', 'H', 0], ['phpmyadmin', 'H', 0], ['jeus', 'H', 0], ['library', 'H', 0],
        ['private', 'I', 0], ['httpd', 'I', 0], ['init', 'I', 0], ['lampp', 'I', 0], ['lamp', 'I', 0],
        ['self', 'J', 0], ['ssh', 'J', 0], ['local', 'J', 0], ['sysconfig', 'J', 0], ['administrator', 'J', 0],
        ['bin', 'K', 0], ['wwwroot', 'K', 0], ['smsosd', 'K', 0], ['data', 'K', 0], ['conf', 'K', 0],
        ['apache', 'L', 0], ['group', 'L', 0], ['apachegroup', 'L', 0], ['apache', 'L', 0],
        ['software', 'L', 0],
        ['foundation', 'M', 0], ['filezilla', 'M', 0], ['server', 'M', 0], ['inetsrv', 'M', 0],
        ['debug', 'M', 0],
        ['panther', 'N', 0], ['repair', 'N', 0], ['filezillaftp', 'N', 0], ['mercurymail', 'N', 0],
        ['sendmail', 'O', 0], ['tomcat', 'O', 0], ['webalizer', 'O', 0], ['webdav', 'O', 0],
        ['plugins', 'O', 0],
        ['defaults', 'P', 0], ['webserver', 'P', 0], ['sites', 'P', 0], ['available', 'P', 0],
        ['desktop', 'P', 0],
        ['stable', 'Q', 0], ['osdlogs', 'Q', 0], ['mysql', 'Q', 0], ['unattend', 'Q', 0], ['drivers', 'Q', 0],
        ['documents', 'R', 0], ['htdocs', 'R', 0], ['regback', 'R', 0], ['httperr', 'R', 0], ['extra', 'R', 0],
        ['schema', 'S', 0], ['passwd', 'S', 0],
        ###########################
        ['vhosts', 'T', 0], ['grub', 'T', 0], ['mkuser', 'T', 0], ['config', 'T', 0], ['passwd', 'T', 0],
        ['group', 'U', 0], ['hosts', 'U', 0], ['motd', 'U', 0], ['issue', 'U', 0], ['bashrc', 'U', 0],
        ['nginx', 'V', 0], ['boot', 'V', 0], ['version', 'V', 0], ['cmdline', 'V', 0], ['mounts', 'V', 0],
        ['host', 'W', 0], ['fstab', 'W', 0], ['sysprep', 'W', 0], ['unattended', 'W', 0], ['unattend', 'W', 0],
        ['shadow', 'X', 0], ['profile', 'X', 0], ['interrupts', 'X', 0], ['cpuinfo', 'X', 0],
        ['meminfo', 'X', 0],
        ['services', 'Y', 0], ['security', 'Y', 0], ['shells', 'Y', 0], ['resolv', 'Y', 0], ['fastab', 'Y', 0],
        ['login', 'Z', 0], ['ftproot', 'Z', 0], ['access', 'Z', 0], ['error', 'Z', 0], ['apache', 'Z', 0],
        ['systeminit', 'a', 0], ['robots', 'a', 0], ['humans', 'a', 0], ['style', 'a', 0],
        ['configuration', 'a', 0],
        ['wp', 'b', 0], ['login', 'b', 0], ['wp', 'b', 0], ['admin', 'b', 0], ['wp', 'b', 0],
        ['content', 'b', 0],
        ['my', 'c', 0], ['php', 'c', 0], ['sessions', 'c', 0], ['server', 'c', 0], ['local', 'c', 0],
        ['wpsettings', 'd', 0], ['explorer', 'd', 0], ['iis', 'd', 0], ['notepad', 'd', 0], ['system', 'd', 0],
        ['temp', 'e', 0], ['windowsupdate', 'e', 0], ['win', 'e', 0], ['weblogic', 'e', 0], ['mysql', 'e', 0],
        ['changelog', 'f', 0], ['properties', 'f', 0], ['mercury', 'f', 0], ['phpinfo', 'f', 0],
        ['sendmail', 'g', 0], ['webalizer', 'g', 0], ['webdav', 'g', 0], ['settings', 'g', 0],
        ['httpd', 'g', 0],
        ['sam', 'h', 0], ['software', 'h', 0], ['eula', 'h', 0], ['license', 'h', 0],
        ['sysprepsysprep', 'h', 0],
        ['sysprepunattended', 'i', 0], ['sysprepunattend', 'i', 0], ['index', 'i', 0], ['apachectl', 'i', 0],
        ['hostname', 'j', 0], ['mysql', 'j', 0], ['bin', 'j', 0], ['default', 'j', 0],
        ['applicationhost', 'j', 0],
        ['httperr', 'k', 0], ['aspnet', 'k', 0], ['schema', 'k', 0], ['ports', 'k', 0], ['httpd', 'k', 0],
        ['ssl', 'l', 0], ['desktop', 'l', 0], ['variables', 'l', 0], ['setupinfo', 'l', 0],
        ['appevent', 'l', 0],
        ['secevent', 'm', 0], ['tomcat', 'm', 0], ['users', 'm', 0], ['web', 'm', 0], ['appstore', 'm', 0],
        ['metabase', 'n', 0], ['netsetup', 'n', 0], ['conf', 'n', 0], ['environ', 'n', 0],
        ['authorized', 'n', 0],
        ['keys', 'o', 0], ['id', 'o', 0], ['rsa', 'o', 0], ['known', 'o', 0], ['hosts', 'o', 0],
        ['network', 'p', 0], ['ntuser', 'p', 0], ['logfiles', 'p', 0], ['global', 'p', 0], ['history', 'p', 0],
        ['htpasswd', 'q', 0], ['bash', 'q', 0], ['history', 'q', 0], ['my', 'q', 0],
        ##############################
        ['d', 'r', 0], ['conf', 'r', 0], ['default', 'r', 0], ['wsconfig', 'r', 0], ['ini', 'r', 0],
        ['gz', 'r', 0],
        ['bashrc', 's', 0], ['inf', 's', 0], ['txt', 's', 0], ['xml', 's', 0], ['defs', 's', 0],
        ['log', 's', 0],
        ['dat', 't', 0], ['css', 't', 0], ['php', 't', 0], ['cnf', 't', 0], ['exe', 't', 0], ['inc', 't', 0],
        ['rtf', 'u', 0], ['html', 'u', 0], ['err', 'u', 0], ['confetc', 'u', 0], ['config', 'u', 0],
        ['bak', 'v', 0], ['evt', 'v', 0], ['sav', 'v', 0], ['sa', 'v', 0], ['keystore', 'v', 0],
        ['pub', 'v', 0],
        ['asa', 'w', 0], ['asp', 'w', 0]
      ],
      [  # FUP
        ['zorback', 'A', 0], ['h4x0r', 'A', 0], ['awen', 'A', 0], ['perlkit', 'A', 0], ['darkraver', 'A', 0],
        ['carbylamine', 'B', 0], ['c99madshell', 'B', 0], ['azrail', 'B', 0], ['aspyqanalyser', 'B', 0],
        ['aspxspy', 'C', 0], ['asmodeus', 'C', 0], ['antichat', 'C', 0], ['aventgrup', 'C', 0],
        ['ru24postwebshell', 'D', 0], ['jspspy', 'D', 0], ['h4ntu', 'D', 0], ['entrika', 'D', 0],
        ['xiangxilianjie', 'E', 0], ['sqlrootkit', 'E', 0], ['kingdefacer', 'E', 0], ['lotfree', 'E', 0],
        ['backdoor', 'F', 0], ['bythehacker', 'F', 0], ['c99shell', 'F', 0], ['knull', 'F', 0],
        ['hackart', 'F', 0],
        ['ru24postwebshell', 'G', 0], ['phpwebshell', 'G', 0], ['rootshell', 'G', 0], ['nullshell', 'G', 0],
        ['aspshell', 'H', 0], ['myshell', 'H', 0], ['wshshell', 'H', 0], ['kcwebtelnet', 'H', 0],
        ['r57shell', 'I', 0], ['jspwebshell', 'I', 0],
        ##################
        ['shell', 'J', 0], ['exec', 'J', 0], ['passthru', 'J', 0], ['system', 'J', 0], ['popen', 'J', 0],
        ['eval', 'K', 0], ['command', 'K', 0], ['base64', 'K', 0], ['getparameter', 'K', 0], ['echo', 'K', 0],
        ['execl', 'L', 0], ['bin', 'L', 0], ['sh', 'L', 0], ['gzinflate', 'L', 0], ['decode', 'L', 0],
        ['uname', 'M', 0], ['execute', 'M', 0], ['createtextfile', 'M', 0], ['createobject', 'M', 0],
        ['phpremoteview', 'N', 0], ['fileoutputstream', 'N', 0], ['executecommand', 'N', 0],
        ['htmlencode', 'N', 0],
        ['getruntime', 'O', 0], ['runtime', 'O', 0], ['unzip', 'O', 0], ['mkdirs', 'O', 0],
        ['fileinputstream', 'P', 0], ['getabsolutepath', 'P', 0], ['replace', 'P', 0], ['function', 'P', 0],
        ['method', 'Q', 0], ['preg', 'Q', 0], ['str', 'Q', 0], ['base64decoder', 'Q', 0],
        ['decodebuffer', 'Q', 0],
        ['language', 'R', 0], ['filename', 'R', 0], ['filepath', 'R', 0], ['file', 'R', 0], ['name', 'R', 0],
        ['encode', 'S', 0], ['realpath', 'S', 0], ['formbase64string', 'S', 0], ['filesystemobject', 'S', 0],
        ['phpinfo', 'T', 0], ['getenv', 'T', 0], ['processbuilder', 'T', 0], ['popupmanagefile', 'T', 0],
        ['rot', 'U', 0], ['action', 'U', 0], ['curl', 'U', 0],
        #####################
        ['php', 'V', 0], ['asp', 'V', 0], ['jsp', 'V', 0], ['asa', 'V', 0], ['cdx', 'V', 0], ['war', 'V', 0],
        ['aspx', 'W', 0], ['zip', 'W', 0], ['cgi', 'W', 0], ['png', 'W', 0], ['gif', 'W', 0], ['jpeg', 'W', 0],
        ['exe', 'W', 0],
        ######################
        ['get', 'X', 0], ['post', 'X', 0], ['http', 'X', 0], ['title', 'X', 0], ['vbscript', 'X', 0],
        ['upload', 'Y', 0], ['upfile', 'Y', 0], ['uploads', 'Y', 0], ['popupfile', 'Y', 0], ['run', 'Y', 0],
        ['request', 'Z', 0], ['response', 'Z', 0], ['content', 'Z', 0], ['form', 'Z', 0], ['data', 'Z', 0],
        ['type', 'a', 0], ['encoding', 'a', 0], ['bytes', 'a', 0], ['filemanager', 'a', 0],
        ['uploadimage', 'a', 0],
        ['fileuploader', 'a', 0]
      ],
      [  # RCE
        ['memberaccess', 'A', 0], ['getsession', 'A', 0], ['getservletcontext', 'A', 0],
        ['getrealpath', 'A', 0],
        ['xmldatasource', 'B', 0], ['objectname', 'B', 0], ['management', 'B', 0], ['io', 'B', 0],
        ['fileoutputstream', 'C', 0], ['bufferedwriter', 'C', 0], ['dispatcher', 'C', 0],
        ['httpservletresponse', 'D', 0], ['lang', 'D', 0], ['runtime', 'D', 0], ['getruntime', 'D', 0],
        ['savegangster', 'E', 0], ['zglzcgf0y2hlci5idhrwu2vydmxldfjlcxvlc3q', 'E', 0],
        ['amf2ys5syw5nllbyb2nlc3ncdwlszgvy', 'F', 0], ['amf2ys5pby5jbnb1dfn0cmvhbvjlywrlcg', 'F', 0],
        ['inputstreamreader', 'G', 0], ['amf2ys5pby5gawxlt3v0chv0u3ryzwft', 'G', 0],
        ['amf2ys5pby5cdwzmzxjlzfdyaxrlcg', 'H', 0], ['zglzcgf0y2hlci5idhrwu2vydmxldfjlc3bvbnnl', 'H', 0],
        ['processbuilder', 'I', 0], ['allowstaticmethodaccess', 'I', 0], ['servletactioncontext', 'I', 0],
        ['methodaccessor', 'J', 0], ['denymethodexecution', 'J', 0], ['redirectaction', 'J', 0],
        ['ognlcontext', 'K', 0], ['memberacess', 'K', 0], ['redirect', 'K', 0], ['action', 'K', 0],
        ['annotationinvocationhandler', 'L', 0], ['annotation', 'L', 0], ['reflect', 'L', 0], ['class', 'L', 0],
        ['classloader', 'M', 0], ['xwork', 'M', 0], ['ognlutil', 'M', 0], ['redirecterrorstream', 'M', 0],
        ['setmemberaccess', 'N', 0], ['getinstance', 'N', 0], ['actioncontext', 'N', 0],
        ['getexcludedpackagenames', 'O', 0], ['getexcludedclasses', 'O', 0], ['getinputstream', 'O', 0],
        ['getwriter', 'P', 0], ['workcontext', 'P', 0], ['xmldecoder', 'P', 0], ['println', 'P', 0],
        ['unmarshaller', 'Q', 0], ['allowpackageprotectedaccess', 'Q', 0], ['allowprotectedaccess', 'Q', 0],
        ['allowprivateaccess', 'R', 0], ['excludedpackagenamepatterns', 'R', 0], ['excludedclasses', 'R', 0],
        ['invokeuq', 'S', 0], ['getruntimeur', 'S', 0], ['getmethoduq', 'S', 0],
        ['constanttransformerxv', 'S', 0],
        ['invokertransformer', 'T', 0], ['imethodnamet', 'T', 0], ['annotationinvocationhandleru', 'T', 0],
        ['invocationhandler', 'U', 0], ['runtimexpsr', 'U', 0], ['objectxpvq', 'U', 0], ['invoker', 'U', 0],
        ['createobject', 'U', 0],
        ######################################
        ['netstat', 'V', 0], ['uname', 'V', 0], ['ipconfig', 'V', 0], ['cmd', 'V', 0], ['root', 'V', 0],
        ['exe', 'W', 0], ['awzjb25mawc', 'W', 0], ['bmv0c3rhdcat', 'W', 0], ['exec', 'W', 0], ['dir', 'W', 0],
        ['rm', 'X', 0], ['rf', 'X', 0], ['mkdir', 'X', 0], ['ls', 'X', 0], ['ifconfig', 'X', 0],
        ['chmglq', 'Y', 0], ['bhntb2qg', 'Y', 0], ['bmv0c3rhdca', 'Y', 0], ['zgyg', 'Y', 0],
        ['dgnwzhvtcca', 'Z', 0], ['cgvybca', 'Z', 0], ['d2dldca', 'Z', 0], ['ymfzaca', 'Z', 0],
        ['y2qg', 'Z', 0],
        ['dm1zdgf0ia', 'a', 0], ['bhnvzia', 'a', 0], ['zgly', 'a', 0], ['zwnobya', 'a', 0], ['bmmglq', 'a', 0],
        ['cgluzya', 'b', 0], ['c2h1dgrvd24g', 'b', 0], ['a2lsbca', 'b', 0], ['dw5hbwug', 'b', 0],
        ['chdk', 'b', 0],
        ['bwtkaxig', 'c', 0], ['cm0glq', 'c', 0], ['dmkg', 'c', 0], ['bxyg', 'c', 0], ['y2htb2qg', 'c', 0],
        ['dg91y2gg', 'd', 0], ['bhmg', 'd', 0], ['y2f0ia', 'd', 0], ['y2f0pg', 'd', 0], ['c3uglq', 'd', 0],
        ['d2hvyw1p', 'e', 0], ['dg9wic0', 'e', 0], ['zgf0zq', 'e', 0], ['cgfzc3dk', 'e', 0],
        ['c3r0esa', 'e', 0],
        ['cm1kaxig', 'f', 0], ['bg4g', 'f', 0], ['y3ag', 'f', 0], ['y2hvd24g', 'f', 0], ['y2hncnag', 'f', 0],
        ['dw1hc2sg', 'g', 0], ['bw9yzsa', 'g', 0], ['agvhzca', 'g', 0], ['dgfpbca', 'g', 0], ['d2mg', 'g', 0],
        ['y3v0ia', 'h', 0], ['c29ydca', 'h', 0], ['c3bsaxqg', 'h', 0], ['z3jlcca', 'h', 0], ['zmluzca', 'h', 0],
        ['wget', 'i', 0], ['powershell', 'i', 0], ['curl', 'i', 0], ['nslookup', 'i', 0],
        #####################
        ['exefile', 'j', 0], ['jexws4', 'j', 0], ['singlesaints', 'j', 0], ['gry', 'j', 0], ['struts2', 'j', 0],
        ['showcase', 'k', 0], ['apache', 'k', 0], ['sun', 'k', 0], ['ognl', 'k', 0], ['soapenv', 'k', 0],
        ['member', 'l', 0], ['access', 'l', 0], ['acunetix', 'l', 0], ['soap', 'l', 0], ['javax', 'l', 0],
        ['java', 'm', 0], ['envelope', 'm', 0], ['method', 'm', 0], ['command', 'm', 0], ['xmlsoap', 'm', 0],
        ['sr', 'n', 0], ['sh', 'n', 0], ['coordinatorporttype', 'n', 0], ['appscan', 'n', 0],
        ['spider', 'n', 0],
        ########################################
        ['propfind', 'o', 0], ['content', 'o', 0], ['length', 'o', 0], ['head', 'o', 0], ['post', 'o', 0],
        ['get', 'p', 0], ['type', 'p', 0], ['user', 'p', 0], ['agent', 'p', 0], ['accept', 'p', 0],
        ['cookie', 'q', 0], ['prohibited', 'q', 0]
      ],
      [  # SQL
        ['case', 'A', 0], ['by', 'A', 0], ['all', 'A', 0], ['char', 'A', 0], ['character', 'A', 0],
        ['chr', 'B', 0], ['column', 'B', 0], ['concat', 'B', 0], ['convert', 'B', 0], ['count', 'B', 0],
        ['create', 'C', 0], ['declare', 'C', 0], ['delete', 'C', 0], ['distinct', 'C', 0], ['drop', 'C', 0],
        ['from', 'D', 0], ['function', 'D', 0], ['group', 'D', 0], ['having', 'D', 0], ['if', 'D', 0],
        ['ifnull', 'E', 0], ['insert', 'E', 0], ['into', 'E', 0], ['like', 'E', 0], ['limit', 'E', 0],
        ['or', 'F', 0], ['and', 'F', 0], ['order', 'F', 0], ['select', 'F', 0], ['union', 'F', 0],
        ['update', 'G', 0], ['when', 'G', 0], ['where', 'G', 0], ['grant', 'G', 0],
        #######################
        ['address', 'H', 0], ['data', 'H', 0], ['database', 'H', 0], ['dba', 'H', 0], ['etc', 'H', 0],
        ['file', 'I', 0], ['filename', 'I', 0], ['id', 'I', 0], ['name', 'I', 0], ['passwd', 'I', 0],
        ['password', 'J', 0], ['pg', 'J', 0], ['pwd', 'J', 0], ['resource', 'J', 0], ['sys', 'J', 0],
        ['system', 'K', 0], ['table', 'K', 0], ['tablename', 'K', 0], ['tables', 'K', 0], ['uid', 'K', 0],
        ['user', 'L', 0], ['username', 'L', 0], ['users', 'L', 0], ['utl', 'L', 0], ['value', 'L', 0],
        ['values', 'M', 0], ['version', 'M', 0], ['schema', 'M', 0], ['information', 'M', 0],
        ['inaddr', 'M', 0],
        ['admin', 'M', 0],
        #############################
        ['cmd', 'N', 0], ['cmdshell', 'N', 0], ['echo', 'N', 0], ['exe', 'N', 0], ['exec', 'N', 0],
        ['shell', 'O', 0], ['master', 'O', 0], ['xp', 'O', 0], ['sp', 'O', 0], ['regdelete', 'O', 0],
        ['availablemedia', 'P', 0], ['terminate', 'P', 0], ['regwrite', 'P', 0],
        ['regremovemultistring', 'P', 0],
        ['regread', 'Q', 0], ['regenumvalues', 'Q', 0], ['regenumkeys', 'Q', 0], ['regenumbalues', 'Q', 0],
        ['regdeletevalue', 'R', 0], ['regdeletekey', 'R', 0], ['regaddmultistring', 'R', 0], ['ntsec', 'R', 0],
        ['makecab', 'S', 0], ['loginconfig', 'S', 0], ['enumdsn', 'S', 0], ['filelist', 'S', 0],
        ['execresultset', 'T', 0], ['dirtree', 'T', 0], ['cmdshell', 'T', 0], ['reg', 'T', 0],
        ['servicecontrol', 'U', 0], ['webserver', 'U', 0],
        ############################
        ['decode', 'V', 0], ['default', 'V', 0], ['delay', 'V', 0], ['document', 'V', 0], ['eval', 'V', 0],
        ['getmappingxpath', 'W', 0], ['hex', 'W', 0], ['is', 'W', 0], ['login', 'W', 0], ['match', 'W', 0],
        ['not', 'X', 0], ['null', 'X', 0], ['request', 'X', 0], ['sets', 'X', 0], ['to', 'X', 0],
        ['var', 'Y', 0], ['varchar', 'Y', 0], ['waitfor', 'Y', 0], ['desc', 'Y', 0], ['connect', 'Y', 0],
        ['as', 'Z', 0], ['int', 'Z', 0], ['log', 'Z', 0], ['cast', 'Z', 0], ['rand', 'Z', 0], ['sleep', 'Z', 0],
        ['substring', 'a', 0], ['replace', 'a', 0], ['benchmark', 'a', 0], ['md', 'a', 0],
        #######################
        ['content', 'b', 0], ['cookie', 'b', 0], ['dbms', 'b', 0], ['db', 'b', 0], ['dir', 'b', 0],
        ['get', 'c', 0], ['http', 'c', 0], ['mysql', 'c', 0], ['oracle', 'c', 0], ['post', 'c', 0],
        ['query', 'd', 0], ['referer', 'd', 0], ['sql', 'd', 0], ['sqlmap', 'd', 0]
      ],
      [  # UAA
        ['myadmin', 'A', 0], ['manager', 'A', 0], ['admin', 'A', 0], ['wp', 'A', 0], ['saedit', 'A', 0],
        ['config', 'B', 0], ['funcspecs', 'B', 0], ['scripts', 'B', 0], ['server', 'B', 0], ['center', 'B', 0],
        ['tomcat', 'C', 0], ['pma', 'C', 0], ['transfer', 'C', 0], ['console', 'C', 0], ['vti', 'C', 0],
        ['acensus', 'D', 0], ['openapi', 'D', 0], ['jmx', 'D', 0], ['web', 'D', 0], ['conf', 'D', 0],
        ['servlet', 'E', 0], ['export', 'E', 0], ['cs', 'E', 0], ['db', 'E', 0], ['changelog', 'E', 0],
        ['status', 'F', 0], ['login', 'F', 0], ['setup', 'F', 0], ['info', 'F', 0], ['join', 'F', 0],
        ['encoding', 'G', 0], ['bin', 'G', 0], ['security', 'G', 0], ['empappupdtlogin', 'G', 0],
        ['content', 'H', 0], ['spmgr', 'H', 0], ['sap', 'H', 0], ['rd', 'H', 0], ['log', 'H', 0],
        ['details', 'I', 0], ['howto', 'I', 0], ['inc', 'I', 0], ['index', 'I', 0], ['check', 'I', 0],
        ['loginform', 'J', 0], ['service', 'J', 0], ['user', 'J', 0], ['plugins', 'J', 0],
        ['properties', 'J', 0],
        ['wsomg', 'K', 0], ['portal', 'K', 0], ['import', 'K', 0], ['gpin', 'K', 0], ['aut', 'K', 0],
        ['rest', 'L', 0], ['dzs', 'L', 0], ['csql', 'L', 0], ['dll', 'L', 0], ['edit', 'L', 0],
        ['view', 'L', 0],
        ['upload', 'M', 0], ['author', 'M', 0], ['resource', 'M', 0], ['zoomsounds', 'M', 0],
        ['phpmyadmin', 'N', 0], ['phpmyadminold', 'N', 0], ['bak', 'N', 0], ['pmapass', 'N', 0],
        ['pmahomme', 'O', 0], ['editor', 'O', 0], ['phpadmin', 'O', 0], ['configuration', 'O', 0],
        ['fckeditor', 'P', 0], ['inf', 'P', 0], ['phpmy', 'P', 0], ['ckfinder', 'P', 0],
        #######################################
        ['rhksflwk', 'Q', 0], ['master', 'Q', 0], ['admin', 'Q', 0], ['manager', 'Q', 0], ['webmaster', 'Q', 0],
        ['root', 'R', 0], ['administrator', 'R', 0], ['administrators', 'R', 0], ['superuser', 'R', 0],
        ['weblogic', 'S', 0], ['guest', 'S', 0], ['test', 'S', 0], ['ftpuser', 'S', 0], ['system', 'S', 0],
        ['scott', 'T', 0], ['tomcat', 'T', 0], ['user', 'T', 0], ['operator', 'T', 0], ['anonymous', 'T', 0],
        ['super', 'U', 0], ['pmauser', 'U', 0], ['mysqladmin', 'U', 0], ['sysmaster', 'U', 0],
        ['dbadmin', 'U', 0],
        ['pmaauth', 'V', 0], ['admindb', 'V', 0], ['administrateur', 'V', 0], ['administrat', 'V', 0],
        ['webmail', 'W', 0], ['adminmaster', 'W', 0], ['phpadmin', 'W', 0], ['testuser', 'W', 0],
        ['rootadmin', 'X', 0], ['adminid', 'X', 0],
        #######################################
        ['root', 'Y', 0], ['administrator', 'Y', 0], ['administrators', 'Y', 0], ['superuser', 'Y', 0],
        ['weblogic', 'Z', 0], ['asdf', 'Z', 0], ['qwer', 'Z', 0], ['test', 'Z', 0], ['passwd', 'Z', 0],
        ['qwerty', 'a', 0], ['password', 'a', 0], ['manager', 'a', 0], ['pass', 'a', 0], ['admin', 'a', 0],
        ['abcd', 'b', 0], ['aaaa', 'b', 0], ['asdfgh', 'b', 0], ['webmaster', 'b', 0], ['webmaste', 'b', 0],
        ['iisadminpwd', 'c', 0], ['asdfg', 'c', 0], ['rootroot', 'c', 0], ['rootpassword', 'c', 0],
        ['asdfasdf', 'd', 0], ['abcdefg', 'd', 0],
        ##########################################
        ['authorization', 'e', 0], ['basic', 'e', 0], ['zmeu', 'e', 0], ['python', 'e', 0], ['cpython', 'e', 0],
        ['scan', 'f', 0], ['testcookie', 'f', 0], ['ehlo', 'f', 0], ['baiduspider', 'f', 0]
      ],
      [  # PT
         ['../', 'A', 0], ['..\\', 'A', 0], ['./', 'A', 0], ['/', 'B', 0] , ['%c0%ae', 'C', 0], ['%c0%af', 'C', 0]
      ], 
      [  # OC
        ['addusers', 'a', 0], ['admodcmd', 'a', 0], ['arp', 'a', 0], ['assoc', 'a', 0], ['attrib', 'a', 0], 
        ['bcdboot', 'a', 0], ['bcdedit', 'a', 0], ['bitsadmin', 'a', 0], ['browstat', 'a', 0], ['cacls', 'a', 0], 
        ['call', 'a', 0], ['certreq', 'a', 0], ['certutil', 'a', 0], ['cd', 'a', 0], ['change', 'a', 0], 
        ['chcp', 'a', 0], ['chkdsk', 'a', 0], ['chkntfs', 'a', 0], ['choice', 'a', 0], ['cipher', 'a', 0], 
        ['cleanmgr', 'a', 0], ['clip', 'a', 0], ['cls', 'a', 0], ['cmd', 'a', 0], ['cmdkey', 'a', 0], 
        ['color', 'a', 0], ['comp', 'a', 0], ['compact', 'a', 0], ['compress', 'a', 0], ['convert', 'a', 0], 
        ['copy', 'a', 0], ['coreinfo', 'a', 0], ['csccmd', 'a', 0], ['csvde', 'a', 0], ['date', 'a', 0], 
        ['defrag', 'a', 0], ['del', 'a', 0], ['delprof', 'a', 0], ['deltree', 'a', 0], ['devcon', 'a', 0], 
        ['dir', 'a', 0], ['diruse', 'a', 0], ['diskpart', 'a', 0], ['diskshadow', 'a', 0], ['diskuse', 'a', 0], 
        ['dism', 'a', 0], ['dnscmd', 'a', 0], ['doskey', 'a', 0], ['driverquery', 'a', 0], ['dsacls', 'a', 0], 
        ['dsadd', 'a', 0], ['dsget', 'a', 0], ['dsquery', 'a', 0], ['dsmod', 'a', 0], ['dsmod-user', 'a', 0], 
        ['dsmod-group', 'a', 0], ['dsmod-computer', 'a', 0], ['dsmove', 'a', 0], ['dsrm', 'a', 0], ['echo', 'a', 0], 
        ['endlocal', 'a', 0], ['eventcreate', 'a', 0], ['exit', 'a', 0], ['expand', 'a', 0], ['explorer', 'a', 0], 
        ['extract', 'a', 0], ['fc', 'a', 0], ['find', 'a', 0], ['findstr', 'a', 0], ['fltmc', 'a', 0], 
        ['for_f', 'a', 0], ['for_cmd', 'a', 0], ['for', 'a', 0], ['forfiles', 'a', 0], ['format', 'a', 0], 
        ['freedisk', 'a', 0], ['fsutil', 'a', 0], ['ftp', 'a', 0], ['ftype', 'a', 0], ['getmac', 'a', 0], 
        ['goto', 'a', 0], ['gpresult', 'a', 0], ['gpupdate', 'a', 0], ['help', 'a', 0], ['hostname', 'a', 0], 
        ['icacls', 'a', 0], ['iexpress', 'a', 0], ['if', 'a', 0], ['ifmember', 'a', 0], ['ipconfig', 'a', 0], 
        ['inuse', 'a', 0], ['label', 'a', 0], ['lgpo', 'a', 0], ['lodctr', 'a', 0], ['logman', 'a', 0], 
        ['logoff', 'a', 0], ['logtime', 'a', 0], ['makecab', 'a', 0], ['mapisend', 'a', 0], ['mbsacli', 'a', 0], 
        ['mem', 'a', 0], ['md', 'a', 0], ['mklink', 'a', 0], ['mode', 'a', 0], ['more', 'a', 0], 
        ['mountvol', 'a', 0], ['move', 'a', 0], ['moveuser', 'a', 0], ['msg', 'a', 0], ['msiexec', 'a', 0], 
        ['msinfo32', 'a', 0], ['mstsc', 'a', 0], ['netdom', 'a', 0], ['netsh', 'a', 0], ['nbtstat', 'a', 0], 
        ['netstat', 'a', 0], ['nltest', 'a', 0], ['now', 'a', 0], ['nslookup', 'a', 0], ['ntbackup', 'a', 0], 
        ['ntdsutil', 'a', 0], ['ntrights', 'a', 0], ['nvspbind', 'a', 0], ['openfiles', 'a', 0], ['path', 'a', 0], 
        ['pathping', 'a', 0], ['pause', 'a', 0], ['perms', 'a', 0], ['monitor', 'a', 0], ['ping', 'a', 0], 
        ['popd', 'a', 0], ['portqry', 'a', 0], ['powercfg', 'a', 0], ['print', 'a', 0], ['printbrm', 'a', 0], 
        ['prncnfg', 'a', 0], ['prnmngr', 'a', 0], ['procdump', 'a', 0], ['prompt', 'a', 0], ['psexec', 'a', 0], 
        ['psfile', 'a', 0], ['psgetsid', 'a', 0], ['psinfo', 'a', 0], ['pskill', 'a', 0], ['pslist', 'a', 0], 
        ['psloggedon', 'a', 0], ['psloglist', 'a', 0], ['pspasswd', 'a', 0], ['psping', 'a', 0], ['psservice', 'a', 0], 
        ['psshutdown', 'a', 0], ['pssuspend', 'a', 0], ['pushd', 'a', 0], ['qgrep', 'a', 0], ['query-process', 'a', 0], 
        ['query-session', 'a', 0], ['query-termserver', 'a', 0], ['query-user', 'a', 0], ['rasdial', 'a', 0], ['rasphone', 'a', 0], 
        ['rd', 'a', 0], ['recover', 'a', 0], ['reg', 'a', 0], ['regedit', 'a', 0], ['regsvr32', 'a', 0], 
        ['regini', 'a', 0], ['rem', 'a', 0], ['ren', 'a', 0], ['replace', 'a', 0], ['reset-session', 'a', 0], 
        ['rmtshare', 'a', 0], ['robocopy', 'a', 0], ['route', 'a', 0], ['runas', 'a', 0], ['rundll32', 'a', 0], 
        ['sc', 'a', 0], ['schtasks', 'a', 0], ['set', 'a', 0], ['setlocal', 'a', 0], ['setspn', 'a', 0], 
        ['setx', 'a', 0], ['sfc', 'a', 0], ['share', 'a', 0], ['shellrunas', 'a', 0], ['shift', 'a', 0], 
        ['shortcut', 'a', 0], ['shutdown', 'a', 0], ['sigcheck', 'a', 0], ['sleep', 'a', 0], ['slmgr', 'a', 0], 
        ['sort', 'a', 0], ['start', 'a', 0], ['strings', 'a', 0], ['subinacl', 'a', 0], ['subst', 'a', 0], 
        ['sysmon', 'a', 0], ['systeminfo', 'a', 0], ['takeown', 'a', 0], ['tasklist', 'a', 0], ['taskkill', 'a', 0], 
        ['telnet', 'a', 0], ['time', 'a', 0], ['timeout', 'a', 0], ['title', 'a', 0], ['tlist', 'a', 0], 
        ['touch', 'a', 0], ['tracert', 'a', 0], ['tree', 'a', 0], ['tsdiscon', 'a', 0], ['tskill', 'a', 0], 
        ['type', 'a', 0], ['typeperf', 'a', 0], ['tzutil', 'a', 0], ['ver', 'a', 0], ['verify', 'a', 0], 
        ['vmconnect', 'a', 0], ['vol', 'a', 0], ['vssadmin', 'a', 0], ['w32tm', 'a', 0], ['waitfor', 'a', 0], 
        ['wbadmin', 'a', 0], ['wecutil', 'a', 0], ['wevtutil', 'a', 0], ['where', 'a', 0], ['whoami', 'a', 0], 
        ['windiff', 'a', 0], ['winrm', 'a', 0], ['winrs', 'a', 0], ['wmic', 'a', 0], ['wpeutil', 'a', 0], 
        ['wpr', 'a', 0], ['wusa', 'a', 0], ['wuauclt', 'a', 0], ['xcacls', 'a', 0], ['xcopy', 'a', 0], 
        ['alias', 'a', 0], ['apt-get', 'a', 0], ['aptitude', 'a', 0], ['aspell', 'a', 0], ['awk', 'a', 0], 
        ['basename', 'a', 0], ['bc', 'a', 0], ['bg', 'a', 0], ['bind', 'a', 0], ['break', 'a', 0], 
        ['builtin', 'a', 0], ['bzip2', 'a', 0], ['cal', 'a', 0], ['case', 'a', 0], ['cat', 'a', 0], 
        ['cd', 'a', 0], ['cfdisk', 'a', 0], ['chattr', 'a', 0], ['chgrp', 'a', 0], ['chmod', 'a', 0], 
        ['chown', 'a', 0], ['chroot', 'a', 0], ['chkconfig', 'a', 0], ['cksum', 'a', 0], ['cmp', 'a', 0], 
        ['comm', 'a', 0], ['command', 'a', 0], ['continue', 'a', 0], ['cp', 'a', 0], ['cpio', 'a', 0], 
        ['cron', 'a', 0], ['crontab', 'a', 0], ['csplit', 'a', 0], ['curl', 'a', 0], ['cut', 'a', 0], 
        ['date', 'a', 0], ['dc', 'a', 0], ['dd', 'a', 0], ['ddrescue', 'a', 0], ['declare', 'a', 0], 
        ['df', 'a', 0], ['diff', 'a', 0], ['diff3', 'a', 0], ['dig', 'a', 0], ['dir', 'a', 0], 
        ['dircolors', 'a', 0], ['dirname', 'a', 0], ['dirs', 'a', 0], ['dmesg', 'a', 0], ['du', 'a', 0], 
        ['echo', 'a', 0], ['egrep', 'a', 0], ['eject', 'a', 0], ['enable', 'a', 0], ['env', 'a', 0], 
        ['eval', 'a', 0], ['exec', 'a', 0], ['exit', 'a', 0], ['expand', 'a', 0], ['export', 'a', 0], 
        ['expr', 'a', 0], ['false', 'a', 0], ['fdformat', 'a', 0], ['fdisk', 'a', 0], ['fg', 'a', 0], 
        ['fgrep', 'a', 0], ['file', 'a', 0], ['find', 'a', 0], ['fmt', 'a', 0], ['fold', 'a', 0], 
        ['for', 'a', 0], ['fsck', 'a', 0], ['ftp', 'a', 0], ['function', 'a', 0], ['fuser', 'a', 0], 
        ['getopts', 'a', 0], ['grep', 'a', 0], ['groupadd', 'a', 0], ['groupdel', 'a', 0], ['groupmod', 'a', 0], 
        ['groups', 'a', 0], ['gzip', 'a', 0], ['hash', 'a', 0], ['head', 'a', 0], ['history', 'a', 0], 
        ['hostname', 'a', 0], ['htop', 'a', 0], ['iconv', 'a', 0], ['id', 'a', 0], ['if', 'a', 0], 
        ['ifconfig', 'a', 0], ['ifup', 'a', 0], ['import', 'a', 0], ['install', 'a', 0], ['iostat', 'a', 0], 
        ['ip', 'a', 0], ['jobs', 'a', 0], ['join', 'a', 0], ['kill', 'a', 0], ['killall', 'a', 0], 
        ['less', 'a', 0], ['let', 'a', 0], ['link', 'a', 0], ['ln', 'a', 0], ['local', 'a', 0], 
        ['locate', 'a', 0], ['logname', 'a', 0], ['logout', 'a', 0], ['look', 'a', 0], ['lpc', 'a', 0], 
        ['lpr', 'a', 0], ['lprm', 'a', 0], ['lsattr', 'a', 0], ['lsblk', 'a', 0], ['ls', 'a', 0], 
        ['lsof', 'a', 0], ['lspci', 'a', 0], ['man', 'a', 0], ['mkdir', 'a', 0], ['mkfifo', 'a', 0], 
        ['mkfile', 'a', 0], ['mknod', 'a', 0], ['mktemp', 'a', 0], ['more', 'a', 0], ['most', 'a', 0], 
        ['mount', 'a', 0], ['mtools', 'a', 0], ['mtr', 'a', 0], ['mv', 'a', 0], ['mmv', 'a', 0], 
        ['nc', 'a', 0], ['netstat', 'a', 0], ['nft', 'a', 0], ['nice', 'a', 0], ['nl', 'a', 0], 
        ['nohup', 'a', 0], ['notify-send', 'a', 0], ['nslookup', 'a', 0], ['open', 'a', 0], ['op', 'a', 0], 
        ['passwd', 'a', 0], ['paste', 'a', 0], ['perf', 'a', 0], ['ping', 'a', 0], ['pkill', 'a', 0], 
        ['popd', 'a', 0], ['pr', 'a', 0], ['printenv', 'a', 0], ['printf', 'a', 0], ['ps', 'a', 0], 
        ['pushd', 'a', 0], ['pv', 'a', 0], ['pwd', 'a', 0], ['quota', 'a', 0], ['quotacheck', 'a', 0], 
        ['ram', 'a', 0], ['rar', 'a', 0], ['rcp', 'a', 0], ['read', 'a', 0], ['readonly', 'a', 0], 
        ['rename', 'a', 0], ['return', 'a', 0], ['rev', 'a', 0], ['rm', 'a', 0], ['rmdir', 'a', 0], 
        ['rsync', 'a', 0], ['screen', 'a', 0], ['scp', 'a', 0], ['sdiff', 'a', 0], ['sed', 'a', 0], 
        ['select', 'a', 0], ['seq', 'a', 0], ['set', 'a', 0], ['shift', 'a', 0], ['shopt', 'a', 0], 
        ['shutdown', 'a', 0], ['sleep', 'a', 0], ['slocate', 'a', 0], ['sort', 'a', 0], ['source', 'a', 0], 
        ['split', 'a', 0], ['ss', 'a', 0], ['ssh', 'a', 0], ['stat', 'a', 0], ['strace', 'a', 0], 
        ['su', 'a', 0], ['sudo', 'a', 0], ['sum', 'a', 0], ['suspend', 'a', 0], ['sync', 'a', 0], 
        ['tail', 'a', 0], ['tar', 'a', 0], ['tee', 'a', 0], ['test', 'a', 0], ['time', 'a', 0], 
        ['timeout', 'a', 0], ['times', 'a', 0], ['touch', 'a', 0], ['top', 'a', 0], ['tput', 'a', 0], 
        ['traceroute', 'a', 0], ['trap', 'a', 0], ['tr', 'a', 0], ['true', 'a', 0], ['tsort', 'a', 0], 
        ['tty', 'a', 0], ['type', 'a', 0], ['ulimit', 'a', 0], ['umask', 'a', 0], ['uname', 'a', 0], 
        ['unexpand', 'a', 0], ['uniq', 'a', 0], ['units', 'a', 0], ['unrar', 'a', 0], ['unset', 'a', 0], 
        ['unshar', 'a', 0], ['until', 'a', 0], ['useradd', 'a', 0], ['userdel', 'a', 0], ['usermod', 'a', 0], 
        ['users', 'a', 0], ['uuencode', 'a', 0], ['vmstat', 'a', 0], ['w', 'a', 0], ['wait', 'a', 0], 
        ['watch', 'a', 0], ['wc', 'a', 0], ['whereis', 'a', 0], ['which', 'a', 0], ['while', 'a', 0], 
        ['who', 'a', 0], ['whoami', 'a', 0], ['write', 'a', 0], ['xargs', 'a', 0], ['xdg-open', 'a', 0], 
        ['xz', 'a', 0], ['yes', 'a', 0], ['zip', 'a', 0], ['bang', 'a', 0], ['rem', 'a', 0], 
        ##############################
        ['-', 'b', 0], ['\\', 'b', 0], ['/', 'b', 0], ['sys32', 'b', 0], ['temp', 'b', 0], 
        ['c:', 'b', 0], ['download', 'b', 0], ['appdata', 'b', 0], ['local', 'b', 0], ['roaming', 'b', 0], 
        ['var', 'b', 0], ['etc', 'b', 0], ['tmp', 'b', 0], ['sbin', 'b', 0], ['bin', 'b', 0], 
        ['dev', 'b', 0], ['.exe', 'b', 0]
      ],
      [  # SSI
        ['abs', 'A', 0], ['acos', 'A', 0], ['addcslashes', 'A', 0], ['addslashes', 'A', 0], 
        ['array', 'A', 0], ['array_count_values', 'A', 0], ['array_flip', 'B', 0], 
        ['array_keys', 'B', 0], ['array_merge', 'B', 0], ['array_pad', 'B', 0], 
        ['array_pop', 'B', 0], ['array_push', 'B', 0], ['array_reverse', 'C', 0], 
        ['array_shift', 'C', 0], ['array_splice', 'C', 0], ['array_unshift', 'C', 0], 
        ['array_values', 'C', 0], ['array_walk', 'C', 0], ['arsort', 'D', 0], ['asin', 'D', 0], 
        ['asort', 'D', 0], ['atan', 'D', 0], ['atan2', 'D', 0], ['base64_decode', 'D', 0], 
        ['base64_encode', 'E', 0], ['basename', 'E', 0], ['base_convert', 'E', 0], 
        ['bin2hex', 'E', 0], ['bindec', 'E', 0], ['ceil', 'E', 0], ['checkdnsrr', 'F', 0], 
        ['chgrp', 'F', 0], ['chmod', 'F', 0], ['chop', 'F', 0], ['chown', 'F', 0], ['chr', 'F', 0], 
        ['chunk_split', 'G', 0], ['clearstatcache', 'G', 0], ['compact', 'G', 0], 
        ['convert_cyr_string', 'G', 0], ['copy', 'G', 0], ['cos', 'G', 0], 
        ['count', 'H', 0], ['crc32', 'H', 0], ['crypt', 'H', 0], ['current', 'H', 0], 
        ['date', 'H', 0], ['decbin', 'H', 0], ['dechex', 'I', 0], ['decoct', 'I', 0], 
        ['deg2rad', 'I', 0], ['dirname', 'I', 0], ['diskfreespace', 'I', 0], ['doubleval!!', 'I', 0], 
        ['each', 'J', 0], ['echo', 'J', 0], ['empty', 'J', 0], ['end', 'J', 0], ['exp', 'J', 0], ['explode', 'J', 0], 
        ['extract', 'K', 0], ['fclose', 'K', 0], ['feof', 'K', 0], ['fgetc', 'K', 0], ['fgetcsv', 'K', 0], 
        ['fgets', 'K', 0], ['floor', 'L', 0], ['getimagesize', 'L', 0], ['getrandmax', 'L', 0], 
        ['gettype', 'L', 0], ['get_html_translation_table', 'L', 0], ['get_meta_tags', 'L', 0], 
        ['hexdec', 'M', 0], ['htmlentities', 'M', 0], ['htmlspecialchars', 'M', 0], ['imagearc', 'M', 0], 
        ['imagechar', 'M', 0], ['imagecolorallocate', 'M', 0], ['imagecolorat', 'N', 0], 
        ['imagecolorclosest', 'N', 0], ['imagecolorexact', 'N', 0], ['imagecolorresolve', 'N', 0], 
        ['imagecolorset', 'N', 0], ['imagecolorsforindex', 'N', 0], ['imagecolorstotal', 'O', 0], 
        ['imagecolortransparent', 'O', 0], ['imagecopyresized', 'O', 0], ['imagecreate', 'O', 0], 
        ['imagecreatefromgif', 'O', 0], ['imagedashedline', 'O', 0], ['imagedestroy', 'P', 0], 
        ['imagefill', 'P', 0], ['imagefilledpolygon', 'P', 0], ['imagefilledrectangle', 'P', 0], 
        ['imagefilltoborder', 'P', 0], ['imagefontheight', 'P', 0], ['imagefontwidth', 'Q', 0], 
        ['imagegif', 'Q', 0], ['imageinterlace', 'Q', 0], ['imageline', 'Q', 0], ['imageloadfont', 'Q', 0], 
        ['imagepolygon', 'Q', 0], ['imagepsbbox', 'R', 0], ['imagepsencodefont', 'R', 0], 
        ['imagepsfreefont', 'R', 0], ['imagepsloadfont', 'R', 0], ['imagepstext', 'R', 0], 
        ['imagerectangle', 'R', 0], ['imagesetpixel', 'S', 0], ['imagestring', 'S', 0], 
        ['imagestringup', 'S', 0], ['imagesx', 'S', 0], ['imagesy', 'S', 0], ['ImageTTFBBox', 'S', 0], 
        ['ImageTTFText', 'T', 0], ['implode', 'T', 0], ['intval', 'T', 0], ['in_array', 'T', 0], ['isset', 'T', 0], 
        ['is_array', 'T', 0], ['is_double', 'U', 0], ['is_float', 'U', 0], ['is_int', 'U', 0], ['is_integer', 'U', 0], 
        ['is_long', 'U', 0], ['is_object', 'U', 0], ['is_real', 'V', 0], ['is_string', 'V', 0], ['join', 'V', 0], 
        ['key', 'V', 0], ['krsort', 'V', 0], ['ksort', 'V', 0], ['list', 'W', 0], ['log', 'W', 0], ['log10', 'W', 0], 
        ['ltrim', 'W', 0], ['max', 'W', 0], ['md5', 'W', 0], ['metaphone', 'X', 0], ['min', 'X', 0], 
        ['mktime', 'X', 0], ['mssql_bind', 'X', 0], ['mssql_close', 'X', 0], ['mssql_connect', 'X', 0], 
        ['mssql_data_seek', 'Y', 0], ['mssql_execute', 'Y', 0], ['mssql_fetch_array', 'Y', 0], 
        ['mssql_fetch_assoc', 'Y', 0], ['mssql_fetch_batch', 'Y', 0], ['mssql_fetch_field', 'Y', 0], 
        ['mssql_fetch_object', 'Z', 0], ['mssql_fetch_row', 'Z', 0], ['mssql_field_length', 'Z', 0], 
        ['mssql_field_name', 'Z', 0], ['mssql_field_seek', 'Z', 0], ['mssql_field_type', 'Z', 0], 
        ['mssql_free_result', 'a', 0], ['mssql_free_statement', 'a', 0], ['mssql_get_last_message', 'a', 0], 
        ['mssql_guid_string', 'a', 0], ['mssql_init', 'a', 0], ['mssql_min_error_severity', 'a', 0], 
        ['mssql_min_message_severity', 'b', 0], ['mssql_next_result', 'b', 0], ['mssql_num_fields', 'b', 0], 
        ['mssql_num_rows', 'b', 0], ['mssql_pconnect', 'b', 0], ['mssql_query', 'b', 0], ['mssql_result', 'c', 0], 
        ['mssql_rows_affected', 'c', 0], ['mssql_select_db', 'c', 0], ['mt_getrandmax', 'c', 0], ['mt_rand', 'c', 0], 
        ['mt_srand', 'c', 0], ['mysql_affected_rows', 'd', 0], ['mysql_change_user', 'd', 0], ['mysql_close', 'd', 0], 
        ['mysql_connect', 'd', 0], ['mysql_create_db', 'd', 0], ['mysql_data_seek', 'd', 0], ['mysql_db_query', 'e', 0], 
        ['mysql_drop_db', 'e', 0], ['mysql_fetch_array', 'e', 0], ['mysql_fetch_field', 'e', 0], 
        ['mysql_fetch_lengths', 'e', 0], ['mysql_fetch_object', 'e', 0], ['mysql_fetch_row', 'f', 0], 
        ['mysql_field_flags', 'f', 0], ['mysql_field_len', 'f', 0], ['mysql_field_name', 'f', 0], 
        ['mysql_field_seek', 'f', 0], ['mysql_field_table', 'f', 0], ['mysql_field_type', 'g', 0], 
        ['mysql_free_result', 'g', 0], ['mysql_insert_id', 'g', 0], ['mysql_list_dbs', 'g', 0], 
        ['mysql_list_fields', 'g', 0], ['mysql_list_tables', 'g', 0], ['mysql_num_fields', 'h', 0], 
        ['mysql_num_rows', 'h', 0], ['mysql_pconnect', 'h', 0], ['mysql_query', 'h', 0], 
        ['mysql_result', 'h', 0], ['mysql_select_db', 'h', 0], ['mysql_tablename', 'i', 0], ['next', 'i', 0], 
        ['nl2br', 'i', 0], ['number_format', 'i', 0], ['octdec', 'i', 0], ['ord', 'i', 0], ['parse_str', 'j', 0], 
        ['parse_url', 'j', 0], ['pi', 'j', 0], ['pos', 'j', 0], ['pow', 'j', 0], ['prev', 'j', 0], ['print', 'k', 0], 
        ['printf', 'k', 0], ['quoted_printable_decode', 'k', 0], ['quotemeta', 'k', 0], ['rand', 'k', 0], 
        ['range', 'k', 0], ['rawurldecode', 'l', 0], ['rawurlencode', 'l', 0], ['reset', 'l', 0], ['round', 'l', 0], 
        ['rsort', 'l', 0], ['rtrim', 'l', 0], ['session_decode', 'm', 0], ['session_destroy', 'm', 0], 
        ['session_encode', 'm', 0], ['session_id', 'm', 0], ['session_is_registered', 'm', 0], 
        ['session_module_name', 'm', 0], ['session_name', 'n', 0], ['session_register', 'n', 0], 
        ['session_save_path', 'n', 0], ['session_start', 'n', 0], ['session_unregister', 'n', 0], 
        ['setlocale', 'n', 0], ['settype', 'o', 0], ['shuffle', 'o', 0], ['similar_text', 'o', 0], ['sin', 'o', 0], 
        ['sizeof', 'o', 0], ['sort', 'o', 0], ['soundex', 'p', 0], ['sprintf', 'p', 0], ['sqrt', 'p', 0], ['srand', 'p', 0], 
        ['strcasecmp', 'p', 0], ['strchr', 'p', 0], ['strcmp', 'q', 0], ['strcspn', 'q', 0], ['stripcslashes', 'q', 0], 
        ['stripslashes', 'q', 0], ['strip_tags', 'q', 0], ['stristr', 'q', 0], ['strlen', 'r', 0], ['strpos', 'r', 0], 
        ['strrchr', 'r', 0], ['strrev', 'r', 0], ['strrpos', 'r', 0], ['strspn', 'r', 0], ['strstr', 's', 0], ['strtok', 's', 0], 
        ['strtolower', 's', 0], ['strtoupper', 's', 0], ['strtr', 's', 0], ['strval', 's', 0], ['str_repeat', 't', 0], 
        ['str_replace', 't', 0], ['substr', 't', 0], ['substr_replace', 't', 0], ['tan', 't', 0], ['trim', 't', 0], 
        ['uasort', 'u', 0], ['ucfirst', 'u', 0], ['ucwords', 'u', 0], ['uksort', 'u', 0], ['unset', 'u', 0], 
        ['urldecode', 'u', 0], ['urlencode', 'v', 0], ['usort', 'v', 0],
        ##############################
        ['$GLOBALS', 'w', 0],['$_SERVER', 'w', 0],['$_GET', 'w', 0],['$_POST', 'w', 0],['$_FILES', 'w', 0],
        ['$_REQUEST', 'w', 0],['$_SESSION', 'w', 0],['$_ENV', 'w', 0],['$_COOKIE', 'w', 0],
        ['$php_errormsg', 'v', 0],['$HTTP_RAW_POST_DATA', 'v', 0],['$http_response_header', 'v', 0],['$argc', 'v', 0],['$argv', 'v', 0]
    ],
      [  # XSS 
        ['innerhtml', 'A', 0], ['script', 'A', 0], ['svg', 'A', 0], ['contenteditable', 'A', 0], ['x', 'A', 0],
        ['src', 'B', 0], ['iframe', 'B', 0], ['javascript', 'B', 0], ['embed', 'B', 0], ['math', 'B', 0],
        ['brute', 'C', 0], ['href', 'C', 0], ['form', 'C', 0], ['action', 'C', 0], ['input', 'C', 0],
        ['type', 'D', 0], ['submit', 'D', 0], ['isindex', 'D', 0], ['value', 'D', 0], ['button', 'D', 0],
        ['formaction', 'E', 0], ['srcdoc', 'E', 0], ['xlink', 'E', 0], ['img', 'E', 0], ['xmlns', 'E', 0],
        ['link', 'F', 0], ['base', 'F', 0], ['style', 'F', 0], ['marquee', 'F', 0], ['audio', 'F', 0],
        ['video', 'G', 0], ['keygen', 'G', 0], ['autofocus', 'G', 0], ['select', 'G', 0], ['option', 'G', 0],
        ['menu', 'H', 0], ['contextmenu', 'H', 0], ['textarea', 'H', 0], ['source', 'H', 0], ['meta', 'H', 0],
        ['object', 'I', 0], ['html', 'I', 0], ['target', 'I', 0], ['card ', 'I', 0], ['onevent', 'I', 0],
        ['animate', 'J', 0], ['handler', 'J', 0], ['feimage', 'J', 0], ['table', 'J', 0],
        ['background', 'J', 0],
        ['frameset', 'K', 0], ['div', 'K', 0], ['allowscriptaccess', 'K', 0],
        ###############################
        ['onload', 'L', 0], ['onmouseover', 'L', 0], ['onsubmit', 'L', 0], ['onfocus', 'L', 0],
        ['onblur', 'L', 0],
        ['onclick', 'M', 0], ['oncopy', 'M', 0], ['oncontextmenu', 'M', 0], ['oncut', 'M', 0],
        ['ondblclick', 'N', 0], ['ondrag', 'N', 0], ['oninput', 'N', 0], ['onkeydown', 'N', 0],
        ['onkeypress', 'O', 0], ['onkeyup', 'O', 0], ['onmousedown', 'O', 0], ['onmousemove', 'O', 0],
        ['onmouseout', 'P', 0], ['onmouseup', 'P', 0], ['onpaste', 'P', 0], ['ontouchstart', 'P', 0],
        ['ontouchend', 'R', 0], ['ontouchmove', 'R', 0], ['ontouchcancel', 'R', 0],
        ['onorientationchange', 'R', 0],
        ['onerror', 'S', 0], ['onpageshow', 'S', 0], ['onhashchange', 'S', 0], ['onscroll', 'S', 0],
        ['onresize', 'T', 0], ['onhelp', 'T', 0], ['onstart', 'T', 0], ['onloadstart', 'T', 0],
        ['onchange', 'U', 0], ['onshow', 'U', 0], ['oneonerrorrror', 'U', 0], ['ontoggle', 'U', 0],
        ['onafterscriptexecute', 'V', 0], ['onbeforescriptexecute', 'V', 0], ['onfinish', 'V', 0],
        ['expression', 'W', 0], ['onbeforeload', 'W', 0], ['onbeforeunload', 'W', 0], ['onformchange', 'W', 0],
        ['vbscript', 'W', 0],
        ##########################
        ['eval', 'X', 0], ['find', 'X', 0], ['top', 'X', 0], ['source', 'X', 0], ['tostring', 'X', 0],
        ['url', 'Y', 0], ['slice', 'Y', 0], ['location', 'Y', 0], ['hash', 'Y', 0], ['setInterval', 'Y', 0],
        ['function', 'Z', 0], ['appendchild', 'Z', 0], ['createelement', 'Z', 0], ['rel', 'Z', 0],
        ['string', 'a', 0], ['fromcharcode', 'a', 0], ['window', 'a', 0], ['parent', 'a', 0], ['self', 'a', 0],
        ['prompt', 'b', 0], ['defineproperties', 'b', 0], ['event', 'b', 0], ['initmouseevent', 'b', 0],
        ['childnodes', 'c', 0], ['clonenode', 'c', 0], ['match', 'c', 0], ['head', 'c', 0], ['substr', 'c', 0],
        ['unescape', 'd', 0], ['xmlhttp', 'd', 0], ['open', 'd', 0], ['content', 'd', 0], ['frames', 'd', 0],
        ['import', 'e', 0], ['behavior', 'e', 0], ['geturl', 'e', 0], ['charset', 'e', 0],
        #######################
        ['alert', 'f', 0], ['navigator', 'f', 0], ['vibrate', 'f', 0], ['document', 'f', 0], ['domain', 'f', 0],
        ['message', 'g', 0], ['write', 'g', 0], ['cookie', 'g', 0], ['echo', 'g', 0], ['exec', 'g', 0],
        ['cmd', 'h', 0], ['msgbox', 'h', 0],
        ########################
        ['xss', 'i', 0], ['hello', 'i', 0], ['fuzzelement', 'i', 0], ['test', 'i', 0], ['injectx', 'i', 0],
        ['netsparker', 'j', 0], ['openbugbounty', 'j', 0], ['baiduspider', 'j', 0], ['csrf', 'j', 0]
      ],
      [  # CSRF
        ['innerhtml', 'A', 0], ['script', 'A', 0], ['svg', 'A', 0], ['contenteditable', 'A', 0], ['x', 'A', 0],
        ['src', 'B', 0], ['iframe', 'B', 0], ['javascript', 'B', 0], ['embed', 'B', 0], ['math', 'B', 0],
        ['brute', 'C', 0], ['href', 'C', 0], ['form', 'C', 0], ['action', 'C', 0], ['input', 'C', 0],
        ['type', 'D', 0], ['submit', 'D', 0], ['isindex', 'D', 0], ['value', 'D', 0], ['button', 'D', 0],
        ['formaction', 'E', 0], ['srcdoc', 'E', 0], ['xlink', 'E', 0], ['img', 'E', 0], ['xmlns', 'E', 0],
        ['link', 'F', 0], ['base', 'F', 0], ['style', 'F', 0], ['marquee', 'F', 0], ['audio', 'F', 0],
        ['video', 'G', 0], ['keygen', 'G', 0], ['autofocus', 'G', 0], ['select', 'G', 0], ['option', 'G', 0],
        ['menu', 'H', 0], ['contextmenu', 'H', 0], ['textarea', 'H', 0], ['source', 'H', 0], ['meta', 'H', 0],
        ['object', 'I', 0], ['html', 'I', 0], ['target', 'I', 0], ['card ', 'I', 0], ['onevent', 'I', 0],
        ['animate', 'J', 0], ['handler', 'J', 0], ['feimage', 'J', 0], ['table', 'J', 0],
        ['background', 'J', 0],
        ['frameset', 'K', 0], ['div', 'K', 0], ['allowscriptaccess', 'K', 0],
        ###############################
        ['onload', 'L', 0], ['onmouseover', 'L', 0], ['onsubmit', 'L', 0], ['onfocus', 'L', 0],
        ['onblur', 'L', 0],
        ['onclick', 'M', 0], ['oncopy', 'M', 0], ['oncontextmenu', 'M', 0], ['oncut', 'M', 0],
        ['ondblclick', 'N', 0], ['ondrag', 'N', 0], ['oninput', 'N', 0], ['onkeydown', 'N', 0],
        ['onkeypress', 'O', 0], ['onkeyup', 'O', 0], ['onmousedown', 'O', 0], ['onmousemove', 'O', 0],
        ['onmouseout', 'P', 0], ['onmouseup', 'P', 0], ['onpaste', 'P', 0], ['ontouchstart', 'P', 0],
        ['ontouchend', 'R', 0], ['ontouchmove', 'R', 0], ['ontouchcancel', 'R', 0],
        ['onorientationchange', 'R', 0],
        ['onerror', 'S', 0], ['onpageshow', 'S', 0], ['onhashchange', 'S', 0], ['onscroll', 'S', 0],
        ['onresize', 'T', 0], ['onhelp', 'T', 0], ['onstart', 'T', 0], ['onloadstart', 'T', 0],
        ['onchange', 'U', 0], ['onshow', 'U', 0], ['oneonerrorrror', 'U', 0], ['ontoggle', 'U', 0],
        ['onafterscriptexecute', 'V', 0], ['onbeforescriptexecute', 'V', 0], ['onfinish', 'V', 0],
        ['expression', 'W', 0], ['onbeforeload', 'W', 0], ['onbeforeunload', 'W', 0], ['onformchange', 'W', 0],
        ['vbscript', 'W', 0],
        ##########################
        ['eval', 'X', 0], ['find', 'X', 0], ['top', 'X', 0], ['source', 'X', 0], ['tostring', 'X', 0],
        ['url', 'Y', 0], ['slice', 'Y', 0], ['location', 'Y', 0], ['hash', 'Y', 0], ['setInterval', 'Y', 0],
        ['function', 'Z', 0], ['appendchild', 'Z', 0], ['createelement', 'Z', 0], ['rel', 'Z', 0],
        ['string', 'a', 0], ['fromcharcode', 'a', 0], ['window', 'a', 0], ['parent', 'a', 0], ['self', 'a', 0],
        ['prompt', 'b', 0], ['defineproperties', 'b', 0], ['event', 'b', 0], ['initmouseevent', 'b', 0],
        ['childnodes', 'c', 0], ['clonenode', 'c', 0], ['match', 'c', 0], ['head', 'c', 0], ['substr', 'c', 0],
        ['unescape', 'd', 0], ['xmlhttp', 'd', 0], ['open', 'd', 0], ['content', 'd', 0], ['frames', 'd', 0],
        ['import', 'e', 0], ['behavior', 'e', 0], ['geturl', 'e', 0], ['charset', 'e', 0],
        #######################
        ['alert', 'f', 0], ['navigator', 'f', 0], ['vibrate', 'f', 0], ['document', 'f', 0], ['domain', 'f', 0],
        ['message', 'g', 0], ['write', 'g', 0], ['cookie', 'g', 0], ['echo', 'g', 0], ['exec', 'g', 0],
        ['cmd', 'h', 0], ['msgbox', 'h', 0],
        ########################
        ['xss', 'i', 0], ['hello', 'i', 0], ['fuzzelement', 'i', 0], ['test', 'i', 0], ['injectx', 'i', 0],
        ['netsparker', 'j', 0], ['openbugbounty', 'j', 0], ['baiduspider', 'j', 0], ['csrf', 'j', 0]
      ],
      [  # AU
        ['chrome' , 'a', 1], ['trident' , 'a', 1], ['opera' , 'a', 1], ['webkit' , 'a', 1], ['gecko' , 'a', 1] 
      ]]
      index_arr = ['Basic', 'FD', 'FUP', 'RCE', 'SQL', 'UAA', 'PT', 'OC', 'SSI', 'XSS', 'CSRF', 'AU']
      try :
        index = index_arr.index(self.preprocessing_type)
      except:
        index = 0 # Basic
      self.SWtoken = SWtoken_Arr[index]

      for i in range(len(self.SWtoken)):
        iLenTemp = len(self.SWtoken[i][0])
        self.SWtoken[i][2] = iLenTemp

      self.sorted_sw_token = sorted(self.SWtoken, key=itemgetter(2), reverse=True)



    def apply(self, data):
      try:
        if self.preprocessing_type == 'RCE':
            for rce in SWupper_arr:
              if rce[0] != " ":
                data = data.replace(str(rce[0]), ' ' + str(rce[0]) + ' ').replace("  ", " ")

        ####################################kps################################################
        data = data.replace("\r\n", " ").replace("\n", " ").replace("\t", " ").replace("  ", " ").replace("  ", " ")
        ####################################kps################################################
        ## URL Decode
        _input = data
        _input = _input.replace("CCOMMAA", ",")
        ####################################kps################################################
        # _input = _input.replace(",", "CCOMMAA")
        ####################################kps################################################
        try:
            iLoopCnt = 0
            val = ""
            while val != _input or iLoopCnt<=5:
              val = _input
              iLoopCnt += 1
              _input = decode.unquote(_input.upper())
            dec_data = _input.lower()
        except:
            dec_data = str(_input).lower()

            dec_data = dec_data.replace("\r\n", " ").replace("\n", " ").replace("\r", " ")
        try:
            dec_data = re.findall(r'(?i)(get.*|post.*)', dec_data)[0]
            # self.mlps_logger.getLogger().info(dec_data)
        except Exception as e:
            dec_data = dec_data
            #print(e)
####################################kps################################################
        # IpFind = list(set(re.findall(r'[\W_]',dec_data)))
        #
        # for ix in range(10):
        #     IpFind.append(ix)
####################################kps################################################
####################################kps################################################
        IpFind = list(set(re.findall(r'[\W_0-9]', dec_data)))
####################################kps################################################
        for token in IpFind:
            if token != " ":
              dec_data = dec_data.replace(str(token), ' '+str(token)+ ' ').replace("  ", " ")

        payload = dec_data
        payload = " " + payload + " "
        payload = payload.strip()
        IpCompare = []

        for word, change, len_word in self.sorted_sw_token :
            payload = payload.replace(" "+word+" "," ksshin"+change+" ")
            IpCompare.append("ksshin"+change)

####################################kps################################################
        # strTemp =""
        # resultPayload = payload.split(" ")
        #
        # for ChangeWord in resultPayload:
        #     if ChangeWord in IpFind or ChangeWord in IpCompare and ChangeWord != " ":
        #         strTemp = strTemp+ " " + ChangeWord.replace("ksshin", "")
        #
        # print(strTemp)
        # result = list()
        #
        # for i, ch in enumerate(strTemp):
        #     if ch != " ":
        #         result.append(ord(ch))
####################################kps################################################
####################################kps################################################
        resultPayload = payload.split(" ")
        result = list()

        for ChangeWord in resultPayload:
            try:
              if (ChangeWord in IpFind or ChangeWord in IpCompare) and ChangeWord != " " and not ChangeWord.isdigit():
                result.append(ord(ChangeWord.replace("ksshin", "")))
            except Exception as e:
              pass

####################################kps################################################
        ## padding
        iMax = self.max_len - 4
        padding0 = []
        bufferLen = len(result)
        #print(bufferLen)
        if bufferLen < iMax:
            # strBuffer=buffer[i].pop(0)
            padding0.extend([0] * 2)
            padding0.extend(result)
            # padding0.extend(buffer[i])
            padding1 = [255] * (iMax - bufferLen)
            padding0.extend(padding1)
            padding0.extend([0] * 2)
        elif bufferLen == iMax:
            #padding0.append(result[i].pop(0))
            padding0.extend([0] * 2)
            padding0.extend(result)
            padding0.extend([0] * 2)

        elif bufferLen > iMax:
            #padding0.append(result[i].pop(0))
            padding0.extend([0] * 2)
            padding0.extend(result[:iMax])
            padding0.extend([0] * 2)

        result = padding0

        return result


        # if result_len < self.max_len :
        #     padding = [255]*(self.max_len - result_len)
        #     result.extend(padding)
        #     return result
        # else :
        #     return result[:self.max_len]

      except Exception as e :
        # self.mlps_logger.error(e, exc_info=True)
        #print(e)
        return [255] * self.max_len

    def get_num_feat(self):
      return self.max_len

if __name__ == '__main__':
    #data = "hjg yjhg 6ug679t g6guy g321%!#% $^$Fgsdfha"
    data = " HEAD /%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/%c0%ae%c0%ae/etc/qbttxe HTTP/1.1#015#012Host: icarus.hangame.com#015#012Cookie: JSESSIONID=1181434228E1C982767B9E1A8DF6B1F4; tracking="+"&SID=234099862&Count=4&Code=0"+"#015#012Connection: Keep-Alive#015#012Accept: */*#015#012User-Agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; .NET CLR 2.0.50727)"
    cvt_fn = SpecialWordChar_1(20, 'PT') # 스테이트딕이 민맥스가 있을경우 넣어줘야함, 아규리스트가 4인데 원소를 4개로 잘라서 몇개만 쓸껀지
    rst = cvt_fn.apply(data=data)
    print(rst)
    print(len(rst))
    # print(len(cvt_fn.apply(data="//")))


def special(data, tp):

    cvt_fn = SpecialWordChar_1(20, tp) # 스테이트딕이 민맥스가 있을경우 넣어줘야함, 아규리스트가 4인데 원소를 4개로 잘라서 몇개만 쓸껀지
    rst = cvt_fn.apply(data=data)
    return rst