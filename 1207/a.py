# cook your dish here
def main():
    t=int(input())
    while(t>0):
        b,p,f=map(int,input().split(" "))
        h,c=map(int,input().split(" "))
        profit=0
        if(b>1):
            if(h>c):
                minimum=b//2
                if(minimum>p):
                    minimum=p
                b-=(minimum*2)
                profit+=(minimum*h)
                minimum=b//2
                if(minimum>c and minimum!=0):
                    minimum=c
                profit+=(minimum*c)
            else:
                minimum=b//2
                if(minimum>f):
                    minimum=f
                b-=(minimum*2)
                profit+=(minimum*c)
                minimum=b//2
                if(minimum>p and minimum!=0):
                    minimum=p
                profit+=(minimum*h)
        print(profit)
        t-=1

main()
