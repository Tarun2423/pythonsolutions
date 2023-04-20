a=[2,4,8,7,6,5,2,25,45,80,20,25,75,60,40,30,70,15,85,50,50]
n=100
a=sorted(a)
print(a)
def binary(arr,t):
    l=0
    r=len(arr)-1
    while(l<=r):
        mid=(l+r)//2
        if(arr[mid]==t):
            return mid
        elif arr[mid]>t:
            r=mid-1
        else:
            l=mid+1
    return "-1"
i=0
while(i<len(a)):
    t=n-a[i]
    s=binary(a[i+1:],t)
    if s!="-1":
        print(a[i],t)
        del a[i+1+s]
    i+=1
