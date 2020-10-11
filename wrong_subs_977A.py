#problem - https://codeforces.com/problemset/problem/977/A
n,k=map(int,input().split())
while(k>0):
    lst_dgt=n%10
    if(lst_dgt>0):
        n-=1
    else:
        n=n//10
    k-=1
print(n)