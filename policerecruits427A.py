t=int(input())
li=list(map(int,input().split(" ")))
i=0;police=0;crimes=0
while(i<t):
    if(li[i]==-1):
        police-=1
        if(police<0):
            police=0
            crimes+=1
    else:
        police+=li[i]
    i+=1
print(crimes)
