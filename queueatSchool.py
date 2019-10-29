# cook your dish here
n,t=map(int,input().split(" "))
stri=input()
while t>0:
    stri=stri.replace("BG","GB")
    t-=1
print(stri)
