import sys
from urllib.request import urlopen
from petronet import *

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        # f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        f = lambda obj: str(obj).encode(enc, errors='ignore').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

# uprint('foo')
# uprint(u'Antonín Dvořák')
# uprint('foo', 'bar', u'Antonín Dvořák')


# response = urlopen("http://www.petronet.co.kr/v3/index.jsp")
# if 'text/html' in response.getheader('Content-Type'):
#     html_bytes = response.read()
#     html_string = html_bytes.decode("utf-8","ignore")
    # print(html_string)
    # uprint(html_string)
with open('test2.html', 'r') as content_file:
    content = content_file.read()
    # html_string = content.decode("utf-8","ignore")
# print(content)
mParse = parsePetronet1("http://www.petronet.co.kr/v3/index.jsp","http://www.petronet.co.kr/v3/index.jsp")
mParse.feed(html_string)

# for elements in pvInsight_data:
#     # print (pvInsight_data['2nd_Grade_Poly_Silicon_Price'][0])
#     # print (pvInsight_data['2nd_Grade_Poly_Silicon_Price'][1])
#     # mParse2 = pvInsight("http://pvinsights.com/","http://pvinsights.com/")
    
#     # mParse.setKey('ThinFilm_Solar_Module')
#     mParse.setKey(elements)
#     mParse.feed(pvInsight_string)
    
#     if len(mParse.dataList) == mParse.itemCount:
#         print(mParse.dataList)
#         QueryString = "UPDATE pvinsight SET " 
#         QueryString = QueryString + elements + "_High = " + mParse.dataList[0] + ", "
#         QueryString = QueryString + elements + "_Low= " + mParse.dataList[1] + ", "
#         QueryString = QueryString + elements + "_Average = " + mParse.dataList[2] + ", "
#         QueryString = QueryString + elements + "_AvgChg = " + mParse.dataList[3] + ", "
#         QueryString = QueryString + elements + "_AvgChgPersent = " + mParse.dataList[4]  
#         QueryString = QueryString + " Where Dateinfo = '" + time.strftime("%Y-%m-%d") + "'"


#         print(QueryString)

#         mParse.dataList = []
#         mParse.itemSeq = 0

