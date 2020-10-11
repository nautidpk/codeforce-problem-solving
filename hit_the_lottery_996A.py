#prob - https://codeforces.com/problemset/problem/996/A
denomination = [100,20,10,5,1]
n = int(input())
used_denomination = 0
for i in denomination:
    if(i<=n):
        used_denomination += n//i
        n = n%i
    if(n==0):
        break
print(used_denomination)