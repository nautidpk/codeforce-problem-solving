n,t=map(int,input().split(" "))
li=list(map(int,input().split(" ")))
i=0;ans="NO";lii=[1]
while(i<n-1):
    a=i+1+li[i]
    lii.append(a)
    i+=1
i=1;flag=True
while(flag):
    if lii[i] ==t:
        ans="YES"
        break
    i=lii[i]
    if i>=n:
        flag=False
        break;
print(ans)
