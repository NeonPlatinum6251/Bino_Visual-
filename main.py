

sigmasums=0
X=0
P=[0.05,0.10,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5]

N=int(input("Enter the number of trials: "))          #gets the N for the equation

def init():
    #these are going to be shown on the y-axis, it is the amount of successes for N trials it is not necessary but it prevents one big block of colour at the bottom
    P=[0.05,0.10,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5] #this is going to be the probabilities of success shown on the x-axis, might add more later
    return P

def howtafindX(X): #this finds how many successes we can have before it is guaranteed calculated by the first time X equals 1 when p is 0.5
    while X != 1:
        X=binocd(N,X,P)
    
    return X

#Captial sigma (Σ) applies the expression after it to all members of a range and then sums the results. VERY IMPORTANT NEED TO REMEMBER

def sigma(X,sigmasums,equation): #this is going to be used in the equation for working out the probability
    for P in range(0,X+1):
        
        sigmasums+=equation 

    return sigmasums

def binocd(N,X,P): # doin' tha maff  
    for i in range(10):
        equation=P[i]^X*(1-P[i])^N-X 
    
        return equation


#def colourvalue(colourstrength):

#this is just to test the maths 
init()
howtafindX(X)
binocd(N,X,P)
sigma(X,sigamsums,equation)
print(sigma(X,sigmasums,equation))
