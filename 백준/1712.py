A, B, C = map(int, input().split()) #A: 고정비용, B: 가변비용, C: 판매비용
if B >= C: #손익분기점 존재 X
    print(-1)
else:
    print(int(A/(C-B))+1) #손익분기점 구하는 식