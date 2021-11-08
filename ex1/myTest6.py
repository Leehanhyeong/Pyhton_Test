#-*- coding: utf-8 -*-
'''
Created on 2021. 11. 8.

@author: dlgks
'''

ar = [10,20,30,3.3, '프로그래밍']

var1 = ar[3] #인덱스 값으로 요소 추출
print("ar[3]={}".format(var1))
size = len(ar)
print("len[ar]={}".format(size))

# ar이라는 리스트에서 가장 마지막에 있는 요소를 추출하여 출력하시오
var2 = ar[len(ar)-1]
print("ar[len(ar)-1]={}".format(var2))
print(ar[-1])

print('-------------요소 추가-------------')

ar.append(120)  #맨 뒤에 추가
print("ar={}".format(ar))

#원하는 위치에(index)에 추가하는 법은 insert
ar.insert(4, 3000)
print(ar)

ar2 = [4500, 6500]

ar+=ar2 #확장 합치다.
print("ar+=ar2={}".format(ar))

ar3 = [10000,20000,30000]
ar.extend(ar3) #확장 합치다.
print(ar)


print('--------------------요소 추가 -----------------')

ar.remove('프로그래밍')
print(ar)

del ar[1] #ar의 2번째 요소 삭제
print(ar)

#먼저 ar에서 120이라는 값의 index값을 구한 후 그값을
#del명령으로 삭제하자
del ar[ar.index(120)]



