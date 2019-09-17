# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 12:59:45 2019

@author: vlunati
"""

from pylab import *
t = linspace(0, 10*pi, 1000)
z = sin(t)*exp(-t/10)
plot(t,z,'b-')
title("Cool! It works!")
xlabel("time")
ylabel("displacement")
show() 

x1 = 10 + 10*t
x2 = 5-5*t+0.5*2*t**2
dx = x2-x1

plot(t,x1,'b*')


plot(t,x2,'r*')
plot(t,dx,'g')
grid()
show()