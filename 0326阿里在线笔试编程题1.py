# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 14:13:09 2018

@author: Leo
"""
import time
import numpy as np
#s = (n+1)**2-1

def line(x, y):
    a=np.true_divide(y, x)
    return a

if __name__=='__main__':
    t=time.time()
    n = int(raw_input())
    new=[]
    for x in range(1, n+1):
        for y in range(x):
            new.append(line(x, y))
    print len(set(new))*2+1
    print 'time is:%f ms' % (time.time()-t)
