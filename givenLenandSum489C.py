def maxLimitNo(m,s):
    if(m*9<s):
        return "-1"
    if(m>1 and s==0):
        return "-1"
    i=0;ans="";flag=True
    while(i<m):
        if(not flag):
            i+=1
            ans+="0"
            continue
        num=s-9
        if(num>=0):
            ans+="9"
            s-=9
        elif(num<0):
            ans+=str(s)
            flag=False
        i+=1
    return ans
        
def minNumber(m,s):
    if(m*9<s or (m>1 and s<1)):
        return "-1"
    if(m==1 and s==0):
        return "0"
    i=0;ans="1";flag=True
    n=s-(m-1)*9
    if(n>0):
        s-=n
        m-=1
        ans=str(n)
    else:
        s-=1
        m-=1
    ans2=maxLimitNo(m,s)
    if(ans2=="-1"):
        if(m<=0):
            return ans;
        ans2=""
        while(i<m):
            ans2+="0"
            i+=1
    return ans+ans2[::-1]
    
m,s=map(int,input().split(" "))
print(minNumber(m,s),maxLimitNo(m,s),sep=" ")

