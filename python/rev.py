# 'A'=65 'a'=97
s="BabcN"
d=""
for i in s:
    if i.isupper():
        r=26-(ord(i)-ord('A'))
        d+=chr(ord('A')-1+r)
    if i.islower():
        r=26-(ord(i)-ord('a'))
        d+=chr(ord('a')-1+r)
print(d)