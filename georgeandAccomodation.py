# cook your dish here
n=int(input())
ans=0
while n>0:
    p,q=map(int,input().split(" "))
    if q-p>=2:
        ans+=1
    n-=1
print(ans)
