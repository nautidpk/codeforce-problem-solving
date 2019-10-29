n=int(input())
hate="I hate"
love="I love"
print(hate+" it" if n==1 else hate,end=" ")
i=2
while(i<=n):
    if i!=n:
        print("that "+hate if i%2==1 else "that "+love,end=" ")
    else :
        print("that "+hate+" it" if i%2==1 else "that "+love+" it")
    i+=1
