strInput=input()
leng=len(strInput)
strI=strInput[1:leng-1].split(", ")
finalList=[]
[finalList.append(i) for i in strI if i not in finalList]
if len(strInput)==2:
    print("0")
else:
    print(len(finalList))
