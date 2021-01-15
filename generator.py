# 제너레이터 - 순회가능한 객체

gen = ( x ** 2 for x in range(1,11))
print(gen, type(gen))

# for item in gen:
#     print(item, type(item))

def make_gen():
    for x in range(10):
        return x ** x
gen = make_gen()
print(gen)


a = ['a1', 'b1', 'c1']
for k,v in enumerate(a):
    print(k,':',v)
for k,v in enumerate(a):
    print(k,':',v)
for k,v in enumerate(a):
    print(k,':',v)

b = (x for x in range(10))
print(b)
for i in b:
    print(i, end = ' ')

# 제너레이터는 값을 한번만 기억,
for i in b:
    print(i, end = ' ')


