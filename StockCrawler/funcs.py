import sys
from urllib.request import urlopen

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='ignore').decode(enc)
        # f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)

def uString(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        return objects
    else:
        f = lambda obj: str(obj).encode(enc, errors='ignore').decode(enc)
        # f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        return str(*map(f, objects))

def checkData(data, positiveTocken, negativeTocken):
    # if len(data) > 3:
            # print(data[0] + data[1] + data[2])

    myPosList = positiveTocken.split()
    myNegList = negativeTocken.split()
    allWordsAreIn = True
    for word in myPosList:
        if word in data:
            continue
        else :
            allWordsAreIn = False
            break;
    if allWordsAreIn:
            for word in myNegList:
                if word in data:
                    allWordsAreIn = False
                    break;
                else :
                    continue
     
    if allWordsAreIn:
        print("test!! test ==> " + data)
        return True
    return False

    # correctCount = 0
    # spaceCount = 0
    # for c in data:
    #     if c == ' ':
    #         spaceCount = spaceCount + 1
    #         correctCount = correctCount + 1

    # # print(str(correctCount))
    # # print(len(data2))
    # # print(spaceCount)
    # # if len(data) > 5:
    #         # print('!!' + data[0] + data[1] + data[2] + data[3] + data[4] + '!!')
    # # print('!!' + data2 + '!!')
    # if correctCount == len(data) and spaceCount != correctCount:
    #     print("test!! test")
    #     if len(data) > 5:
    #         print('!!' + data[0] + data[1] + data[2] + data[3] + data[4] + '!!')
    #     print(data)
    #     return True
    # return False

# print(checkData('tttt', 'test123'))
