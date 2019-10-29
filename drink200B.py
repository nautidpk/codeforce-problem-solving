n=int(input())
pO=list(map(int,input().split(" ")))
result=0.0;i=0
while(i<n):
    result+=(pO[i]/100)
    i+=1
print('{0:.12f}'.format((result/n)*100))
