
#-*- coding: utf-8 -*-
'''
Created on 2021. 11. 8.

@author: dlgks

자바에서는 true또는 false를 기억하는 자료형을 boolean이라고 하지만
파이썬에서는 bool이라고 한다.
'''

b1 = True
b2 = False
print("b1={}".format(b1))
print("b2={}".format(b2))
#자바에서 처럼 소문자로 true또는 false로 사용하면 오류다.

#산술연산자(+,-,*,/,&)
a = 100
b = 32
print("a+b : %d"%(a+b))

c= a*b
print("a*b : %d"%c)

c= a/b
print("a/b : %f"%c)

c= a%b
print("a%%b : %f"%c)

#비교연산자(==, !=, >, <, <=, >=) = bool형태로 나온다.
print("a==b: %s"%a==b)
print(a>b)
print(a<=b)
print(a!=b)

#논리연산자(&=and, |:or, !:not)
print("a={}, b={}".format(a,b))

print((a>b) & (a >=30)) #둘 다 참이여야 함
print((a>b) | (a >=30)) #하나만 참이여도 참
'''
++,-- 와 같은 증감연산자는 지원하지 않는다. 굳이 하려면
a+=1과 같은 식을 사용해야 하는데 이것 또한 print()함수 내에서 사용하지 못한다.

아무래도 파이썬에서는 가독성을 중시하며, ++, --를 변수 앞에 명시하느냐 
뒤에 명시하느냐? 에따라 혼란스러운 상황이 발생하는 부작용이 비번하게 유발되므로 파이썬스럽지 못하다는
판단에 증감연사자를 생략한 듯 보인다.(개인적인 의견!)
'''














