s=list(map(int,input().split()))
b=list(map(int,input().split()))
m=max(b)
prev=s[0]
for i in range(1,len(s)):
    if s[i]<prev and i+1<len(s) and s[i+1]>m:
        s[i]=m
        print(s)
        exit()
    else:
        prev=s[i]
print("Not possible")