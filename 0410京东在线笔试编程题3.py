# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 20:25:52 2018

@author: Leo
"""
s=raw_input()

def huiwen(s):
    s=''.join(s)
    if s==s[::-1]:
        return True
    
def delete(s):
    c=len(s)
    for i in range(len(s)):
        news=list(s)
        news=del(news[i])
        if huiwen(news):
            c=c+1
    s=del(s[0])
    delete(s)
    return c

print delete(s)