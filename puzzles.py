n,m=map(int,input().split(" "))
puzzles=sorted(list(map(int,input().split(" "))))
start=0;mind=40004
while n<=m:
    diff=puzzles[n-1]-puzzles[start]
    if diff<mind:
        mind=diff
    n+=1
    start+=1
print(mind)
    
