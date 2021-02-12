count = int(input())
score = 0
result = 0
array = []
for i in range(count):
    check = input()
    for j in range(len(check)):
        if check[j] == 'O':
            score += 1
            result += score
        if check[j] == 'X':
            score = 0
    array.append(result)
    score = 0
    result = 0
for i in range(count):
    print(array[i])
