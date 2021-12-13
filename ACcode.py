s=input().split('=')
n=int(s[1])
a=[0]
ans=[]
for i in range(1,n+1):
    if(i>1):
        a.append(a[i-1]+int(input()))
    else:
        a.append(int(input()))
s=input().split('=')
n=int(s[1])
s=input().split('=')
bg=int(s[1])
for i in range(0,n):
    s=input().split()
    aa,bb=int(s[0]),int(s[1])
    if(aa>bb):aa,bb=bb,aa
    tmp=a[bb]-a[aa-1]
    if(tmp<=bg):ans.append(i+1)
print(ans)