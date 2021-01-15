# 2진수로 변환하기
# 1-1. 변환
# decimal = 10
# result = ''
# while decimal > 0:
#     remainder = decimal % 2
#     decimal = decimal // 2
#     result = str(remainder) + result
# print(result)
# print('-'*100)

# bin(), oct(), hex() 함수의 사용
# 10진수 -> 2진수, 8진수, 16진수 변환

su = 32
su_binary = bin(su)
print('32를 2진수 변환 :', su_binary, type(su_binary))
# 0b 기호는 2진수를 나타내는 문자열

su_octat = oct(su)
print('32를 8진수 변환 :', su_octat, type(su_octat))
# 0o 기호는 8진수를 나타내는 문자열

su_hexa = hex(su)
print('32를 16진수 변환 :', su_hexa, type(su_hexa))
# 0x 기호는 16진수를 나타내는 문자열

# 2진수, 8진수, 16진수 -> 10진수 변환
before_binary = 0b1101
before_octat = 0o50
before_hexa = 0x78

print('2진수 -> 10진수 변환 : ', before_binary)
print('8진수 -> 10진수 변환 : ', before_octat)
print('16진수 -> 10진수 변환 : ', before_hexa)
