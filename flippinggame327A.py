# cook your dish here
n=int(input())
li=list(map(int,input().split(" ")))
count=0;si=0;no=0;m=0;j=0;ei=0;bm=0;am=0
for i in li:
    if(i==0):
        count+=1
    else:
        no+=1
        count-=1
        am+=1
        bm+=1
    if(count<=0):
        si=j+1
        count=0
        bm=0
    if(count>m):
        m=count
        ei=bm
        am=0
    j+=1
if(no==n):
    print(n-1)
else:
    bm=no-ei
    print(m+bm+ei)
