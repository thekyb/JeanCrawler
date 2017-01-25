import time
from urllib.request import urlopen
from dataDic import * 
from dataParser import * 
from queryExecuter import myQueryExecuter 

# Insert pvinsight tuple with date information
# try:
response = urlopen("http://www.sunsirs.com/uk/prodetail-463.html")
if 'text/html' in response.getheader('Content-Type'):
    html_bytes = response.read()
    html_string = html_bytes.decode("utf-8")
finder2 = sunsirs("http://www.sunsirs.com/uk/prodetail-463.html","http://www.sunsirs.com/uk/prodetail-463.html")
finder2.feed(html_string)
# print(finder2.dataList)
queryString = "INSERT INTO Sunsir VALUES('" + finder2.dataList[3] + "', " + finder2.dataList[2] + ");"
print(queryString)
QE = myQueryExecuter
QE.execute(QE, queryString)		
# except Exception:
    # print("Error during INSERT QUERY")
