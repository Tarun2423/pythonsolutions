a=[2,4,7,9,11]
k=4
m=a[-1]
b=[]
s=a[0]
for i in range(1,len(a)):
    if a[i]!=s+1:
        temp=s+1
        next=a[i]
        while(temp<next):
            b.append(temp)
            temp+=1
        s=temp
    else:
        s=a[i]
print(b)
