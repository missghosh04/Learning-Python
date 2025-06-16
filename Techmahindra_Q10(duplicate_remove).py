N=int(input("size"));
arr=list(map(int,input("arr").split(" ")))
ans=[]
d={}
for i in arr:
    if i not in d:
        d[i]=i
        ans.append(i)

print(ans)

