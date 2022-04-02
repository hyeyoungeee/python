#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 15:40:16 2022

@author: bgfretail
"""

#과제 1
#x= 5.0 y =3을 입력하고, 결과창으로
#"x+y = 8.0 입니다" 를 출력하는 함수 작성 

x = 5.0
y = 3.0

print("x+y = {} 입니다".format(x+y))


#과제 2
# x = "than3k"
# y = "yo97u"
# x와 y를 같이 선언한 후에 강의에서 사용한 함수로 "thank you" 출력

x = "than3k"
y = "yo97u"

x1 = x.replace("3","")
y1 = y.replace("97", "")
print("{} {}".format(x1,y1))
