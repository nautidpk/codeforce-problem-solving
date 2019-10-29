strA=input()
strB=input()
n=len(strB)
i=0;ans=""
while(i<n):
    if strB[i]!=strA[i]:
        ans+="1"
    else:
        ans+="0"
    i+=1
print(ans)
