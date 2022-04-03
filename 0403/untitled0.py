#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 20:50:02 2022

@author: bgfretail
"""

#####함수
def sum1(a,b):
    return a+b

a = sum1(1,2)

def sum1_1(a,b):
    return a,b,a+b

d,e,f = sum1_1(3,4)
g = sum1_1(1,2)

######
def sum2(a,b):
    if type(a) == int and type(b) == int:
        return a+b
    else:
        print("숫자입력해")
        
        
sum2(2,3)
sum2('sdf', '12')

###
def sum3(*a):
    return sum(a), type(a)

sum3(1,2,3,4)

####
def exer(name, *args):
    print(name)
    print(len(args))
    print(type(args))
    
exer("정혜영", 1,2,3)

##
def mean1(**a):
    print(type(a))
    return sum(a.values())

mean1(a=1,b=2)


#########class

class coin :
    def __init__(self,name):
        self.name = name
        self.shares = 0
    
    def buy(self, shares):
        self.shares += shares
        print(self.name + " 코인 {} 개 매수완료".format(shares))



eos = coin("EOS")
eos.buy(4)



##
class squid_game:
    def __init__(self, *args):
        self.data = list(args)[0]
        print("참가자 명단은 아래와 같습니다. \n" + str(self.data))
        
    def check(self):
        print(self.data)
        print(type(self.data))
        return self.data
    
    def fail(self, *args):
        self.data = [x for x in self.data if x not in list(args)[0]]
        print(args)
        print(type(self.data))
        return self.data

    def fail2(self,*args):
        args = list(args)[0]
        print(len(args)) 
        for i in range(0, len(args)):
            print(args[i])
            self.data.remove(args[i])
            
        return self.data
    
    def night_random_fight(self, num):
        for i in range(num):
            j = self.data.pop()
            print("{}번째 참가자 탈락".format(j))
        return self.data
                  

first_list = list(range(1,51))
first_comp = squid_game(first_list)

a = first_comp.check()

import random
first_dead_list = random.sample(first_list, 10)

first_live_list = first_comp.fail(first_dead_list)

second_dead_list = random.sample(first_live_list, 10)

second_live_list = first_comp.fail2(second_dead_list)



























