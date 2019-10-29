n,m=map(int,input().split(" "))
nm=n;ans=0
while(nm>=m):
    ans2=nm//m
    ans+=ans2
    nm=(nm%m+ans2)
print(n+ans)
