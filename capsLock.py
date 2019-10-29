strInput=input()
if len(strInput)==1:
	if strInput==strInput.lower():
		print(strInput.upper())
	else:
		print(strInput.lower())
elif strInput.upper()==strInput or (strInput[0].lower()+strInput[1:].upper())==strInput:
	print(strInput.capitalize() if strInput[0].lower()==strInput[0] else strInput.lower())
else:
	print(strInput)
