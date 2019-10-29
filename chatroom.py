strInput=input().lower()
ans="NO"
n=len(strInput)-1
h1=strInput.find('h')
if h1>-1 and h1!=n:
	e1=strInput.find('e',h1+1)
	if e1>-1 and e1!=n:
		h1=strInput.find('l',e1+1)
		if h1>-1 and h1!=n:
			e1=strInput.find('l',h1+1)
			if e1>-1 and e1!=n:
				h1=strInput.find('o',e1+1)
				if h1>-1:
					ans="YES"
print(ans)
