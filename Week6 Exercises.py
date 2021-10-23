# -*- coding: utf-8 -*-
"""
Created on Sat May 23 19:37:43 2020

"""

def acceleration(dist1, dist2):
    G = 6.67408*(10**-11)
    M_1 = 10**20
    return G*M_1*(dist2-dist1)/abs((dist2-dist1)**3)

def vel2(formervel, dTime, acceleration):
    return formervel+ dTime * acceleration
    
def position(vel2, dTime, prevPosition):
    return prevPosition + dTime * vel2

print(position(vel2(-6.67408, 1000, acceleration(993325.92,6.67408*10**(-5))), 1000, 993325.92))
        