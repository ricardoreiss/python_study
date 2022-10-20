a = '4000'
b = '2000'

na = len(a)
nb = len(b)

ma = na/2
ae = int(a[:int(ma)])
ad = int(a[int(ma):])

mb = nb/2
be = int(b[:int(mb)])
bd = int(b[int(mb):])

c = ae*be
u = ad*bd
e = (ae+ad)*(be+bd)
d = e - u - c

ans = ((10**na) * c) + ((10**int(na/2)) * d) + u

print(ans)
print(int(a)*int(b))