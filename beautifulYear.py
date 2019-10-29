def isDistinct(year):
    l=[0]*10
    while(year>0):
        index=year%10
        l[index]+=1
        if(l[index]==2):
            return False
        year//=10
    return True
year=int(input())
flagi=True
while(flagi):
    year+=1
    if isDistinct(year):
        flagi=False
print(year)
