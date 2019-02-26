"""
stringjumble.py
Author: Andrew
Credit: realpython, Matt, stackoverflow

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
txt = str(input("Please enter a string of text (the bigger the better): "))
print('You entered "'+txt+'". Now jumble it:')

def reverse(txt): 
  str = "" 
  for i in txt: 
    str = i + str
  return str
print(reverse(txt))

b = txt.split(" ")

print(reverse(b))

def reverse2(b):
    vga = ""
    for j in b:
        vga = j + vga
    agv = " ".join(vga)
    return vga
print(reverse2(b))

f = txt.split(" ")

"""
def reverse(txt):
    print(txt[::-1])

words = txt.split(" ")

def reverse2(words):
    words = words[-1::-1]
    text = ' '.join(words)
print(reverse2(words))
    
def reverse3(words):
    str = txt.split(" ")
    nw = [w[::-1] for w in str]
    nt = ' '.join(nw)
    print(nt)

reverse(txt)
reverse2(words)
reverse3(words)

"""
