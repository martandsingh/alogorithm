#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 16:50:45 2019

@author: martandsingh
"""

import numpy as np
rows = 13
cols = 10

top_half, bottom_half_left, top_half_right, bottom_half_right, top, bottom = int(rows/2), rows - int(rows/2), int(rows/2), rows - int(rows/2), cols, cols

#print(top_half_right, bottom_half_right)
A = [[' ' for x in range(cols)] for x in range(rows)]

def intro():
    _hyphen = '-'*5
    print(_hyphen + "welcome to the codemaker".capitalize() + _hyphen)
    print("A small program to implement seven segment numbers, which you all must have seen in digital clocks.")
    print("\nThis program will print a given number in seven segment form. It doesnt support multiple digit for now.")
    print("\nYou can download script from github repo mentioned in description.")
    print("\nAlso follow us on facebook: https://www.facebook.com/codemakerz")
    print("\n\n\n This script is not filtered. You may find some unused variables.")
    print(_hyphen + "Thank You..."+ _hyphen)
 
def get_array():
    return [[' ' for x in range(cols)] for x in range(rows)]

def show_top_left_half(A):
    for i in range(top_half):
        for j in range(1):
#            if(i%2 != 0):
            A[i][j] = '*'
    

def show_bottom_left_half(A):
    for i in range(bottom_half_left, rows-1):
        for j in range(1):
#            if(i%2 != 0):
            A[i][j] = '*'

def show_top_right_half(A):
    for i in range(top_half):
        for j in range(cols-1, cols):
            A[i][j] = '*'

def show_bottom_right_half(A):
     for i in range(bottom_half_left, rows-1):
        for j in range(cols-1, cols):
            A[i][j] = '*'

def show_top(A):
    for i in range(1):
        for j in range(cols):
            A[i][j] = '*'

def show_bottom(A):
    for i in range(1):
        for j in range(cols):
            A[rows-1][j] = '*'

def show_middle(A):
    for i in range(top_half, top_half+1):
        for j in range(cols):
            A[i][j] = "*"

def show_left_middle_dot(A):
    A[top_half][0] = "*"
    

def show_right_middle_dot(A):
    A[top_half][cols-1] = "*"

def print_number(val):
    A = get_array()
    if val == 1:
        show_top_right_half(A)
        show_bottom_right_half(A)
        show_right_middle_dot(A)
     
    elif val == 2:
        show_top(A)
        show_bottom(A)
        show_top_right_half(A)
        show_middle(A)
        show_bottom_left_half(A)
    elif val == 3:
        show_top(A)
        show_bottom(A)
        show_top_right_half(A)
        show_middle(A)
        show_bottom_right_half(A)
    elif val == 4:
        show_top_left_half(A)
        show_middle(A)
        show_top_right_half(A)
        show_bottom_right_half(A)
    elif val == 5:
        show_top(A)
        show_bottom(A)
        show_top_left_half(A)
        show_bottom_right_half(A)
        show_middle(A)
    elif val == 6:
        show_bottom(A)
        show_middle(A)
        show_top_left_half(A)
        show_bottom_left_half(A)
        show_bottom_right_half(A)
    elif val == 7:
        show_top(A)
        show_top_right_half(A)
        show_bottom_right_half(A)
        show_right_middle_dot(A)
    elif val == 8:
        show_top(A)
        show_middle(A)
        show_bottom(A)
        show_top_left_half(A)
        show_bottom_left_half(A)
        show_top_right_half(A)
        show_bottom_right_half(A)
    elif val == 9:
        show_top(A)
        show_middle(A)
        show_bottom(A)
        show_top_left_half(A)
        show_top_right_half(A)
        show_bottom_right_half(A)
    elif val == 0:
        show_top(A)
        show_bottom(A)
        show_top_left_half(A)
        show_bottom_left_half(A)
        show_top_right_half(A)
        show_bottom_right_half(A)
        show_left_middle_dot(A)
        show_right_middle_dot(A)   
    
    for i in range(rows):
        for j in range(cols):
            print(A[i][j], end=''*3)
        print('')


def main():
    is_exit = False
    intro()
    while True:
        if(is_exit):
            exit()
        else:
            num = input("enter single digit to print in digital format. Press 'y' to exit: ")
            if num.lower() == 'y':
                is_exit = True
            else:
                num = int(num)
                print("\n")
                print(print_number(num))  
                print("\n")
                
    
      
main()