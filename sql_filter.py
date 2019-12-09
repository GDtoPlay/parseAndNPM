def parse(sql):
    orderstart = 0
    orderlist = ['update','select','delete','insert']
    commaindex=[]
    subquery=[]
    start = 0
    endL = True
    end = 0
    check=0
    root = 0
    insertcheck=[]
    dellist=[]
    alist=[]
    nonaccept=[]
    
    funclist=['ascii', 'bin', 'binary-operator', 'bit_length', 'cast', 'char-function',
              'character_length', 'char_length', 'chr', 'concat', 'concat_ws',
              'convert', 'elt', 'export_set', 'extractvalue', 'field', 'find_in_set',
              'format', 'from_base64', 'hex', 'insert-function', 'instr', 'lcase',
              'left', 'length', 'lengthb', 'like', 'load_file', 'locate', 'lower',
              'lpad', 'ltrim', 'make_set', 'match-against', 'mid', 'not-like',
              'not-regexp', 'octet_length', 'ord', 'position', 'quote',
              'repeat-function', 'replace-function', 'reverse', 'right', 'rpad',
              'rtrim', 'soundex', 'sounds-like', 'space', 'strcmp', 'substring',
              'substring_index', 'to_base64', 'trim', 'ucase', 'uncompressed_length',
              'unhex', 'updatexml', 'upper', 'weight_string', 'column_add',
              'column_check', 'column_create', 'column_delete', 'column_exists',
              'column_get', 'column_json', 'column_list', 'regexp', 'regexp_instr',
              'regexp_replace', 'regexp_substr', 'rlike', 'adddate', 'addtime',
              'convert_tz', 'curdate', 'current_date', 'current_time',
              'current_timestamp', 'curtime', 'date-function', 'datediff', 'date_add',
              'date_format', 'date_sub', 'day', 'dayname', 'dayofmonth', 'dayofweek',
              'dayofyear', 'extract', 'from_days', 'from_unixtime', 'get_format',
              'hour', 'last_day', 'localtime', 'localtimestamp', 'makedate', 'maketime',
              'microsecond', 'minute', 'month', 'monthname', 'now', 'period_add',
              'period_diff', 'quarter', 'second', 'sec_to_time', 'str_to_date',
              'subdate', 'subtime', 'sysdate', 'time-function', 'timediff',
              'timestamp-function', 'timestampadd', 'timestampdiff', 'time_format',
              'time_to_sec', 'to_days', 'to_seconds', 'unix_timestamp', 'utc_date',
              'utc_time', 'utc_timestamp', 'week', 'weekday', 'weekofyear', 'year',
              'yearweek', 'avg', 'bit_and', 'bit_or', 'bit_xor', 'count',
              'count-distinct', 'group_concat', 'max', 'min', 'std', 'stddev',
              'stddev_pop', 'stddev_samp', 'sum', 'variance', 'var_pop', 'var_samp',
              'addition-operator', 'subtraction-operator-', 'division-operator',
              'multiplication-operator', 'modulo-operator', 'div', 'abs', 'acos',
              'asin', 'atan', 'atan2', 'ceil', 'ceiling', 'conv', 'cos', 'cot',
              'crc32', 'degrees', 'exp', 'floor', 'greatest', 'least', 'ln', 'log',
              'log10', 'log2', 'mod', 'oct', 'pi', 'pow', 'power', 'radians', 'rand',
              'round', 'sign', 'sin', 'sqrt', 'tan', 'truncate', 'case-operator',
              'if-function', 'ifnull', 'nullif', 'bitwise_and', 'shift-left',
              'shift-right', 'bit_count', 'bitwise-xor', 'bitwise-or', 'bitwise-not',
              'aes_decrypt', 'aes_encrypt', 'compress', 'decode', 'des_decrypt',
              'des_encrypt', 'encode', 'encrypt', 'md5', 'old_password', 'password',
              'sha1', 'sha2', 'uncompress', 'uncompressed_length', 'benchmark',
              'binlog_gtid_pos', 'charset', 'coercibility', 'collation', 'connection_id',
              'current_role', 'current_user', 'database', 'decode_histogram',
              'default', 'found_rows', 'last_insert_id', 'last_value',
              'procedure-analyse', 'row_count', 'schema', 'session_user', 'system_user',
              'user', 'version', 'get_lock', 'inet6_aton', 'inet6_ntoa', 'inet_aton',
              'inet_ntoa', 'is_free_lock', 'is_ipv4', 'is_ipv4_compat', 'is_ipv4_mapped',
              'is_ipv6', 'is_used_lock', 'master_gtid_wait', 'master_pos_wait',
              'name_const', 'release_lock', 'sleep', 'uuid', 'uuid_short',
              'values-value', 'json_array', 'json_array_append', 'json_array_insert',
              'json_compact', 'json_contains', 'json_contains_path', 'json_depth',
              'json_detailed', 'json_extract', 'json_insert', 'json_keys', 'json_length',
              'json_loose', 'json_merge', 'json_object', 'json_query', 'json_quote',
              'json_remove', 'json_replace', 'json_search', 'json_set', 'json_type',
              'json_unquote', 'json_valid', 'json_value', 'spider_bg_direct_sql',
              'spider_copy_tables', 'spider_direct_sql', 'spider_flush_table_mon_cache',
              'cume_dist', 'dense_rank', 'first_value', 'lag', 'lead', 'median',
              'nth_value', 'ntile', 'percent_rank', 'rank', 'row_number',
              'geometrycollection', 'linestring', 'multilinestring', 'multipoint',
              'multipolygon', 'point', 'polygon', 'sleep', 'st_buffer', 'st_convexhull',
              'st_intersection', 'st_pointonsurface', 'st_symdifference', 'st_union',
              'st_boundary', 'st_dimension', 'st_envelope', 'st_geometryn',
              'st_geometrytype', 'st_isclosed', 'st_isempty', 'st_isring', 'st_issimple',
              'st_numgeometries', 'st_relate', 'st_srid', 'contains', 'crosses',
              'disjoint', 'equals', 'intersects', 'overlaps', 'st-contains', 'st-crosses',
              'st_difference', 'st_disjoint', 'st_distance', 'st-equals',
              'st_intersects', 'st_length', 'st-overlaps', 'st-touches', 'st-within',
              'touches', 'within', 'glength', 'st_endpoint', 'st_numpoints', 'st_pointn',
              'st_startpoint', 'mbrcontains', 'mbrdisjoint', 'mbrequal', 'mbrintersects',
              'mbroverlaps', 'mbrtouches', 'mbrwithin', 'st_x', 'st_y', 'st_area',
              'st_centroid', 'st_exteriorring', 'st_interiorringn', 'st_numinteriorrings',
              'mlinefromwkb', 'mpointfromwkb', 'mpolyfromwkb', 'st_asbinary',
              'st_geomcollfromwkb', 'st_geomfromwkb', 'st_linefromwkb', 'st_pointfromwkb',
              'st_polyfromwkb', 'mlinefromtext', 'mpointfromtext', 'mpolyfromtext',
              'st_astext', 'st_geomcollfromtext', 'st_geomfromtext', 'st_linefromtext',
              'st_pointfromtext', 'st_polyfromtext'
            ]
    
    for idx,name in enumerate(sql):
        if name in orderlist:
            root = name
            orderstart = idx

    if root == "insert":
        for i in range(0,len(sql)):
            if sql[i] == "values":
                insertcheck.append(i+1)
                insertcheck.append(subparse(sql,i+1))
                break
        del sql[insertcheck[1]]
        del sql[insertcheck[0]]

    
           
        
    for i in range(0,len(sql)):
        if start != 0:

            if i <= end:
                continue
        if isinstance(sql[i],list):
            continue
        if sql[i] == ",":
            commaindex.append(i)
        if sql[i] is "(":
            if sql[i-1] in funclist:
                start = i
                end = subparse(sql,start)
                if end !=-1:
                    subquery = sql[int(start)+1:end]
                    sql[start] = subquery
                    dellist.append([start+1,end+1])
                    #print([start+1,end+1])
                else:
                    nonaccept.append(start)
    for i in dellist:
        for l in range(i[0],i[1]):
            if l in alist:
                continue
            alist.append(l)
    if commaindex != []:
        for i in commaindex:
            if i in alist:
                continue
            alist.append(i)
    if nonaccept != []:
        for i in nonaccept:
            if i in alist:
                continue
            alist.append(i)
        
            
    alist.sort(reverse=True)
    for i in alist:
        del sql[i]
    
    
    endL = endlist(sql,orderstart)
    if endL != False:
        lastsql = sql[end:]
        sql = sql[:end]
    for i in range(0,len(sql)):
        if isinstance(sql[i],list):
            sql[i]= parse(sql[i])
    if endL != False:
        lastsql = additional_assign_check(lastsql)
        lastsql = assign2root(lastsql,endL)
        lastsql = child2list(lastsql,endL)
    sql = additional_assign_check(sql)
#    print(sql)              ##
    sql = assign2root(sql,root)
#    print(sql)              ##            
    sql = child2list(sql,root)

    
    if endL != False:
        
        sql.extend(lastsql)
    return sql

def endlist(sql,start):
    orderlist = ['update','select','delete','insert']
    for i in range(start+1,len(sql)):
        if sql[i] in orderlist:
            return i
    return False
    
def subparse(sql,start):
    count = 1
    for i in range(start+1,len(sql)):
        
        l = sql[i]
        if l is "(":
            count += 1
        if l is ")":
            count -= 1
        if count is 0:
            return i
    return -1

def splitcheck(origin_sql):    
    sql = []
    for chunk in origin_sql:
        if ',' in chunk or '(' in chunk or ')' or '+' or '&' or '=' or '|' in chunk:
            start = 0
            end = 0
            for idx, char in enumerate(chunk):
                if char == ',':
                    end = idx - 1
                    if end >= 0:
                        if chunk[start:end + 1] != '':
                            sql.append(chunk[start:end + 1])
                    sql.append(',')
                    start = idx + 1

                elif char == '(':
                    end = idx - 1
                    if end >= 0:
                        if chunk[start:end + 1] != '':
                            sql.append(chunk[start:end + 1])
                    sql.append('(')
                    start = idx + 1

                elif char == ')':
                    end = idx - 1
                    if end >= 0:
                        if chunk[start:end + 1] != '':
                            sql.append(chunk[start:end + 1])
                    sql.append(')')
                    start = idx + 1

                elif char == '=':
                    end = idx - 1
                    if end >= 0:
                        if chunk[start:end + 1] != '':
                            sql.append(chunk[start:end + 1])
                    sql.append('=')
                    start = idx + 1

                elif char == '&':
                    end = idx - 1
                    if end >= 0:
                        if chunk[start:end + 1] != '':
                            sql.append(chunk[start:end + 1])
                    sql.append('&')
                    start = idx + 1

                elif char == '|':
                    end = idx - 1
                    if end >= 0:
                        if chunk[start:end + 1] != '':
                            sql.append(chunk[start:end + 1])
                    sql.append('|')
                    start = idx + 1
                    
                elif char == '+':
                    end = idx - 1
                    if end >= 0:
                        if chunk[start:end + 1] != '':
                            sql.append(chunk[start:end + 1])
                    sql.append('+')
                    start = idx + 1

            if start != len(chunk):
                sql.append(chunk[start:])
                    
        else:
            sql.append(chunk)                

    return sql

def additional_assign_check(sql):
    addlist = []
    for i in sql:
        if isinstance(i,list):
            continue
        if i == "order":
            if sql[sql.index(i)+1] == 'by':
                addlist.append(sql.index(i))
        if i == "group":
            if sql[sql.index(i)+1] == "by":
                addlist.append(sql.index(i))
        if i == "delete":
            if sql[sql.index(i)+1] == "from":
                addlist.append(sql.index(i))
        if i == "insert":
            if sql[sql.index(i)+1] == "into":
                addlist.append(sql.index(i))

    addlist.reverse()
    for i in addlist:
        sql[i] = sql[i]+" "+sql[i+1]
        del sql[i+1]
    
    return sql
        
def assign2root(sql,root):
    if root == "update":
        rootlist=[]
        rootstring=''
        assignindex=[]
        first = True
        rootindex = 0
        for i in sql:
            if isinstance(i,list):
                continue
            if i == "update":
                rootlist.append(i.upper())
                assignindex.append(sql.index(i))
                rootindex = sql.index(i)
            if i == "set":
                rootlist.append(i.upper())
                assignindex.append(sql.index(i))
            if i == "where":
                rootlist.append(i.upper())
                assignindex.append(sql.index(i))

        for i in range(0,len(assignindex)):
            if sql[assignindex[i]] == "update":
                sql[assignindex[i]] = "Table"
            if sql[assignindex[i]] == "set":
                sql[assignindex[i]] = "Column"
            if sql[assignindex[i]] == "where":
                sql[assignindex[i]] = "Condition"

        for i in range(0,len(assignindex)):
            if first is True:
                rootstring = rootlist[i]
                first = False
                continue
            rootstring = rootstring+' '+rootlist[i]

        sql.insert(rootindex,rootstring)
        
    elif root == "delete":
        rootlist=[]
        rootstring=''
        assignindex=[]
        first = True
        rootindex = 0
        for i in sql:
            if isinstance(i,list):
                continue
            if i == "delete from":
                rootlist.append(i.upper())
                assignindex.append(sql.index(i))
                rootindex = sql.index(i)
            if i == "where":
                rootlist.append(i.upper())
                assignindex.append(sql.index(i))

        for i in range(0,len(assignindex)):
            if sql[assignindex[i]] == "delete from":
                sql[assignindex[i]] = "Table"
            if sql[assignindex[i]] == "where":
                sql[assignindex[i]] = "Condition"

        for i in range(0,len(assignindex)):
            if first is True:
                rootstring = rootlist[i]
                first = False
                continue
            rootstring = rootstring+' '+rootlist[i]

        sql.insert(rootindex,rootstring)

    elif root == "insert":
        rootlist=[]
        rootstring=''
        assignindex=[]
        first = True
        rootindex = 0
        for i in sql:
            if isinstance(i,list):
                continue
            if i == "insert into":
                rootlist.append(i.upper())
                assignindex.append(sql.index(i))
                rootindex = sql.index(i)
            if i == "values":
                rootlist.append(i.upper())
                assignindex.append(sql.index(i))

        for i in range(0,len(assignindex)):
            if sql[assignindex[i]] == "insert into":
                sql[assignindex[i]] = "Table"
            if sql[assignindex[i]] == "values":
                sql[assignindex[i]] = "Value"

        for i in range(0,len(assignindex)):
            if first is True:
                rootstring = rootlist[i]
                first = False
                continue
            rootstring = rootstring+' '+rootlist[i]
            
    elif root == "select":
        rootlist=[]
        rootstring=''
        assignindex=[]
        first = True
        rootindex = 0
        rootflag = 0
        for i in sql:
#            print(i)                ##
            if isinstance(i,list):
                continue
            if i == "union":
                rootlist.append(i.upper())
                rootindex = sql.index(i)
                assignindex.append(sql.index(i))
                rootflag = -1
            if i == "select":
                rootlist.append(i.upper())
                assignindex.append(sql.index(i))
                if rootflag is 0:
                    rootindex = sql.index(i)
                    rootflag = 1
            if i == "from":
                rootlist.append(i.upper())
                assignindex.append(sql.index(i))
            if i == "where":
                rootlist.append(i.upper())
                assignindex.append(sql.index(i))
            if i == "group by":
                rootlist.append(i.upper())
                assignindex.append(sql.index(i))
            if i == "order by":
                rootlist.append(i.upper())
                assignindex.append(sql.index(i))
            if i == "having":
                rootlist.append(i.upper())
                assignindex.append(sql.index(i))

        for i in range(0,len(assignindex)):
            if sql[assignindex[i]] == "select":
                sql[assignindex[i]] = "Column"
            if sql[assignindex[i]] == "from":
                sql[assignindex[i]] = "Table"
            if sql[assignindex[i]] == "where":
                sql[assignindex[i]] = "Condition"
            if sql[assignindex[i]] == "order by":
                sql[assignindex[i]] = "Order column"
            if sql[assignindex[i]] == "group by":
                sql[assignindex[i]] = "Group option"
            if sql[assignindex[i]] == "having":
                sql[assignindex[i]] = "Having condition"

        for i in range(0,len(assignindex)):
            if first is True:
                rootstring = rootlist[0]
                first = False
                continue
            #print(i , len(assignindex))
            rootstring = rootstring+' '+rootlist[i]
#        print(rootlist)                ##
#        print(assignindex)              ##
#        print(rootstring)               ##
        if rootflag == -1 :
            del sql[rootindex]
        sql.insert(rootindex,rootstring)

    return sql

def child2list(sql,root):
    childlist=[]
    if root == "delete" :
        childlist = ['Table','Condition']
    elif root == "update":
        childlist = ['Table','Column','Condition']
    elif root == "select":
        childlist = ['Column','Table','Condition','Order column','Group option']
    elif root == "insert":
        childlist = ['Table','Value']
    child_flag = 0
    child_start = 0
    child_index = []
    dellist=[]
    for index in range(0,len(sql)):
        if child_flag == 1 and index == len(sql) - 1:
            child_flag = 0
            child_index.append([child_start,index])
            child_start = 0
#            print(1)            ##
        elif child_flag == 1 and sql[index] in childlist:
            child_flag = 0
            child_index.append([child_start,index -1])
            child_start = 0
#            print(2)            ##
        elif child_flag == 0 and sql[index] in childlist:
            child_flag = 1
            child_start = index + 1
#            print(3)            ##
    if child_index == []:
        return sql
        
    child_index.reverse()
    
    for i in child_index:
        sql[i[0]] = sql[i[0]:i[1]+1]
        del sql[i[0]+1:i[1]+1]
    ## child-child list complete
    for index in range(0,len(sql)):
        if sql[index] in childlist:
            sql[index] = sql[index:index+2]
            dellist.append(index+1)
    dellist.reverse()
    for i in dellist:
        del sql[i]
    ## make child list finished

    return sql

def and_or_check(sql):
    and_or_list=[]
    and_or_flag = False
    and_or_start=-1    
    for i in range(0,len(sql)):
        if and_or_flag:
            if sql[i] == "and" or sql[i] == "or":
                if i+1 == len(sql) -1:
                    and_or_flag = False
                    and_or_start = -1
                    continue
                and_or_list.append([and_or_start,i-1])
                and_or_start = i
            if i == len(sql)-1:
                and_or_list.append([and_or_start,i])
        if sql[i] == "and" or sql[i] == "or":
            and_or_start = i
            and_or_flag = True
        elif sql[i] == "order":
            if i != len(sql)-1:
                if sql[i+1] == "by":
                    and_or_start = i
                    and_or_flag = True

    and_or_list.reverse()
    for index in and_or_list:
        sql[index[0]] = sql[index[0]:index[1]+1]
        del sql[index[0]+1:index[1]+1]
    return sql

def sqlfilter(raw_string):
    string = raw_string.lower()
    sql = string.split()
    
    sql = splitcheck(sql)
    sql = and_or_check(sql)
    sql = parse(sql)
    
    #print(sql)
    return sql
