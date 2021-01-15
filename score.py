# A~ E 학생의 2차원 성적 리스트
kor_score = [60, 80, 90, 60, 70]
eng_score = [90, 100, 80, 90, 80]
math_score = [60, 70, 90, 80, 80]
midterm_score = [kor_score, math_score, eng_score]
#print(midterm_score[0][0])
stu_score = [0, 0, 0, 0, 0]

dic = {
    'name': 'pey',
    'phone': '0119993323',
    'birth': '1118'
}
a = {
    1: 'hi',
    2: 'welcome'
}
b = {
    'a': [1,2,3]
}
# a[2] = 'b'
# print(a)
# a['name']='pey'
# print(a)
# a[3]=['a', 'b', 'c']
# print(a)
# del a[2]
# print(a)

# grade = {
#     'pey': 10,
#     'juliet': 90
# }
# print(grade['pey'])
# print(grade['juliet'])

# c = {
#     [1,2]: 'hi'
# }
# a_key = a.keys()
# print(a_key, type(a_key))

# 1.
# list_of_list = [
#     [1,2,3],
#     [4,5,6,7],
#     [8,9]
# ]
# for i in list_of_list:
#     for j in i:
#         print(j)

# 2.
numbers = [1, 2,3, 4, 5, 6, 7, 8, 9]
output = [
    [],
    [],
    []
]
for number in numbers:
    output[(number + 2)%3].append(number)

print(output)

# 3.

dict = {
    'name': '7d 망고',
    'type': 'fruit',
    'taste': ['sweet', 'delicious', 'thik'],
    'origin': 'philipin',
    'tip': {

    }
}
for line in dict:
    if type(dict[line]) is list:
        for item in dict[line]:
            print(line,':',item)
    else:
        print(line, ':', dict[line])