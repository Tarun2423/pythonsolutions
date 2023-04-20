a=[5,4,3,2,1]
for i in range(1,len(a)):
    print(i)
    cur=a[i]
    j=i-1
    while j>=0 and a[j]>cur:
        a[j+1]=a[j]
        print(a)
        j-=1
    a[j+1]=cur
    print("SEcond",a)
