#-*- coding: utf-8 -*-
'''
Created on 2021. 11. 8.

@author: dlgks
자바의 Map구조와 같이 Key와 Value가 하나의 쌍을 이루어 저장되는 구조다.
'''

d1 = {"k1":100, 2:200} #딕셔너리 생성
print("d1:",d1)

d1[3] = 300 # 3이라는 키에 값이 300인 원소 추가
print("d1:",d1)

d1[2] = 400
print(d1)

#요소삭제, 검출, 그리고 키 목록 또는 값 목록등을 작업해야 한다.

del d1[2]  #키가 2인 요소 삭제
print("del d1[2]:",d1)


v1 = d1.get(3) #키가 3인 요소의 값을 가져와서 변수 v1에 저장
print("v1:",v1)

keys = d1.keys() # d1 에 저장된 모든 키들만 얻어낸다.
                 # list가 아닌 dict keys객체다.ㅏ
print("d1.keys():{},{}".format(keys, type(keys)))


values = d1.values() # d1에 저장된 모든 값들만 얻어낸다.
                    #list가 아닌 dict values 객체다.
print("d1.values():{},{}".format(values, type(keys)))

key_list = list(keys) # dict_keys객체를 다시 list객체로 변환
print(key_list)
