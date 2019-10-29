n=int(input())
scores=list(map(int,input().split(" ")))
worst=scores[0];best=scores[0];i=1;count=0
while(i<n):
    if scores[i]>best:
        best=scores[i]
        count+=1
    elif scores[i]<worst:
        worst=scores[i]
        count+=1
    i+=1
print(count)
