n=6
a=[6,3,2,10,2,1]
m=max(a)
print(m)
for i in range(m):
    ind=0
    for j in range(n):
        ce=a[ind]
        diff=m-ce
        if(diff>0):
            print("-",end="")
            a[ind]=a[ind]+1
        else:
            print("*",end="")
        ind+=1
    print()
    
