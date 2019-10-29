n=int(input())
moneylist=list(map(int,input().split(" ")))
start=1;maxm=1;count=1;
while(start<n):
    if moneylist[start]>=moneylist[start-1]:
        count+=1
    else:
        count=1
    if count>maxm:
        maxm=count
    start+=1
print(maxm)
