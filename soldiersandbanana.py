# cook your dish here
k,n,w=map(int,input().split(" "))
sumap=(w*(w+1))//2
sumap*=k
ans=0 if w==0 else (sumap-n)
print(ans if ans>0 else 0)
