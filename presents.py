n=int(input())
petyfriends=list(map(int,input().split(" ")))
i=0
ans=[0]*n
while i<n:
    ans[petyfriends[i]-1]=i+1
    i+=1
i=0
while i<n:
    print(ans[i],end=" ")
    i+=1
