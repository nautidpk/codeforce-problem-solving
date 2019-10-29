n=int(input())
max=0;sum=0
while(n>0):
	exist,entp=map(int,input().split(" "))
	sum+=(entp-exist)
	if sum>max:
		max=sum
	n-=1
print(max)
