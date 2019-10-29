n=int(input())
while n>0:
	myInput=input()
	if len(myInput)>10:
		ans=myInput[0]+str(len(myInput)-2)+myInput[len(myInput)-1]
		print(ans)
	else:
		print(myInput)
	n-=1
