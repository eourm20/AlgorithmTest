num = int(input())
count = 0
for i in range(num):
    S = input()
    for j in range(len(S)):
        if j != len(S)-1:
            if S[j] == S[j+1]:
                continue
            elif S[j] in S[j+1:]:
                break
        else:
            count+=1
print(count)