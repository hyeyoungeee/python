#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 22:09:57 2022

@author: bgfretail
"""

f = open('test', 'r', encoding='utf8')
line = f.readlines()
f.close()

f = open('정보', 'r', encoding='utf8')
line = f.readlines()
f.close()
print(str(line).rstrip())


result = []
for i in line:
    temp = i.replace("\n", "")
    result.append(temp)
    
print(result)
    
    
result2 = []
for i in range(len(line)):
    temp = result[i].split(":")
    result2.append(temp)

print(result2)

result3 = []
for i in range(len(line)):
    
    
    
flat_list = [item for sub in result2 for item in sub]
