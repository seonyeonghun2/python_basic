# 반복문
# while, for

# 리스트, 튜플같은 컬렉션이나 이터레이터를 순환함
a = 'hello python'
for char in a:
    print(char, end='')
print()
b = []
for char in a:
    b.append(char)
print(str(b))
print()

# 조건식과 반복문
c = [1, 2, None, 4, None, 5]
total = 0
for item in c:
    if item is None:
        continue
    else:
        total += item
print('None을 뺀 합 : ', total)


# 숫자 세기, 합 계산하기
total = 0
for i in range(1,11):
    if i % 2 == 0:
        total += i
print('1~10까지 짝수 합 : ',str(total))
print()
# 컴프리헨션
d = [i**2 for i in range(1,10)]
print(d)
e = [j for j in range(1,10) if j % 2 ==0]
print(e)