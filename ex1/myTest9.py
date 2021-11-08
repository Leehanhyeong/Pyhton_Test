#-*- coding: utf-8 -*-
'''
Created on 2021. 11. 8.

@author: dlgks
'''

t1 = set('1234567')
t2 = set('4567890')

print(t1)
print(t2)

res1 = t1&t2 # 두 Set구조의 모두가 가지고 있는 교집합
print('t1&t2 : {}'.format(res1))

res1 = t1|t2 # 두 Set구조의 요소들을 합친 합집합
print('t1|t2 : {}'.format(res1))

res1 = t1-t2 # 두 Set구조의 요소들을 뺀t1-t2 차집합
print('t1-t2 : {}'.format(res1))

t1.add(22);
print(t1)

t1.remove('4')
print(t1)

t2.add(500)
print(t2)

t2.remove(500)
print(t2)

f1 = frozenset({10,20})
print('f1:',f1)

#f1.add(30)
f2 = frozenset({40,50})

f3 = frozenset({f1,f2})
print('f3:', f3)



