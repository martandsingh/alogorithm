#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 13:42:57 2019

@author: CodeMakerz
"""

def func(text:str) -> bool:
    is_true = False
    for i in range(int(len(text)/2)):
        if text[i] == text[len(text)-1-i]:
            is_true = True
        else:
            is_true = False
    return is_true


