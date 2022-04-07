#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 23:21:32 2022

@author: bgfretail
"""

#pandas 매우 중요 
import pandas as pd
example = pd.Series()

lst = [1,2,3,4,5]
ex_1 = pd.Series(lst)
print(ex_1, type(ex_1))


ex_1.loc[0]
ex_1.iloc[0]

dict = {"성별":"여자", "이름":"정혜영", "나이":"31", "지역":"서울"}
ex_2 = pd.Series(dict)

ex_2.loc[1]
ex_2.iloc[1]
ex_2.loc['이름']

## iloc는 고유의 자리, loc는 눈에 보이는 자리 

ex_2.reset_index(drop = True)
ex_2.reset_index(drop = False) #default
ex_2.reset_index()

ex_3 = ex_2.reset_index()

#시리즈 여러 줄이 데이터 프레임워크 

print(ex_3)
ex_3.loc[3,0]
ex_3.loc[3,'index']
ex_3.iloc[3,0]
ex_3.iloc[3,1]

ex_3.shaoe
type(ex_3)
