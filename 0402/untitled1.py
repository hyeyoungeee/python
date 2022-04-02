#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 16:36:19 2022

@author: bgfretail
"""

lst = [60,30,"20"]

score = [85, 90, 91, 92,93]
max(score)
min(score)
sum(score)

#range(시작, 끝, 스텝)
list(range(10))
list(range(5,10))
list(range(0,10,2))


#리스트인덱싱
score[0]
score[5]
score[-1]
score[-7]

score[1:2]
score[1:5]
score[:3]
score[2:]

score.append(100)

del score[5]

#삭제한다 
score[2:] = []

score.append([100,100])
score.extend([99,99])

