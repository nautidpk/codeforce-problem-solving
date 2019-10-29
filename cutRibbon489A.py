n,a,b,c=map(int,input().split(" "))
i=min(a,min(b,c))+1
dp=[0]*(4001)
dp[a]=1;dp[b]=1;dp[c]=1
if dp[n]==-1:
    print("1")
else:
    while(i<=n):
        maxa=dp[i-a] if i-a>=0 else -1
        maxb=dp[i-b] if i-b>=0 else -1
        maxc=dp[i-c] if i-c>=0 else -1
        old=dp[i]
        dp[i]=max(maxa,maxb,maxc)
        dp[i]=dp[i]+1 if dp[i]>0 else old
        i+=1
    print(dp[n])
