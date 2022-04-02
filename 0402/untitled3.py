#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 17:43:34 2022

@author: bgfretail
"""

#과제 
#튜플은 값을 수정할 수 없다.
#근데 수정하려면 ? 
#힌트는 리스트를 이용해라

tpl = (0,1,2,3)

#list = tpl
#list[5] = '4'

#for(i in tpl) : list

temp = list(tpl)

temp.append('4')

tpl1 = tuple(temp)
