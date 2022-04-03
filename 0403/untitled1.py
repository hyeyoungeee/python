#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 21:54:37 2022

@author: bgfretail
"""

#과제 

#계산기 만들기 
#class 명은 Cal, 덧셈함수 ADD, 뺄셈함수 Sub 두개만 만들어보기 

class cal:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        if type(a) == int and type(b) == int:
            return print("입력받은 숫자는 {},{}".format(a,b))
        else:
            print("숫자를 입력하세요")
        
    def add(self, a,b):
        return print("{}입니다".format(a + b))
    
    def sub(self, a,b):
        return a-b 
    

example = cal(1,"2")       
example.add(1,2)        
example.sub(3,1)
e