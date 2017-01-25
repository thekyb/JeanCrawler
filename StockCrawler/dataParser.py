from dataDic import *
from html.parser import HTMLParser
from funcs import *


class parsePvInsight(HTMLParser):

    catchData = False
    DataFlag = False
    dataKey = ''
    dataList = []
    itemCount = 0   
    itemSeq = 0


    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def setKey(self, key): 
        self.dataKey = pvInsight_data[key][0]
        print(self.dataKey)
        self.dataNegKey = pvInsight_data[key][1]
        print(self.dataNegKey)
        self.itemCount = pvInsight_data[key][2]
        print(self.itemCount)
    def handle_starttag(self, tag, attrs):
        if tag == 'b' and self.DataFlag == True:
            self.catchData = True
    # def handle_endtag(self, tag):
    #     pass
    # def handle_endtag(self, tag):
    #     if self.DataFlag == True:
    #         if tag == 'b':
    #             self.catchData = False
    #         # if tag == 'td':

    #         #     if self.meetTd == 5:
    #         #         self.meetTd = 0
    #         #         self.DataFlag = False
    #         #         self.itemSeq = self.itemSeq+1

    def handle_endtag(self, tag):
        if tag == 'b':
            self.catchData = False

    def handle_data(self, data):
        if checkData(data, self.dataKey, self.dataNegKey):
            self.DataFlag = True
        if self.catchData == True:
            # self.dataList[(self.itemSeq+1)*(self.infoTypeSeq +1)-1] = data
            self.dataList.append(data)
            self.itemSeq = self.itemSeq +1
            if self.itemSeq == self.itemCount:
                self.DataFlag = False
 
    def page_links(self):
        return self.link

    def error(self, message):
        pass

class sunsirs(HTMLParser):

    DataFlag = 0
    meetTd = False
    catchData = False
    # itemList = [ "Comodity", "Price", "Date"]
    dataList = list()
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    # When we call HTMLParser feed() this function is called when it encounters an opening tag <a>
    def handle_starttag(self, tag, attrs):
        if self.catchData == False:
            if tag == 'td':
                self.meetTd = True

    def handle_data(self, data):
        # print(self.itemList[self.itemSeq])
        if self.meetTd == True:
            if data == "Polysilicon":
                self.dataList.append(data)
                self.DataFlag = 1
                print("=======>1 : " + data)
            elif self.DataFlag == 1:
                self.dataList.append(data)
                self.DataFlag = 2
                print("=======>2 : " + data)
            elif self.DataFlag == 2:
                self.dataList.append(data)
                self.DataFlag = 3
                print("=======>3 : " + data)
            elif self.DataFlag == 3:
                self.dataList.append(data)
                self.DataFlag = 0
                self.catchData = True
                self.meetTd = False
                print("=======>4 : " + data)
                    


