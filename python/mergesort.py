def mergesort(a):
    if len(a)<2:
        return
    mid=len(a)//2
    lh=a[:mid]
    rh=a[mid:]
    mergesort(lh)
    mergesort(rh)
    merge(lh,rh,a)
def merge(lh,rh,a):
    i=j=k=0
    while(i<len(lh) and j<len(rh)):
        if lh[i]<=rh[j]:
            a[k]=lh[i]
            i+=1
            k+=1
        else:
            a[k]=rh[j]
            j+=1
            k+=1
    while i<len(lh):
        a[k]=lh[i]
        i+=1
        k+=1
    while j<len(rh):
        a[k]=rh[j]
        j+=1
        k+=1
a=[40,1,99,3,7,20,160,24,88,4,8]
mergesort(a)
print(a)    