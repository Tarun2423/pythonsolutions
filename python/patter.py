# n=int(input())
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1:
#             print("*",end="")
#         else:
#             if j==0 or j==n-1:
#                 print("*",end="")
#             else:
#                 print("",end=" ")
#     print()


i1=input().strip()
i2=input().strip()
aa=ord(i1)
bb=ord(i2)
for i in range(aa,bb+1):
    r=""
    p=hex(i).replace("0x", "")
    for i in p:
        if i.isalpha():
            r+=i.upper()
        else:
            r+=i
    print(r)