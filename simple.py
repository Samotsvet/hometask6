# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 14:28:23 2020

@author: tonya
"""
def simple(x):
    return x*x

def integrate_rectangle(f, a, b, nsteps):
    measure = (b - a) / nsteps
    res = 0.
    for i in range (0, nsteps):
        res += f(a + i*measure + measure/2) * measure
    return res

def midpoint_rule(func, a, b, eps):
    nsteps = 0
    dis = 99999999
    final = 0
    while(dis>eps):
        nsteps+=1
        fir = integrate_rectangle(func, a, b, nsteps)
        sec = integrate_rectangle(func, a, b, 2*nsteps)
        dis = abs(fir-sec)
    #final = integrate_rectangle(func, a, b, nsteps)
    return nsteps
def main():
    a = 2
    b = 3
    eps=0
    for i in range(0,6):
        #print(i)
        eps = pow(10,-2*i)
        print(eps, midpoint_rule(simple, a, b, eps))
    print(midpoint_rule(simple, a, b, eps))

main()
    
    