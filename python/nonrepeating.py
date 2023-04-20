s="apple"
arr=[]
i=0
c=0
m=0
while(i<len(s)):
    if s[i] not in arr:
        c+=1
        arr.append(s[i])
        i+=1
    else:
        m=max(m,c)
        c=0
        arr=[]
m=max(m,c)
print(m)
