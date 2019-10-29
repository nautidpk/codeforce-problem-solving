from math import ceil
n,x=map(int,input().split(" "))
i=1;count=0
while(i<=n):
    if(x%i==0 and x//i<=n):
        count+=1
    i+=1
print(count)
