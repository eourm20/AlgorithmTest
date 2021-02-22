case = int(input())
new_S = ""
for i in range(case):
    R, S = input().split()
    for j in range(len(S)):
        new_S += S[j]*int(R)
    print(new_S)
    new_S = ""