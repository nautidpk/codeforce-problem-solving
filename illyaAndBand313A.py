inp=int(input())
if(inp>=0):
    print(inp)
else:
    ina=abs(inp)
    ans1=(ina//10)
    ans2=(ina//100)*10+(ina%10)
    ans=ans1 if ans1<ans2 else ans2
    if(ans>0):
        print("-",ans,sep="")
    else:
        print("0")
