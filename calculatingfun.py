import math
def calc(a,b):
    totaln=math.ceil(b/2)
    return (totaln*a+totaln*b)//2
n=int(input())
ans=(calc(2,n)-calc(1,n-1)) if n%2==0 else (calc(2,n-1)-calc(1,n))
print(ans)
