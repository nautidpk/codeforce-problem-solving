# cook your dish here
n=input()
totalc=str(n.count("4")+n.count("7"))
if totalc.count("4")+totalc.count("7")==len(totalc):
    print("YES")
else:
    print("NO")
