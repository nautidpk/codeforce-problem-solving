n=int(input())
cubes=0;start=1;flag=True
while(flag):
    cubes+=(start*(start+1))//2
    if cubes>n:
        start-=1
        flag=False
        break
    start+=1
print(start)
