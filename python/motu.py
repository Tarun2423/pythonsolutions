arr=[12,4,3,3]
b=1
a=2*b
n=len(arr)
s=0
e=n-1
i=0
m=p=1
while(s<=e):
    while(arr[s]>0 and arr[e]>0):
        arr[e]-=b
        arr[s]-=a
    if arr[s]<=0:
        if s+1==e:
            break
        s+=1
        m+=1
    if arr[e]<=0:
        if e-1==s:
            break
        e-=1
        p+=1
print(m,p)
