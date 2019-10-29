n=int(input())
li=list(map(int,input().split(" ")))
maxi=max(li)
cnt=[0]*(maxi+1)
dp=[0]*(maxi+1)
i=0;j=2
while(i<n):
    cnt[li[i]]+=1
    i+=1
dp[0]=cnt[0];dp[1]=cnt[1]
while(j<=maxi):
    dp[j]=max(dp[j-2]+(cnt[j]*j),dp[j-1])
    j+=1
print(dp[maxi])
