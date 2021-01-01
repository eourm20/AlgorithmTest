A, B, V = map(int, input().split())
d = (V-B)/(A-B)
if d != int(d):
    d+=1
print(int(d))