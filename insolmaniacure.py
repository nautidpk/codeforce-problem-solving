pa=int(input())
pb=int(input())
pc=int(input())
pd=int(input())
a=pa;b=pb;c=pc;d=pd
n=int(input())
flaga=True
count=0
l=[0]*(n+1)
while(flaga):
    if a<=n:
        l[a]+=1
    if a<=n and l[a]==1:
        count+=1
    if b<=n:
        l[b]+=1
    if b<=n and  l[b]==1:
        count+=1
    if c<=n:
        l[c]+=1
    if c<=n and  l[c]==1:
        count+=1
    if d<=n:
        l[d]+=1
    if d<=n and l[d]==1:
        count+=1
    a+=pa;b+=pb;c+=pc;d+=pd
    if a>n and b>n and c>n and d>n:
        flaga=False
print(count)

