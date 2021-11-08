#-*- coding: utf-8 -*-

'''
Created on 2021. 11. 8.

@author: dlgks

파이썬의 자료구조
 List : [값1, 값2, ...., 값n] 배열과 같고 순서를 가짐
 Tuple:(값1, 값2, ...., 값n] List와 같지만 읽기전용
 Set: {값1, 값2, ...., 값n] List와 유사하지만 교집합 구분
 dict : dist(키1=값1, 키2=값2, .... , 키n=값n) 키와 값이 쌍을 이루어 저장됨
             {키1:값1, 키2:값2, .... , 키n:값n} (자바의 Map구조)
'''

ar1 = [1,2,3,4]
ar2 = [10,3,14, "TEST"]
print("ar1={}".format(ar1))
print("ar2={}".format(ar2))

#배열 합치기 [1,2,3,4,10,3,14,"TEST"]
ar3 = ar1+ar2
print(ar3)

#배열안에 배열이 포함되는 경우
ar4 = [10,20,[300,400]]
print("ar4={}".format(ar4))

str="들음에 있어 믿음이 생기고, 그 믿음에서 행동이 뒤따른다."
ar5=str.split(" ")
print("ar5={}".format(ar5))









