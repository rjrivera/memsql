import glob, os

path = "home/ubuntu/dbinput"
print "Currently in %s" % path
serverDomain = "MasterAggregator"
recordValues = [0,'0', 'asd', 3, 'asdfjk', 'asd']
workFile = open('generateData.txt', 'w')
for record in range(0, 349999999):
    recordValues[0] = record
    recordValues[1] = '\'abd' + str(random.randint(1, 999)) + 'cb' +str(random.randint(1,99)) + '\''
    recordValues[2] = '\'' + str(random.randint(1,999)) + '\''
    recordValues[3] = random.randint(1,7)
    recordValues[4] = 'mac' + str(random.randint(1, 999999))
    recordValues[5] = random.randint(1,9999)
    sql = 'INSERT INTO SCANS (SCAN_ID, SCAN_HASH, SCAN_TYPE, SCAN_COUNT, MACHING_TYPE, SEQUENCE_CODE) VALUES ('
    sql += str(recordValues[0]) + ',' 
    sql += str(recordValues[1]) + ','
    sql += str(recordValues[2]) + ','
    sql += str(recordValues[3]) + ','
    sql += str(recordValues[4]) + ','
    sql += str(recordValues[5]) + ');\n'
    print("\n")
    print(sql)
    workFile.write(sql)


