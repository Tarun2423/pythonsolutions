a=[]
s=input().strip()
m=s
while(True):
    c=0
    d=""
    for i in range(len(m)):
        if m[i] in m[i+1:]:
            c+=1
            d+=m[i+1:]
            break
        else:
            d+=m[i]
    if c==0:
        print(m)
        break
    else:
        m=(d[::-1])
