# -*- coding: utf-8 -*-

import math

def isPrime(n): 
    if n <= 1: 
        return False 
    i = 2 
    while i*i <= n: 
        if n % i == 0: 
            return False 
        i += 1 
    return True 

n=int(raw_input())

primelist=[]
for i in range(n+1):
    if isPrime(i):
        primelist.append(i)
        
m=int(math.log(n,2))
c=0
con=[]
for i in primelist:
    for s in range(m):
        if i**s<=n:
            con.append(i**s)
            
print len(set(con))
    