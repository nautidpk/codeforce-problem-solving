n,m,a,b=map(int,input().split(" "))
if b/m<=a:
    ridet=(n//m)*b
    ridet=min(ridet+(n%m)*a,ridet+b)
    print(ridet)
else:
    print(n*a)
