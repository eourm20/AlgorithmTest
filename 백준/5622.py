dial = ['ABC', "DEF","GHI",'JKL','MNO','PQRS',"TUV","WXYZ"]
S = input()
min = 0
for i in range(len(S)):
    for j in dial:
        if S[i] in j:
            min += dial.index(j)+3
print(min)