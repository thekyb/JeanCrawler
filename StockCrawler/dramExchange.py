import time
from urllib.request import urlopen
from dataDic import * 
from dataParser import * 
from queryExecuter import myQueryExecuter 

# Insert pvinsight tuple with date information
try:
    queryString = "INSERT INTO pvinsight (Dateinfo) VALUES('"+ time.strftime("%Y-%m-%d") + "');"
    print(queryString)
    QE = myQueryExecuter
    QE.execute(QE, queryString)		
except Exception:
    print("Error during INSERT QUERY")
# get whole pvinside html data from A url
response = urlopen("http://pvinsights.com/")
if 'text/html' in response.getheader('Content-Type'):
    html_bytes = response.read()
    pvInsight_string = html_bytes.decode("utf-8")


infoTypeList = ["High", "Low", "Average", "AvgChg", "AvgChgPersent"]
mParse = parsePvInsight("http://pvinsights.com/","http://pvinsights.com/")

# find data from html and organize 
for elements in pvInsight_data:
    
    mParse.setKey(elements)
    mParse.feed(pvInsight_string)
    # print(mParse.dataList)
    print(len(mParse.dataList))
    print(mParse.itemCount)
    if len(mParse.dataList) == mParse.itemCount:
        queryString = "UPDATE pvinsight SET " 
        queryString = queryString + elements + "_High = " + mParse.dataList[0] + ", "
        queryString = queryString + elements + "_Low= " + mParse.dataList[1] + ", "
        queryString = queryString + elements + "_Average = " + mParse.dataList[2] + ", "
        queryString = queryString + elements + "_AvgChg = " + mParse.dataList[3] + ", "
        queryString = queryString + elements + "_AvgChgPersent = " + mParse.dataList[4]  
        queryString = queryString + " Where Dateinfo = '" + time.strftime("%Y-%m-%d") + "'"
        queryString = queryString.replace('%', '')
        print(queryString)
        QE.execute(QE, queryString)		

        mParse.dataList = []
        mParse.itemSeq = 0

	
	
#         # ask special information from that html data
#         # make quary string for each data string 
#         # put it into mysql db


# # get whole sunsir html data from A url

# # find data from html and organize 

# #         ask special information from that html data
# #         make quary string for each data string 
# #         put it into mysql db


# # get whole dramexchange html data from A url

# # find data from html and organize 

# #         ask special information from that html data
# #         make quary string for each data string 
# #         put it into mysql db
