n=int(input())
i=0
home=[];guest=[]
while(i<n):
    a,b=map(int,input().split(" "))
    home.append(a)
    guest.append(b)
    i+=1
ans=0
for i in home:
    ans+=guest.count(i)
print(ans)
