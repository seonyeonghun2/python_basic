# 매개변수로 전달된 값을 모두 곱해서 리턴하기

def mul(*values):
    result = 1
    for value in values:
        result = result * value
    return result

final =mul(1,3,4,5,6,9,0)
print(final)

def f(x):
    return x

print(f(10))

def ff(x):
    return (x**2)+(2*x)+1

print(ff(10))
print('-*-'*30)
# 재귀함수(recursive) - 원래 자리로 되돌아가거나 되돌아 옴


# def recursive(x):
#     result = 1
#     for i in range(1, x+1):
#         result *= i
#     return result
# print('1 : ',recursive(1))
# print('2 : ',recursive(2))
# print('3 : ',recursive(3))
# print('4 : ',recursive(4))
# print('5 : ',recursive(5))

# 1. for반복문
def for_factorial(x):
    result = 1
    for i in range(1,x+1):
        result *= i
    return result
print('5! : ',for_factorial(5))

# 2. 재귀함수
def recursive_func(x):
    if x > 1:
        return x * recursive_func(x-1)
    else:
        return 1
print('5! : ', recursive_func(5))

# 3. math module
import math

# help(math)
print('5! : ',math.factorial(5))

# recursive
num = 1
def recur():
    global num
    num += 1
    print(num)
    if num == 10:
        return
    recur()
recur()

print('-*-'*30)

def sum(a, b, c):
    return a+b+c
numbers = [1,2,3]
#sum(numbers) # error
print(sum(*numbers))