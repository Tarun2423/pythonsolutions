a="ramajayam"
b="subashree"
c="flames"
a=list(a)
b=list(b)
c=list(c)
al=len(a)
bl=len(b)
cnt=0
for i in a:
    for j in range(len(b)):
        if i==b[j]:
            b[j]='#'
            cnt+=1
            break
f=(al-cnt)+(bl-cnt)
print(f)
ct=0
i=f-1
if(i>=6):
    i=i%6
while(ct<5):
    d=f
    if(c[i]!='#'):
        c[i]='#'
        ct+=1
    while(d>0):
        i+=1
        if(i>=6):
            i=0
        if(c[i]!='#'):
            d-=1
    c[i]='#'
    ct+=1
for i in c:
    if i!='#':
        print(i)
        break
        
        