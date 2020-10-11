#prob - https://codeforces.com/problemset/problem/1328/A
t=int(input())
while(t>0):
    a,b=map(int,input().split())
    mod_a_k=a%b
    print(0 if mod_a_k ==0 else (b-mod_a_k))
    t-=1