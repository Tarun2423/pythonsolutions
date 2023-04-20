a=list(map(int,input().split()))
for i in range(len(a)):
    pes=0
    pos=0
    for j in range(len(a)):
        if i!=j and j<i:
            pes+=a[j]
        if i!=j and j>i:
            pos+=a[j]
    if pes==pos and pes!=0:
        print(True)
        exit()
print(False)



