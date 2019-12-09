from sql_filter import *
import urllib
import numpy as np
import os

def del_annotation(string):
    start_flag = False
    oneline_flag = False
    dellist = []
    start_index = -1
    for index in range(0,len(string)):
        char = string[index]
        if start_flag == False:
            if char == "/":
                if index == len(string)-1 :
                    continue
                elif string[index+1] == "*":
                    start_flag = True
                    start_index = index
            elif char == "#":
                start_flag = True
                oneline_flag = True
                start_index = index
                if index == len(string)-1:
                    dellist.append([index,index])
            elif char == "-":
                if index == len(string)-1 :
                    continue
                elif string[index+1] == "-":
                    start_flag = True
                    oneline_flag = True
                    start_index = index
        else:
            if oneline_flag == True:                #oneline comment
                if index == len(string)-1:
                    dellist.append([start_index,index])
            elif index > start_index + 1:           #comment
                if char == "*":
                    if index == len(string)-1:
                        continue
                    elif string[index+1] == "/":
                        dellist.append([start_index,index+1])
                        start_flag = False
                        start_index = -1
    dellist.reverse()
    for i in dellist:
        string = string[:i[0]]+" "+string[i[1]+1:]

    return string

def sqldatareadtest():
    dirname = "./sqldata/"
    savefolder = "./sqlnp/"
    filename = os.listdir(dirname)
    datanum=0           # 전체 데이터 수
    num=0               # 다중 리스트 데이터 수
    emptynum=0          # 빈 데이터 수
    error_num=[]        # 에러 수
    emptyindex=[]       # 빈 데이터 index
    test=[]
    nplist=[]
    testnum=0
    for fileN in filename:
        p=open(dirname+fileN,'r',encoding='utf-8')
        pw=open(savefolder+"text/"+fileN[:-4]+'_filter.txt','w',encoding='utf-8')
        print(fileN)
        for row in p:
            
            #if testnum >10: break
            #if testnum%100 == 0 : print(testnum)
            try:
                onelineflag= True
                #if datanum ==100: break
                datanum+=1
                writelist=[]
                row = row.strip(']\n[').split(', ')
                for data in row:
                    data = urllib.parse.unquote(data)
                    data = data.replace(";"," ")
                    data = data.replace("\\t"," ")
                    data = data.replace("\\n"," ")
                    data = data.replace("%3b"," ")
                    string = del_annotation(data[1:-1])
                    if len(string) < 8:
                        writelist.append(string)
                    else:
                        result = sqlfilter(string)
                        writelist.append(result) 
                
                whitelistflag = True
                for data in writelist:
                    for i in data:
                        if "exec" in i:
                            writelist = []
                            whitelistflag = False
                            break
                    for i in data:
                        if onelineflag == False:
                            break
                        if isinstance(i,list):  #if data has sevral lists, onelineflag is False
                            if len(i) == 0:
                                continue
                            num+=1
                            test.append(datanum)
                            onelineflag = False
                            
                pw.write(str(writelist)+"\n")
                nplist.append((writelist))
                #print(writelist)
                testnum+=1

            except IndexError:
                #print("error!",end="")
                error_num.append(datanum)
        p.close()
        pw.close()
    np.save(savefolder+fileN[:-4]+"_filter",nplist)

    
sqldatareadtest()
