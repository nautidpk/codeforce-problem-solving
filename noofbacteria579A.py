def no_of_bact(n):
    count=0
    while(n>0):
        if(n%2==1):
            count+=1
        n//=2
    return count
n=int(input())
print(no_of_bact(n))
