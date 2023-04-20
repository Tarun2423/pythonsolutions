h,t=map(int,input().split())
h-=1
t-=1
d=int(input())
def printmat(a):
    for i in range(15):
        print(*a[i])
a=[[0 for _ in range(15)]for _ in range(15)]
if d==0:
    t=h
    for i in range(3):
        a[h][t]=1
        t+=1
    head=[h,h]
    tail=[h,t]
elif d==1:
    t=h
    for i in range(3):
        a[h][t]=1
        t-=1
    head=[h,h]
    tail=[h,t]
elif d==2:
    t=h
    for i in range(3):
        a[t][h]=1
        t+=1
    head=[h,h]
    tail=[t,h]
elif d==3:
    t=h
    for i in range(3):
        a[t][h]=1
        t-=1
    head=[h,h]
    tail=[t,h]
printmat(a)
print(head)
print(tail)
while(1):
        print("enter no of steps")
        st=int(input())
        hx,hy=head[0],head[1]
        tx,ty=tail[0],tail[1]
        for i in range(st):
            if(hy<ty): 
                hy-=1
                a[hx][hy]=1
                a[tx][ty]=0
                ty-=1
            else:
                hy+=1
                a[hx][hy]=1
                a[tx][ty]=0
                ty+=1               
        printmat(a)
        
