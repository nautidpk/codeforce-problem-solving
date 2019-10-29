n,h=map(int,input().split(" "))
li=list(map(int,input().split(" ")))
i=0;ans=0
while(i<n):
    if li[i]>h:
        ans+=1
    ans+=1
    i+=1
print(ans)
