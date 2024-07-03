
import math
import numpy as np
from itertools import product
import turtle
#from scipy.stats import binom

N=int(input("Enter the number of trials: "))      #gets the N for the equation
def init():
    X=0                                                #these are gonna be shown on the y-axis, it is the amount of successes for N trials
    P=[0.05,0.10,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5] #this is gonna be the probabilities of success shown on the x-axis
    sigmasums=0
    return X, P, sigmasums
def howtafindX(X): #this finds how many successes we can have before it is guaranteed calculated py the first time X equals 1 when p is 0.5
    while X!=1:
        X=binocd(N,X,P)
        maxtrials=N

    return
def binoequation():


    return
#Captial sigma (Σ) applies the expression after it to all members of a range and then sums the results. VERY IMPORTANT NEED TO REMEBER
def sigma(X,sigmasums,): #this is gonna be used in the equation for working out the probability
    for i in range(X):
        sigmasums=sigmasums+(X*X)
        X=X-1

    return
def binocd(N,X,P): # doin' tha maff

    colourstrength=   #I will store the answer of the binomial as the colour strength

    return colourstrength
def colourvalue(colourstrength):


