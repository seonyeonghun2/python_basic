# 세트
# 중복되지 않는 값을 담을때, 순서가 없다(=인덱싱x)

set1 = set([1,2,3,3,2,4,5,7,8,6,9,10])
print(set1, type(set1))
set2 = set('hello')
print(set2)
# 세트 --> 리스트 또는 튜플
set_to_list = list(set2)
set_to_tuple = tuple(set2)
print(set_to_list, type(set_to_list))
print(set_to_tuple, type(set_to_tuple))

# 교집합, 합집합, 차집합

set3 = set([1, 2, 3, 4, 6, 8])
set4 = set([2, 3, 4, 5, 6, 8])
print('교집합', set3&set4)
print('합집합', set3|set4)
# intersection() 함수
print(set3.intersection(set4))

# .add(v), .clear(), .pop(), .remove(x)
# a.union(b), a.update(b), a.intersection(b), a.difference(b)