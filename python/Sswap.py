s="aaabc"
g="aaacb"
r=[]
r[:0]=s
d=r[:]
for i in range(len(s)-1):
    for j in range(i+1,len(s)):
        d[i],d[j]=s[j],s[i]
        st="".join(d)
        if st==g:
            print(1)
            exit()
        else:
            d=r[:]
print(2)    