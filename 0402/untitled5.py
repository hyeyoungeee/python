#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 18:04:39 2022

@author: bgfretail
"""

#과제 
#리스트 [] a= list()
#튜플 () a =tuple()
#딕셔너리 {} a= dict()

name = ['이정재', '김태리', '남주혁','보미']

a = dict()
b = []

for i in range(1, len(name)+1):
    b.append("{}번".format(i))
    
for i in range(0, len(name)+1):
    a[b[i]] = name[i]
    
c= dict(zip(b,name))
