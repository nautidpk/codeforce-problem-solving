n,k=map(int , input().split(" "))
l=list(map(int,input().split(" ")))
count=0
maxlimit=l[k-1]
for i in l:
	if i>=maxlimit and i>0:
		count+=1
print(count)
