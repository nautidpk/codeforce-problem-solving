n=int(input())
strInput=input()
nA=strInput.count("A")
nD=strInput.count("D")
if nD==nA:
    print("Friendship")
elif nD<nA:
    print("Anton")
else:
    print("Danik")
