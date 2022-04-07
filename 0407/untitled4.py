#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 22:33:12 2022

@author: bgfretail
"""

f = open('coin.txt', 'r', encoding='utf-8')
line = f.readlines()
f.close()

result = line[0].split(",")


#각각의 str을 float으로 
result = list(map(float,result))
result = [float(x) for x in result]
##빈칸은 숫자로 바꿀수없어서 에러남 

#try & except
for i in range(len(result)):
    try:
        result[i] = float(result[i])
        print(i, result[i],type(result[i]))
    except:
        print("리스트 {}번째에서 에러 발생, 다음으로 넘어갑니다.".format(i))
        
print(result)

#pass, continue, raise error
result = [8,9,19,"",11,12,"",13]
for i in result:
    print(type(i))
    
for i in result:
    if i > 10 :
        print(i)
        
for i in result :
    try:
        if i > 10 :
            print(i)
    except:
        print("대소비교불가")
        
        
        #####
        
for i in result :
    try:
        if i > 10 :
            if i == 11:
                print("11발견")
                pass
            print(i)
    except:
        print("대소비교불가")        
        
        

for i in result :
    try:
        if i > 10 :
            if i == 11:
                print("11발견")
                continue
            print(i)
    except:
        print("대소비교불가")        
        

for i in result :
    try:
        if i > 10 :
            if i == 11:
                print("11발견")
                break
            print(i)
    except:
        print("대소비교불가")        
        
##pass : 하던 일 계속 해 , continue : 밑에 줄 실행하지말고 다음 루프 실행해, break : 멈춤, raise exception : 에러 발생시 문구 표시 
        


for i in result :
    try:
        if i > 10 :
            if i == 11:
                print("11발견")
                raise Exception("에러")
            print(i)
    except Exception as e :
        print(e)
        print("대소비교불가")        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        