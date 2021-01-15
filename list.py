# 리스트
# 튜플은 생성후 데이터를 변경할 수 없으나, 리스트는 변경이 가능
# (,)  vs [, ]

list1 = [1, 2, True]
list2 = [2021, 'hello', 'python', 'world']

list1[0] = 'AB'
list2[0] = 21

print(list1)
print(list2)

# range(정수) : 0 ~ 정수[포함x] 생성
range1 = range(10)
print(range1, type(range1))
for i in range1:
    print(i, end=' ')

# list() 함수를 이용해 리스트로 변경
list3 = list(range1)
print(list3)

# 리스트 원소 추가하기 - .append(), .insert(), .extend()
list4 = [2, 4, 'A', True]

# 뒤에 추가
list4.append(False)

# 앞에 추가
list4.insert(0,'B')
print(list4)


# 리스트 원소 삭제하기 - .pop(), .remove(), del , .clear()
list5 = ['html', 'css', 'java', 'python']
# 마지막 원소 삭제
list5.pop()
print(list5)

# 일치하는 원소 삭제 - 앞쪽에서~
list5.remove('html')
print(list5)

# 인덱스로 삭제
del list5[0]
print(list5)
list5.append('html')

# 여러 원소를 추가
list5.extend(['css', 'python'])
print(list5)

# 한번에 모든 원소 삭제
list5.clear()
print(list5)

# 멤버쉽 테스트
print('html' in list5)
print('apache' not in list5)

# 리스트 연산 : +, *
print(list4 + ['hello', 'python'])
print(list4 * 3)

# 리스트 정렬 - .sort()
# 오름차순 정렬
a = [9, 7, 5, 3, 2, 10, 8, 1, 4, 6]
a.sort()
print(a)
# a[::-1] 과 같은 결과
a.reverse()
print(a)

# 문자열 길이로 정렬
b = ['hi', 'welcome', 'python', 'world']
b.sort(key=len)
print(b)

# 슬라이스
print(a[1:5])
a[0:2] = 109,'A'
print(a)
print(b[-1])

# enumerate() - 리스트의 원소에 인덱스 순서를 부여함 (튜플 반환)
item = ['first', 'second', 'third']
no = enumerate(item)
for i in no:
    print(i, type(i))

# enumerate() 활용
mapping = {}
for i, v in enumerate(b):
    mapping[i] = v
print(mapping)

athlete = ['kim', 'park', 'lee', 'son', 'cha']
cate = ['figure', 'baseball', 'running', 'football', 'swim']
new_ath = {}
for i in range(len(athlete)):
    new_ath[athlete[i]] = cate[i]
print(new_ath)

# sorted() - 정렬된
new_cate = sorted(cate)
print(new_cate)