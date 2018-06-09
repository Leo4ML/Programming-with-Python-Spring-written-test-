# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 21:06:45 2018

@author: Leo
"""
import numpy as np
import time

n,k=map(int, raw_input().split())

def count(n,k):
    c=0
    if k==0:
        return n**2

    for y in xrange(k+1,n+1):
        c=c+n/y*(y-k)
        if n%y>=k:
            c=c+(n%y-k+1)
    return c

if __name__=='__main__':
    start=time.clock()
    print count(n,k)
    end=time.clock()
    print 'time is :',end-start,'s'
        