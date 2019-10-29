n,m=map(int,input().split(" "))
i=1
snake='#';empt='.'
while(i<=n):
    if i%2==1:
        print(snake*m);
    elif i%4==0:
        print(snake+empt*(m-1))
    else:
        print(empt*(m-1)+snake)
    i+=1
