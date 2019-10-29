strA=input()
upper=0;lower=0
for st in strA:
    if st.isupper():
        upper+=1
    else:
        lower+=1
print(strA.lower() if lower>=upper else strA.upper())
