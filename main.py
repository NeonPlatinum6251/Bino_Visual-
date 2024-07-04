
import math
import turtle #fuck it we are turtling

N=int(input("Enter the number of trials: "))          #gets the N for the equation
def init():
    X=0   #these are going to be shown on the y-axis, it is the amount of successes for N trials it is not necessary but it prevents one big block of colour at the bottom
    P=[0.05,0.10,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5] #this is going to be the probabilities of success shown on the x-axis, might add more later
    sigmasums=0
    return X, P, sigmasums

def howtafindX(X): #this finds how many successes we can have before it is guaranteed calculated by the first time X equals 1 when p is 0.5
    while X!=1:
        X=binocd(N,X,P)


    return

#Captial sigma (Σ) applies the expression after it to all members of a range and then sums the results. VERY IMPORTANT NEED TO REMEMBER
def sigma(X,sigmasums): #this is going to be used in the equation for working out the probability
    for P in range(0,X+1):
        sigmasums+=binocd(N,X,P)
        
    return sigmasums

def binocd(N,X,P): # doin' tha maff  

    colourstrength=   #I will store the answer of the binomial as the colour strength

    return colourstrength

def colourvalue(colourstrength):


