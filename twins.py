# cook your dish here
n=int(input())
candy=sorted(list(map(int,input().split(" "))))
sumc=sum(candy)
count=0;last=n-1;flag=0;suma=0
while(last>=0 and flag==0):
    suma+=candy[last]
    last-=1
    count+=1
    if suma>(sumc//2):
        flag=1
print(count)
