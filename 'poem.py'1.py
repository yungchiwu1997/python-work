# coding: utf-8
from numpy.random import randint
for i in range(10):
    print(randint(1,10),end=",")
words='''我
你
花朵
微風
輕輕
親親
靈魂
文山區
思念
他
你們
忘記
哭
悄悄的
青春'''
phrase = words.split("\n")
from numpy.random import sample, choice    
n=randint(3,6)
for i in range(n):
    k = randint(1,5)
    egg = choice(phrase,k)
    ham = " ".join(egg)
    print(ham)
