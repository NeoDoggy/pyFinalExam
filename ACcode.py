#bintree
def mtree(n,np):
    if(arr[np]==-1):
        ans[n]=np
        arr[np]=n
        return
    else:
        if(n<=arr[np]):
            ans[n]=np
            mtree(n,np*2)
        else:
            ans[n]=np
            mtree(n,np*2+1)
#var
s=list(map(int,input().split()))
arr=[-1 for i in range(0,pow(2,len(s))+1)]
ans={}
#main
for i in s:
    mtree(i,1)
#output
for i in ans:
    print(str(i)+":"+str(ans[i]))