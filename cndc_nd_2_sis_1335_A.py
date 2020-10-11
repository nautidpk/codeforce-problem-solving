#prob - https://codeforces.com/problemset/problem/1335/A
t=int(input())
while(t>0):
    n=int(input())
    half = n//2
    total_ways = (n -1 - half)
    print(total_ways)
    t-=1