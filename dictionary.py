# 딕셔너리
# key:value - 쌍으로 이루어져 있음

# 빈 딕셔너리
dict1 = {}
dict2 = {
    'a': 'value1',
    'b': 'vaue2',
    'c': ['c1', 'c2', 'c3']
}
# 인덱싱
print(dict2['a'])
print(dict2['c'][0])
dict2['d']='value3'
print(dict2)

# 멤버쉽 테스트 (key)
print('a' in dict2)
print('c1' in dict2)

# 키(key) 제거하면 값(value)도 제거됨
del dict2['d']
print(dict2)

dict2.pop('c')
print(dict2)

dict3 = {
    'id': '물아까와쓰지마',
    'lev': 99,
    'hp': 1000,
    'mp': 100,
    'skill':['뛰기', '걷기', '잠자기']
}
# dict3_items = dict3.items()
# for key, value in dict3_items:
#     print(key,':', value)

dict3_items = dict3.items()
for key, value in dict3_items:
    if type(value) is list:
        for i in range(len(value)):
            print(key, ':', value[i])
    else:
        print(key, ':', value)
print('='*100)

words = ['apple', 'banana', 'tomato', 'melon', 'orange']
by_letter = {}
# for word in words:
#     letter = word[0]
#     if letter not in by_letter:
#         by_letter[letter] = word
#     else:
#         by_letter[letter].append(word)
# print(by_letter)

# 또는?

# for word in words:
#     letter = word[0]
#     by_letter.setdefault(letter,[]).append(word)
#
# print(by_letter)

# 또는?
for word in words:
    key = word[0]
    if key not in by_letter.keys():
        by_letter[key] = word
    else:
        by_letter[key].append(word)
print(by_letter)

# 딕셔너리의 key로 사용하려면 변경되지 않아야 하고, hash() 함수로 확인가능