# a=list(map(int,input().split()))
# d=int(input())
a=[4,15,6,3,13,4,7,14,8,15,5,8]
d=15
a=sorted(a)
print(a)
if max(a)>d:
    print('-1')
    exit()
i=0
s=0
res=0
n=len(a)-1
while(1):
    s+=a[i]
    print(i,s,res)
    if i==n:
        if s<=d:
            res+=1
        break
    while s<d:
        i+=1
        if i==n:
            break
        s+=a[i]
    if s==d:
        i+=1
    else:
        pass
    res+=1
    s=0
print("res",res)

