from math import ceil 
def isTriPrime(n):
    i=2;primeCount=2
    while(i*i<=n):
        if(n%i==0):
            ans=1 if n//i==i else 2
            primeCount+=ans
        if(primeCount>3):
            break
        i+=1
    return primeCount==3
t=int(input())
li=list(map(int,input().split(" ")))
for i in li:
    if(isTriPrime(i)):
        print("YES")
    else:
        print("NO")
