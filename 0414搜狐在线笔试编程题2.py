# -*- coding: utf-8 -*-

m= map(int,raw_input().split())
n=m[0]
k=m[1]
L=map(int,raw_input().split())

def fenduan(L,k):
    new=[]
    for i in range(k):
        if i <k-1:
            new[i]=L[(i)*len(L)/k:(i+1)*len(L)/k]
        if i==k-1:
            new[i]=L[(i)*len(L)/k:]
    return new
List=fenduan(L,k)
new=[]
for i in range(len(List)):
    new.append(min(List[i]))
print new.sort()