k,r=map(int,input().split(" "))
flag=True;i=1
while(flag):
    if k*i%10==0 or (k*i-r)%10==0:
        flag=False
        break
    i+=1
print(i)
