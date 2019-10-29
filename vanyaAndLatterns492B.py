n,l=map(int,input().split(" "))
light=sorted(map(int,input().split(" ")))
mz=light[0];ml=light[n-1]-l
mz*=2;ml*=2
ml=-ml if ml<0 else ml
maxD=0;i=1
while(i<n):
    d=light[i]-light[i-1]
    if d>maxD:
        maxD=d;
    i+=1
maximum=maxD if maxD>=mz and maxD>=ml else (ml if ml > mz else mz)
print('{0:.10f}'.format(maximum/2))
