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