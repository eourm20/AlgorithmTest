count = int(input())
array = []
sum = 0
ave = 0
num = 0
for i in range(count):
    class_array = list(map(int, input().split()))
    for j in range(class_array[0]):
        sum += class_array[j+1]
    ave = sum/class_array[0]
    for k in range(class_array[0]):
        if class_array[k+1] > ave:
            num += 1
    array.append(num/class_array[0]*100)
    sum = 0
    ave = 0
    num = 0
for i in range(count):
    print('%.3f'%array[i] +"%")
