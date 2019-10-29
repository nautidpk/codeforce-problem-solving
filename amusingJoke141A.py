str1=input()
str2=input()
strf=''.join(sorted(str1+str2))
totalLTwo=len(str2)+len(str1)
strFinal=''.join(sorted(input()))
totalL=len(strFinal)
ans="YES"
if totalL>totalLTwo:
    ans="NO"
elif strFinal != strf:
    ans="NO"
print(ans)
