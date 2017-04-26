
#coding=utf-8

import cx_Oracle

#import sys

#import urllib

#import os

#import json

import numpy as np

import matplotlib.pylab as plt

#import pandas as pd  
cr.execute(sql)

rs=cr.fetchall()
#print rs[0][0]
#print rs[0][1]
b=[]
b1=[]

for i in rs:
     #print i[0]print n1
    pdf=[]
    b.append(i[1])
    b1.append(i[0])
     #print i[1]
      
#print b
#plt.plot(b)
#plt.show()


num=30
bins=[]
n=[]

def abc(b,num):
    pdf=[]
   
    [n, bins,patchs] = plt.hist(b,num)
   

    for n1 in n:
        p=n1/float(sum(n))/float(bins[2]-bins[1])
        pdf.append(p)
    return pdf
    pdf = abc(b,num)
    print pdf
    pdf1=np.array(pdf[0])
    plt.plot(pdf[1][0:-1],pdf1)
    plt.show()
