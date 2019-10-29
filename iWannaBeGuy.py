n=int(input())
s=list(map(int,input().split(" ")))
li=s[1:]
secInput=list(map(int,input().split(" ")))
sec=secInput[1:]
[li.append(i) for i in sec if i not in li]
print("I become the guy." if len(li)==n else "Oh, my keyboard!")
