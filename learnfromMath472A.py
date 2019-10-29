n=int(input())
ans1=0;ans2=0
if n%2==0:
    ans1=4
    ans2=n-4
else:
    ans1=9
    ans2=n-9
print(ans1,ans2,sep=" ")
