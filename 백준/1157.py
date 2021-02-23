S = input().lower()
word = list(set(S)) #사용된 단어의 배열
# set(문자열) = 문자열에 사용된 알파벳 추출
cnt = [] #사용 알파벳 개수 저장
for i in word:
    cnt.append(S.count(i))

if cnt.count(max(cnt)) != 1:
    print("?")
else:
    print(word[(cnt.index(max(cnt)))].upper())