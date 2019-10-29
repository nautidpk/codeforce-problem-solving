# your code goes here
n=int(input())
stones=input()
pre=stones[0]
count=0
for i in range(1,n):
	if stones[i]==pre:
		count+=1
	pre=stones[i]
print(count)
