#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 17:51:15 2022

@author: bgfretail
"""

#if문 쓸 때 무조건 들여쓰기 
score = 30


if score < 30 : 
    print("fail")
elif score >= 30 :
    print("success")
else :
    print("error")
    
    
score = 90
if score > 30 : 
    print("good")
elif score > 80 :
    print("great")


#for문 

for i in range(5) :
    print(i)
    
for i in [0,1,2,3,4] :
    print(i)
    
for i in ["배", "고","파"]:
    print(i)
    

#while문
i=0
while i < 10:
    print(i)
    i+= 1
    
break

lst = list(range(9))
lst_odd = [x for x in lst if x % 2 == 1]
lst_even = [x for x in lst if x % 2 == 0]
