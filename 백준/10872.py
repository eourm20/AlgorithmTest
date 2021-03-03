N = int(input())
arr = range(1,N+1)
F_N = 1
for i in arr:
    F_N *= i 
print(F_N)