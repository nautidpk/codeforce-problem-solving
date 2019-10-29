li,bob=map(int,input().split(" "))
count=0
while(li<=bob):
    li*=3
    bob*=2
    count+=1
print(count)
