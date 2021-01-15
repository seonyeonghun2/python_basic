a = 'string'
b = 'this is strings'
c = '''
long long years ago,
python was born some day,
It has some data types, like str, int, bool and etc
'''

print('공백의 갯수 : ',c.count('\n'))

# ''' 뒤에 있는 개행(공백) 문자가 포함

a = 'change string'
print(a)

# 파이썬 문자열은 변경 불가
# 아래 코드는 오류가 납니다.
'''a[10] = 'a'
a[10] = 'y'
print(a)'''

d = 5.6
print(d, type(d))
# str() 함수를 이용해 문자열로 변환가능
d = str(d)
print(d, type(d))

# 역슬래시 이스케이프
e = '12\\34'
print(e)
# r - raw
f = r'this\has\no\special\character'
print(f)

# byte code
g = b'this is byte code'
print(g)
decoded_g = g.decode('utf-8')
print(decoded_g)
