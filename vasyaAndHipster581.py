# cook your dish here
a,b=map(int,input().split(" "))
ans1=a if a<b else b
ans2=(a-ans1+b-ans1)//2
print(ans1,ans2,sep=" ")
