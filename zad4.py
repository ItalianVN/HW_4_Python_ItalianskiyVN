
# from random import randint
# k = int(input('k = '))
# res = [(randint(0, 3), k - i) for i in range(k + 1)]
# print(res)
# res = [(str(c) if c > 1 or not i else '', 'x' if i else '', f'^{i}' if i > 1 else '') for c, i in res if c]
# print(res)
# res = [''.join(x) for x in res if not all(not len(x) for x in res)]
# print(res)
# res = ' + '.join(res) + ' = 0'
# print(res)
# with open('file.txt', 'w') as f: f.write(res)

from random import randint
k = int(input('k = '))
res = [(randint(0, 3), k - i) for i in range(k + 1)]
print(res)
res = [(str(c) if c > 1 else '', 'x' if i else '', f'^{i}' if i > 1 else '') for c, i in res if c]
print(res)
res = [''.join(x) for x in res if not all(not len(x) for x in res)]
print(res)
res = ' + '.join(res) + ' = 0'
print(res)
with open('file.txt', 'w') as f: f.write(res)