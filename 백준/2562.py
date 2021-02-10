array = []
for i in range(9):
    array.append(int(input()))
print(max(array),array.index(max(array)) + 1)
