# cook your dish here
n=int(input())
li=list(map(int,input().split(" ")))
m=max(li)
s=0
for i in li:
    s+=m-i
print(s)
