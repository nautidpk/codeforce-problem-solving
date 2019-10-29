import math
n=int(input())
ans=math.ceil(n/5)
ans=1 if ans==0 and n>0 else ans
print(ans)
