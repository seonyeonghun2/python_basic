f = open('./some_file.txt', 'w')
for i in range(1, 11):
    data = '%d번째 줄입니다 \n' % i
    f.write(data)
f.close()


f2 = open('./some_file.txt', 'r')
while True:
    fl = f2.readline()
    if not fl: break
    print(fl)
f2.close()

