def bintr(s,n):
    if(d.get(n)==None):
        d[n]=s
        return
    else:
        if(s>=d[n]):
            bintr(s,n*2+1)
        else:
            bintr(s,n*2)
d={}
l=list(map(int,input().split()))
for i in l:
    bintr(i,1)
for i in d:
    print(d[i],':',i)
