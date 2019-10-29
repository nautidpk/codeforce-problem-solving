s,n=map(int,input().split(" "))
ans="YES";i=0;dr=[];st=[]
while(i<n):
    a,b=map(int,input().split(" "))
    if s>a:
        s+=b
    else:
        dr.append(a);
        st.append(b)
    i+=1
if len(dr)==0:
    print(ans)
else:
    flag=True
    while(flag):
        m=dr.index(min(dr))
        if s>dr[m]:
            s+=st[m]
            del st[m]
            del dr[m]
        else:
            flag=False
        if len(dr)==0:
            break
    print(ans if flag==True else "NO")
