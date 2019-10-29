# your code goes here
m,n=map(int,input().split(" "))
ans=0
if m>1:
	remaining=m%2
	ans=(n*(m//2))
	if remaining==1:
		ans+=n//2
elif n>1:
	remaining=n%2
	ans=(m*(n//2))
	if remaining==1:
		ans+=m//2
print(ans)
