petystr=input()
newstr=petystr.replace("WUB"," ").split(" ")
oStr=[i for i in newstr if i!=""]
n=len(oStr);i=0
while i<n:
    if i<n-1:
        print(oStr[i],end=" ")
    else:
        print(oStr[i],end="")
    i+=1
