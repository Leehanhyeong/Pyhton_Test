#-*- coding: utf-8 -*-
'''
Created on 2021. 11. 8.

@author: dlgks
리스트와 비슷하지만 다른점은 리스트는 요소의 추가,삭제가 자유로운 
가변적 길이를 가졌지만 튜플은 immutable(불변) 즉, 읽기 전용으로 사용된다.
'''

list1 = [10,50,100,150]
tuple1 = (100,'tuple',200)

list1[1] = 500 # 두번째 요소의 값 50을 500으로 변경
list1.append(200)  #요소추가 append
print("list1={}".format(list1))

# tuple1[1] = "프로그래밍" #읽기전용(불변)이라 적용불가.
print("tuble1={}".format(tuple1))

print("tuble1.count={}".format(tuple1.count(200)))
print("tuple1.index('tuple')={}".format(tuple1.index('tuple')))

list2 = list1[:] # 즉 리스트 복사
print("list1={}".format(list1))
print("list2={}".format(list2))

chk = list2 is list1 #주소비교
print("list2 is list1= {}".format(chk))

tuple2 = tuple1[:] #튜플 복사
print("tuble1={}".format(tuple1))
print("tuble2={}".format(tuple2))


chk= tuple2 is tuple1 #주소비교
print(chk)








