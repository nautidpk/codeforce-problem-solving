def returnOdd(li):
    i=0;co=0;ce=0;cei=0;coi=0
    while(i<len(li)):
        if li[i]%2==1:
            co+=1
            coi=i+1
        else:
            ce+=1
            cei=i+1
        
        i+=1
    return cei if ce==1 else coi
n=int(input())
li=list(map(int,input().split(" ")))
print(returnOdd(li))
