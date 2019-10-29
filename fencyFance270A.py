# cook your dish here
t=int(input())
while(t>0):
    n=int(input())
    ext=180-n
    sides=360//ext
    print("YES" if sides*ext==360 else "NO")
    t-=1
