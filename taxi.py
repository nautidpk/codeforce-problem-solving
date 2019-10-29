n=int(input())
studentgroup=sorted(list(map(int,input().split(" "))),reverse=True)
cur=0;total=0;first=0;last=n-1
while(first<=last):
	if studentgroup[first]==4:
		total+=1
		first+=1
	elif studentgroup[first]==3:
		first+=1
		if studentgroup[last]==1:
			total+=1
			last-=1
		else:
			total+=1
	else:
		cur+=studentgroup[first]
		first+=1
		if cur==4:
			cur=0
			total+=1
if cur>0:
	total+=1
print(total)
