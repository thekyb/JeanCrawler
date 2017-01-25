import time
from urllib.request import urlopen
from dataDic import * 
from dataParser import * 
from queryExecuter import myQueryExecuter 
from funcs import *

class parsePetronet2(HTMLParser):

    findDiv = False
    dataInfoStr = ""
    Location = ""

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_data(self, data):
        pass
    def handle_starttag(self, tag, attributes):
        # print("this is test===============")
        # print(tag)
        if self.findDiv == True:
            self.findDiv = False
            if tag == 'dt':
                for name, value in attributes:
                    if name == "class" and value == 'gasoline':
                        self.dataInfoStr = 'gasoline'
                        return
            elif tag == 'dd' and self.dataInfoStr != '':
                print(self.get_starttag_text())
        elif tag != 'div': return
        for name, value in attributes:
            if name == 'id' and value == 'today_oil_c3': # Domestic Oil price
                Location = "domestic"
                self.findDiv = True
                return 
                
            elif name == 'id' and value == 'today_oil_c4': # Domestic Oil price
                Location = "worldwide"
                self.findDiv = True
                return 
        
    def page_links(self):
        return self.link

    def error(self, message):
        pass

class parsePetronet1(HTMLParser):

    DataFlag = ""
    dataDic = {} 

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def handle_starttag(self, tag, attributes):
        print(tag)
    # def handle_data(self, data):
        # uprint(data)
        # print("================================")
        # if data in ("Dubai" ,"WTI (NYMEX)", "Brent (ICE)"):
        #     self.DataFlag = data
        #     # print(" test ==> " + data)
        #     return
        # if self.DataFlag != "":
        #     # print("Found data ==> " + data)
        #     self.dataDic[self.DataFlag] = [data]
        #     self.DataFlag = ""
    def page_links(self):
        return self.link

    def error(self, message):
        pass
        
# Insert pvinsight tuple with date information


response = urlopen("http://www.petronet.co.kr/v3/index.jsp")
if 'text/html' in response.getheader('Content-Type'):
    html_bytes = response.read()
    encode =  html_bytes
    # html_string = html_bytes.decode("utf-8")
    html_string = html_bytes.decode("utf-8", 'ignore')
    # uString = uString(html_string)
    # html_uString = uprint(html_string)
    # print(uString)
mParse = parsePetronet1("http://www.petronet.co.kr/v3/index.jsp","http://www.petronet.co.kr/v3/index.jsp")
# mParse.feed(html_string)




# try:
#     queryString = "INSERT INTO pvinsight (Dateinfo) VALUES('"+ time.strftime("%Y-%m-%d") + "');"
#     print(queryString)
#     QE = myQueryExecuter
#     QE.execute(QE, queryString)		
# except Exception:
#     print("Error during INSERT QUERY")
# # get whole pvinside html data from A url
# response = urlopen("http://pvinsights.com/")
# if 'text/html' in response.getheader('Content-Type'):
#     html_bytes = response.read()
#     pvInsight_string = html_bytes.decode("utf-8")


# infoTypeList = ["High", "Low", "Average", "AvgChg", "AvgChgPersent"]
# mParse = parsePetronet2("http://pvinsights.com/","http://pvinsights.com/")

# # find data from html and organize 
# for elements in pvInsight_data:
    
#     mParse.setKey(elements)
#     mParse.feed(pvInsight_string)
#     # print(mParse.dataList)
#     print(len(mParse.dataList))
#     print(mParse.itemCount)
#     if len(mParse.dataList) == mParse.itemCount:
#         queryString = "UPDATE pvinsight SET " 
#         queryString = queryString + elements + "_High = " + mParse.dataList[0] + ", "
#         queryString = queryString + elements + "_Low= " + mParse.dataList[1] + ", "
#         queryString = queryString + elements + "_Average = " + mParse.dataList[2] + ", "
#         queryString = queryString + elements + "_AvgChg = " + mParse.dataList[3] + ", "
#         queryString = queryString + elements + "_AvgChgPersent = " + mParse.dataList[4]  
#         queryString = queryString + " Where Dateinfo = '" + time.strftime("%Y-%m-%d") + "'"
#         queryString = queryString.replace('%', '')
#         print(queryString)
#         QE.execute(QE, queryString)		

#         mParse.dataList = []
#         mParse.itemSeq = 0

	
	
# #         # ask special information from that html data
# #         # make quary string for each data string 
# #         # put it into mysql db


# # # get whole sunsir html data from A url

# # # find data from html and organize 

# # #         ask special information from that html data
# # #         make quary string for each data string 
# # #         put it into mysql db


# # # get whole dramexchange html data from A url

# # # find data from html and organize 

# # #         ask special information from that html data
# # #         make quary string for each data string 
# # #         put it into mysql db
