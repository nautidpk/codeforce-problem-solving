remainder=240
n,k=map(int,input().split(" "))
count=0;i=1
remainder-=k
while(i<=n):
    remainder-=i*5
    if(remainder<0):
        break
    count+=1
    i+=1
print(count)
