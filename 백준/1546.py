count = int(input())
origin = list(map(int,input().split()))
new = []
max_score = max(origin)
for i in range(count):
    new.append(origin[i]/max_score*100)
    ave = sum(new)/count
print("%.2f" %ave)