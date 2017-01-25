
# myList1 = [0] *1000
# myList2 = [0] *5

# for num in range(5):
#     myList1[num] = input("What is your first name? : ")
#     myList2[num] =input("What is your last name? : ")
#     # myList1.append( input("What is your first name? : "))
#     # myList2.append(input("What is your last name? : "))


# for num in range(5):
#     print(str(myList1[num]) + "   " + str(myList2[num]))


# myDic = {}

# for num in range(5):
#     myDic[num] = [input("What is your first name? : "),input("What is your last name? : ")]


# # myDic[1]= [a,b,c,d]
# # myDic[2]= [e,f,r,c]
# for num in range(5):
#     print(str(myDic[num][0]) + "   " + str(myDic[num][1]))

myStr = []
for num in range(5):
    myStr.append(input("input your string: ").upper().strip())

myStar = "";
myBlank = "";

mymaxlen = 0
for num in range(len(myStr)):
    if mymaxlen < len(myStr[num]):
        mymaxlen = len(myStr[num])

for idx in range(mymaxlen + 7):
    myStar = myStar + "*" 

print("")
print(myStar)
for num in range(len(myStr)):
    myBlank = ""
    for idx in range(mymaxlen- len(myStr[num])):
        myBlank = myBlank + " "
    print ("* " + myStr[num] + myBlank + "    *")
# for num in range(len(myStr)):
#     print ("* " + myStr[num] +"    *")

print(myStar)


