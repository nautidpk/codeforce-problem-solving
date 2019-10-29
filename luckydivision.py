# your code goes here
strInput=input()
number=int(strInput)
ans="NO"
luckyno=[4,7,44,47,74,77,444,447,474,477,744,747,774,777]
if strInput.count('4')+strInput.count('7')==len(strInput):
	ans="YES"
for i in luckyno:
	if number%i==0 :
		ans="YES"
print(ans)
