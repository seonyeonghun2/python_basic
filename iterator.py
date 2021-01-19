# map(), filter() - iterator를 조작하는 함수
# iterator - 여러개의 데이터를 일렬로 관리하는 데이터 타입 (list, tuple, strings)

# 1. map() - iterator 요소들을 변경할 수 있다. 새로운 iterator를 반환
# map(함수, 이터레이터)

def make_double(num):
    return num * 2

list_a = [1, 2, 3, 4, 5]
# 반환은 리스트가 아님!, 필요하면 list() 함수를 사용해서 형 변환
result = map(make_double, list_a)
print(list(result))
# 한번 더 출력해보세요!
print(list(result))

# 2.filter() - iterator 요소들을 걸러낸다
def num_even(num):
    if num % 2 == 0:
        return True
tuple_a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
final = filter(num_even, tuple_a)
print(tuple(final))
print(tuple(final))

def power(item):
    return item * item
def under_3(item):
    return item < 3
list1 = [1, 2, 3, 4, 5]
out1 = map(power, list1)
print('map 함수 실행결과')
print(list(out1))
out2 = filter(under_3, list1)
print('filter 함수의 실행 결과')
print(tuple(out2))

def spam(eggs):
    eggs.append(1)
    eggs = [2, 3]
ham = [0]
spam(ham)
print(ham)

# def test(t):
#     t = 20
#     print('in function : ', t)
# # 전역변수
# x = 10
# print('before : ', x)
# test(x)
# print('after : ', x)

# 변수의 범위 scoping RUle
def test(t):
    print(x)
    #지역변수 t - 함수 내에서만 사용
    t = 20
    print('in function : ', t)
# 전역변수
x = 10
test(x)
# 아래 코드는 Error!
# print('t의 값 : ',t)
# 전역변수, 지역변수의 이름이 같다면? 새로운 메모리 주소가 할당
def f():
    s = 'I love london!'
    print(s, id(s))

s = 'I love Paris'
f()
print(s, id(s))

# c 언어 예제
# 값 바꾸기 1
def swap_offset(offset_x, offset_y):
    temp = a[offset_x]
    a[offset_x] = a[offset_y]
    a[offset_y] = temp

a = [x for x in range(1,6)]
print(a)
swap_offset(1,2)
print(a)

# 값 바꾸기 2
def swap_reference(list_ex, offset_x, offset_y):
    temp = list_ex[offset_x]
    list_ex[offset_x] = list_ex[offset_y]
    list_ex[offset_y] = temp

b = [y for y in range(1,6)]
print(b)
swap_reference(b, 1, 2)
print(b)



