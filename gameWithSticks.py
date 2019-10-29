n,m=map(int,input().split(" "))
ans=n if n<m else m
print("Malvika" if ans%2==0 else "Akshat")
