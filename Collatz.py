#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def collatz(number):
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            print(number)

        elif number % 2 == 1:
            number = number * 3 + 1
            print(number)
try:
    playerNumber = int(input())
    collatz(playerNumber)
except ValueError:
    print ('You need to enter a number')
    

