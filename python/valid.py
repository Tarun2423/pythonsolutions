a='())))'
b=[]
b[:0]=a
cc=0
s=[]
for i in b:
    if i=='(':
        s.append(i)
    elif i==')':
        if len(s)==0:
            cc+=1
        else:
            s.pop(-1)
print(cc+len(s))
