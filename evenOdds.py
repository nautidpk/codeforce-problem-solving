n,k=map(int,input().split(" "))
nOdd=0;nEven=0
if n%2==0:
    nOdd=n//2
    nEven=n//2
else:
    nOdd=n//2+1
    nEven=nOdd-1
ans=0
if k<=nOdd:
    ans=1+(k-1)*2
else:
    k-=nOdd
    ans=2+(k-1)*2
print(ans)
