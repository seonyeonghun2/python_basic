tup = 4, 5, 6
print(tup, type(tup))

nested_tup = (4,5,6), (7,8)
print(nested_tup, type(nested_tup))
list_to_tuple = tuple([1,3,5,7,9])
print(list_to_tuple)
str_to_tup = tuple('string to tuple')
print(str_to_tup)
other_tup = tuple(['foo', [1, 2], True])
print(other_tup)
# other_tup[2] = False

print(tup+nested_tup)
other_tup[1].append(2)

a,b,c=tup
print(a,b,c)
(e,f,g),(h,i) = nested_tup
print(e,f,g,h,i)
# tmp = a
# a = b
# b = tmp
# print(a,b)
a,b = b,a

seq = [(1,2,3), (4,5,6), (7,8,9)]
for a,b,c in seq:
    print(f'a={a}, b={b},c={c}')

values = 1,2,3,4,5
print(values, type(values))
a,b,*rest = values
# 불필요한 값을 무시
# a,b,_rest = values
print(a, b, rest, type(rest))
# packing
def func(*args):
    print(args)
    print(type(args))
func(1,2,3,'a','가')
# unpacking
def sum(a, b, c):
    return a+b+c
numbers = [1,2,3]
#sum(numbers) # error
print(sum(*numbers))
print(sum(*'abc'))
print(sum(*(4,5,6)))
print(sum(*{'가','나','다'}))
print(sum(*{'치킨':3, '피자':12, '음료':10}))

