n = []
with open('a.txt','r') as f1:
    a = f1.read()
    for x in a:
        n.append(x)

with open('b.txt','r') as f2:
    b = f2.read()
    for y in b:
        n.append(y)

n.sort()

with open('c.txt','w') as f3:
    for z in n:
        f3.write(z)
print(a)
print(n)
print(type(a))