# 함수의 선언
def funcName():
    # code here
    print('hello')

# 함수 실행
funcName()

def print_n_times(value, n):
    for i in range(n):
        print(value)

print_n_times('안녕하세요', 5)
print('-'*10)
# print_n_times('안녕하세요',4,5)

# 가변 매개변수 - 매개변수 여러개
def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times(3, 'hello', 'python', 'world')

def print_n_times(value, n=2):
    for i in range(n):
        print(value)

print_n_times('안녕하세요')
print('-'*10)
# 에러발생!
# def print_n_times(n=2, *values):
#     for i in range(n):
#         for value in values:
#             print(value)
#         print()
#
# print_n_times('안녕하세요','반갑습니다','파이썬')

def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()
print('-'*10)
print_n_times('안녕하세요', '반갑습니다', '파이썬', n=5)

def f():
    a = 5
    b = 6
    c = 7
    return {'a':a, 'b':b, 'c':c}
    # return a,b,c


# a,b,c = f()
return_value = f()
print(return_value, type(return_value))

# function is object in python3

def add_many(*args):
    result = 0
    for i in args:
        result =result +i
    return result

result2 = add_many(1,2,3,4,5)
print(result2)

def calc(choice, *args):
    if choice == 'add':
        result = 0
        for i in args:
            result = result + i
    elif choice == 'mul':
        result = 1
        for i in args:
            result = result * i
    return result

print(calc('add', 10,20,30))
print(calc('mul', 5, 4, 2, 0))

def print_kwargs(**kwargs):
    print(kwargs)

run = print_kwargs(a=1,b=3)

print_kwargs(name='foo', age=3, gender='male')

print('-'*100)

a = 1
# def vartest(a):
#     a = a +1
#     return a
def vartest(x):
    global a
    x = a +1
    return x


a = vartest(a)
print(a)
print('='*100)
# def vartest(b):
#     b = b + 1
# vartest(3)
# print(b)


# lambda - 함수를 한 줄로 간결하게 만들때....람다
print('-'*100)
ads = lambda a, b: a+b
res = ads(3, 4)
print(res)

def apply_to_list(some_list, f):
    return [f(x) for x in some_list]
list1 = [1, 3, 5, 7, 9]
output1 = apply_to_list(list1, lambda x: x*2)
print(output1)
import math
print(help(math))

def test():
    return 10,20
a1, b1 = test()
print(a1, b1)

a2, b2 = 97, 40
x2 = divmod(a2, b2)
print(x2[1])

def call_10_times(func):
    for i in range(10):
        func()
def print_hello():
    print('안녕하세요')

call_10_times(print_hello)

# def power(item):
#     return item * item
# def under_3(item):
#     return item < 3
# list1 = [1, 2, 3, 4, 5]
# out1 = map(power, list1)
# print('map 함수 실행결과')
# print(out1)
# out1_list = list(out1)
# print(out1_list)
# out2 = filter(under_3, list1)
# print('filter 함수의 실행 결과')
# print(out2)
# out2_list = list(out2)
# print(out2_list)

# power = lambda x: x * x
# under_3 = lambda x: x< 3
#
# list_input = [1, 2, 3, 4, 5]
#
# output_a = map(power, list_input)
# print('map 함수의 실행 결과')
# print('map(power, list_input) : ', output_a)
# print('map(power, list_input) : ', list(output_a))
# print()
#
# output_b = filter(under_3, list_input)
# print('filter함수의 실행 결과')
# print('filter(power, list_input) : ', output_b)
# print('filter(power, list_input) : ', list(output_b))
# print()

# def print_n_times(n, *args):
#     for i in range(n):
#         for arg in args:
#             print(arg)
#         print()
# print_n_times(5,'만나서', '반갑습니다', '메뚜기')

def print_x_times(value, x):
    for i in range(x):
        print(value)

print('='*100)
print_x_times('안녕하세요', 5)

# 가변 매개변수 - print(x,y,z,..)
strs= {'1':'김연아', '2':'박찬호', '3':'이동국'}
def print_x_times2(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_x_times2(3, strs)

def print_x_times3(value, n=2):
    for i in range(n):
        print(value)
print_x_times3('안녕하슈')

def print_y_times(*args, n=2):
    for i in range(n):
        for value in args:
            print(value)
        print()
print_y_times('안녕하세요', '만나서', '반갑습니다', 3)

def print_some(a, b ,c):
    return a,b,c

def test(a, b=10, c=50):
    print(a+b+c)

test(10,20,30)
test(a=10,b=100,c=300)
test(c=10,a=100,b=200)
test(10,c=200)

value = input('> value?')
print(value)

