n,t=map(int,input().split(" "))
digit="1"
if(t==10 and n==1):
    print("-1")
else:
    if(t==10):
        n-=1
    digit*=n
    print(t*(int(digit)))
