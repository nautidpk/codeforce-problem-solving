# cook your dish here
def are_all_zeros(a):
    for i in range(len(a)):
        for j in range(len(a[0])):
            if(a[i][j]==1):
                return -1
    return 1


def main():
    n,m=map(int,input().split())
    a=[];i=0
    while(i<n):
        a.append(list(map(int,input().split(" "))))
        i+=1
    steps=0;i=0
    ans=[]
    for i in range(n-1):
        for j in range(m-1):
            if(a[i][j] *a[i][j+1]*a[i+1][j]*a[i+1][j+1]>0):
                steps+=1
                a[i][j]=2
                a[i+1][j]=2
                a[i][j+1]=2
                a[i+1][j+1]=2
                ans.append([i+1,j+1])
    result=are_all_zeros(a)
    if(result==-1):
        print('-1')
    else:
        print(steps)
        for i in ans:
            print(str(i[0])+' '+str(i[1]))
main()
