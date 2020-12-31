n = int(input())
c = 0
N = n
while True:
    if N < 10:
        N = N*10 + N
        c += 1
        print(N)
        if N == n:
            break
    else:
        n1 = N%10
        n2 = N//10 + n1
        if n2 >= 10:
            n2 = n2%10
            N = n1*10 + n2
            c+=1
            print(N)
            if N == n:
                break
        else:
            N = n1*10 + n2
            c+=1
            print(N)
            if N == n:
                break
print(c)