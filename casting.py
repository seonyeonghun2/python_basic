# 형변환
#  str, bool, int, float

a = '3.141592'
cast_a = float(a)
print(cast_a, type(cast_a))

# 일반적인 Null을, python은 None으로 표현

b = 5
if b is not None:
    print(b)
else:
    print('b is None data')

print(b is None)