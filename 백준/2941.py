cro = ["c=", 'c-', 'dz=', 'd-','lj','nj','s=','z=']
S = input()
for i in cro:
    S = S.replace(i, "!")
print(len(S))
