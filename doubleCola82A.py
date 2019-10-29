import math
n=int(input())
l=['Sheldon','Leonard','Penny','Rajesh','Howard']
cur=5;curcoc=1;pre=5
while(cur<n):
    n-=cur
    curcoc*=2
    cur*=2
if n==0:
    print("Howard")
else:
    ind=math.ceil(n/curcoc)-1
    print(l[ind])
