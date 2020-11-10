#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 21:14:21 2020

@author: giri
"""

def main():
    '''
Program will displays which is highest alphabets among & its ascii value
    '''
    word = str(input("Enter your favoirate word here : "))
    first_alpha = ord(word[0]) #which converts the alphabet to its equivalent ASCII 
    
    for char in word:
        if (first_alpha == ord(char) or first_alpha > ord(char)):
            first_alpha = first_alpha
            
        elif(first_alpha < ord(char)):
            first_alpha = ord(char)
            
    print(chr(first_alpha),first_alpha)


if __name__ == "__main__":
    main()
    print(main.__doc__)
        
