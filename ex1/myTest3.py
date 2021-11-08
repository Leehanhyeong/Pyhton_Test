#-*- coding: utf-8 -*-
'''
Created on 2021. 11. 8.

@author: dlgks
자바처럼 문자와 문자열로 구분되지 않고, 그냥 문자열로 인식한다.
'''

str = "go for it!"

print(str)

print("str:{}".format(str))

test = str*3 #str이 기억하는 문자열을 3번 반복해서 변수 test에 저장
print("str*3: %s"%test) 

test2 = test.replace("for","get") #for을 get으로 바꿔라
print("test2 : %s"%test2)

v1= str[3] #str이 기억하는 문자열의 왼쪽에서 4번째 문자값을 추출하여 변수 v1에 저장한 것
print("str[3] : %s"%v1)

v2= str[3:6] #자바의 str.substring(3,6)와 같다.
print("str[3:6] : %s"%v2)

v3= str.find("f") # 자바의 str.indexof(f)와같다. 
print("str.find(f):{}".format(v3))
#find함수는 찾는 값이 없으면 -1을 반환한다.

v4= str.index("fo") # 자바의 str.indexof(f)와 같다.
print("str.index(fo):{}".format(v4))
#index함수는 찾는 값이 없으면 오류난다.
