# -*- coding: utf-8 -*-
import math

n=int(raw_input())


def huiwen(n):
    s=bin(n)[2:]
    if panduan(s):
        return True
'''
def panduan(s):
    if len(s) < 2: 
        return True
    if s[0]!=s[-1]: 
        return False
    return panduan(s[1:-1])  
    '''
def panduan(s):
    b=s[::-1]
    return s==b
if n>16:
    q=int(math.log(n,2))
    n=n-2**q-1
c=0
for i in range(1,n+1,2):
    if huiwen(i):
        c=c+1
print c+1