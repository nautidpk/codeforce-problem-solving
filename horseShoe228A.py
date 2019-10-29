a=list(map(int,input().split(" ")))
ans=0
l=[]
[l.append(i) for i in a if i not in l]
if len(l)==4:
    ans=0
else:
    ans=4-len(l)
print(ans)

