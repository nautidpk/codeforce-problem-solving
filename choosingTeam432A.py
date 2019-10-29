# cook your dish here
n,k=map(int,input().split(" "))
li=list(map(int,input().split(" ")))
i=0;count=0
while(i<n):
    if li[i]+k<=5:
        count+=1
    i+=1
print(count//3)
