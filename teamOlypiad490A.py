n=int(input())
li=list(map(int,input().split(" ")))
l1=[];l2=[];l3=[];count=0
for i in li :
    if(i==1):
        l1.append(count+1)
    elif (i==2):
        l2.append(count+1)
    else:
        l3.append(count+1)
    count+=1
minlen=min(len(l1),len(l2),len(l3))
print(minlen)
count=0
while(count<minlen):
    print(l1[count],l2[count],l3[count],sep=" ")
    count+=1
