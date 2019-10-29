# cook your dish here
nf=int(input())
sumx=0;sumy=0;sumz=0
while(nf>0):
    x,y,z=map(int,input().split(" "))
    sumx+=x;sumy+=y;sumz+=z
    nf-=1
print("YES" if sumx==0 and sumy==0 and sumz==0 else "NO")
