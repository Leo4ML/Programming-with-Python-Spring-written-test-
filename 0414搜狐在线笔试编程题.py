# -*- coding: utf-8 -*-


n= int(raw_input())
rule=[]
for i in range(n):
    rule.append(map(int,raw_input().split()))

def score_task(l):
    return l[2]
def score_day(l):
    return (l[2]-l[1]+1)*l[3]

def score(l):
    s1=0
    s2=0
    for i in range(len(l)):
        if l[i][0]==2:
            if l[i][1]>0:
                s1=s1+score_task(l[i])
                
        if l[i][0]==1:
            s2=s2+score_day(l[i])
            
    return s1+s2
print score(rule)