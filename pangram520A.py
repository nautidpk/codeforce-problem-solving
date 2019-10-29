n=int(input())
strInput=input().lower()
ans="YES"
alph="abcdefghijklmnopqrstuvwxyz"
i=0
for i in alph:
    if strInput.find(i)==-1:
        ans="NO"
print(ans)
