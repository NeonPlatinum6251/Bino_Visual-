import turtle

sigmasums =float(0.0)
X= float(0.0)
P = [0.05, 0.10, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
N = int(input("Enter the number of trials: "))  # gets the N for the equation

def binocd(N, X, P):  # doin' tha maff
    return P ** X * (1 - P) ** (N - X)

def howtafindX(N,P):  # this finds how many successes we can have before it is guaranteed calculated by the first time X equals 1 when p is 0.5
    X = 0
    while True:
        probab = [binocd(N,X+1,p) for p in P]
        if any(prob >= 1 for prob in probab):
            break
        X += 1
    return X

# Captial sigma (Σ) applies the expression after it to all members of a range and then sums the results. VERY IMPORTANT NEED TO REMEMBER

def sigma(X, sigmasums,equation,N,P):  # this is going to be used in the equation for working out the probability
    for i in range(0, X + 1):
        sigmasums += equation(N,i,P)
    return sigmasums


def equation(N,i,P): #stupid fucking function
    return binocd(N,i,P[i%len(P)])

result = sigma(int(X),sigmasums,equation,N,P)
# this is just to test the maths
howtafindX(N,P)
print(result)
print(X)