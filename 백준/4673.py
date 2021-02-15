def d(n):
    a = 0
    for i in list(str(n)):
        a = a + int(i) 
    return int(n) + a
a= []
for i in range(1,10001):
    k = d(i)
    a.append(k)

for j in range(1, 10001):
    if j in a:
        pass
    else:
        print(j)