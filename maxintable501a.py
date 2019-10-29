# cook your dish here
dp=[[1]*10,[1]*10,[1]*10,[1]*10,[1]*10,[1]*10,[1]*10,[1]*10,[1]*10,[1]*10]
i=1;j=1
while(i<10):
    j=1
    while(j<10):
        dp[i][j]=dp[i-1][j]+dp[i][j-1]
        j+=1
    i+=1
n=int(input())
print(dp[n-1][n-1])

