# 튜플
# 생성 후에 데이터는 변경할 수 없다.

tuple1 = 4, 5, 6
#빈 튜플
tuple2 = ()
tuple3 = tuple([4, 8, 12, ['A', 'B', 'C'], 16, 20])
tuple4 = tuple('this is tuple!')
print(tuple1, type(tuple1))
print(tuple2, type(tuple2))
print(tuple3, type(tuple3))
print(tuple4, type(tuple4))


#중첩된 튜플
nested_tuple = (4, 5, 6), (7, 8)
print(nested_tuple)

# 인덱싱
print(nested_tuple[0])
print(nested_tuple[0][0])

# 에러발생
# tuple3[0] = 11

# 튜플 내에 저장된 객체는 값의 변경이 가능
tuple3[3].append('D')
print(tuple3)

# 튜플의 연산 : +, *
print(tuple1 + tuple3)
print(tuple1 * 2)

# 튜플의 값 분리하기

a,b,c = tuple1
print(a, b, c)

# 문자열의 값 분리
i,j = 'hello python'.split(' ')
print(i, j)

seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a,b,c in seq:
    print(f'a={a}, b={b}, c={c}')

# 값 분리하기
values = (1, 2, 3, 5, 8)
a, b, *rest = values
# a, b, *_ 를 사용하기도 함.
print(a,b, rest)

# 튜플 메서드
tuple5 = (1, 2, 3, 4, 4, 2, 3, 1)
print(tuple5.count(4))