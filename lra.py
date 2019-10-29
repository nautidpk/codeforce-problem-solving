# your code goes here
l,r,a=map(int,input().split(" "))
ans=0
if l==r:
	ans=(l+r)+2*(a//2)
elif l<r:
	if a>(r-l):
		ans=2*r+2*((a-r+l)//2)
	else:
		ans=(l+a)*2
else:
	if a>(l-r):
		ans=2*l+2*((a-l+r)//2)
	else:
		ans=(r+a)*2
print(ans)
