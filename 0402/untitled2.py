#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 16:50:28 2022

@author: bgfretail
"""

#과제 1 
#list1 = range(1,10)을 
#list2 = [6,7,8,9,10,1,2,3,4,5] 로 나오도록 한줄 코딩 

lst1 = [1,2,3,4,5,6,7,8,9,10]

lst2 = lst1[5:] + lst1[:5]


nums = list(range(10))
nums1 = nums
nums2 = nums[:] #복사 

nums[0] = "a"

import copy
nums = list(range(10))
nums3 = copy.deepcopy(nums)
nums[0] = "a"

#튜플 ()
tpl = (0,1,2,3,4,5)
tpl[1] ='999'


tpl.count(2)
tpl.index(3)


#집합{}, 중복 안됨 순서 의미 없음
name = {'www', 'www', 'ddd'}
name2 = set()
name1 = {} #얘는 딕셔너리 

'w2ww' in name

names = {'이정재', [1,2]}
name.add('알ㄹㅣ')
name.update([1,2,3])

#원소 제거
#remove() : 원소가 없으면 에러  
#discard()  : 원소가 없어도 노에러
name.remove('aaa')
name.discard('aaa')



#딕셔너리 
#무조건 한줄이넹
#키중복되면 마지막 값이 덮어진다 

inf = {"이름" : "정혜영","나이" : "31","키" : "162"}
inf.keys()
inf.values()
inf.items()

inf["지역"] = "서울"
inf
inf.get("성별")
inf.get("성별", "없엉?")
inf["성별"]

list = list(inf.key())

"나이" in inf



























