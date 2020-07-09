#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time


# In[ ]:


name = input("What is your name:")
print("hello "+name+" Let's Plaay Hangman")
print(" ")
time.sleep(0.5)
print("Start guessing the word")
time.sleep(1.0)
word='smile'
guesses=''
chance=10

while chance>0:
    failed=0
    for char in word:
        if char in guesses:
            print(char),
        else:
            print('_'),
            failed+=1
            
    if failed==0:
        print("You Win!!")
        break;
    print    
    guess=input("Enter any character that best fits the word: ")
    guesses+=guess
    if guess not in word:
        chance-=1
        print("Wrong")
        
        time.sleep(0.5)
        print("Remaining ",+ chance," chance left to guess the word.")
        if chance==0:
            print("You lose!")


# In[ ]:




