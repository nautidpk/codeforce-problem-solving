# your code goes here
n=int(input())
ans=0
while(n>0):
	operation=input()
	if operation.find("+")>-1:
		ans+=1
	else:
		ans-=1
	n-=1
print(ans)
