n,m=map(int,input().split(" "))
lH=list(map(int,input().split(" ")))
i=0;ans=0;curH=1
while i<m:
    if curH==lH[i]:
        ans+=0
    elif curH<lH[i]:
        ans+=lH[i]-curH
    else:
        ans+=n-curH+lH[i]
    curH=lH[i]
    i+=1
print(ans)
