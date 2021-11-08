#-*- coding: utf-8 -*-
'''
Created on 2021. 11. 8.

@author: dlgks
집합을 의미하는 것이 바로 Set이다. 즉, 합집합, 교집합, 차집항븨
연산을 수행한다. 그리고
자바와 같이 중복을 허용하지 않는다.

'''

icecream1 = {'체리주빌레','엄마는외계인','치즈고구마','엄마는외계인'}
print('icecream1의 길이:{},{}'.format(len(icecream1),icecream1))

res = "슈팅스타" in icecream1 #icecream1안에 "슈팅스타"가 있냐 물어보는 것.
print("슈팅스타 in icecream1:",res) #당연히 없으니 false가 나온다.


res = "슈팅스타" not in icecream1 
print("슈팅스타 not in icecream1:",res) 