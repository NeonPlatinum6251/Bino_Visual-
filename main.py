
import math
import turtle

sigmasums =0.0
X= 0.0
P = [0.05, 0.10, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]
N = int(input("Enter the number of trials: "))  # gets the N for the equation

def binocd(N, X, P):  # doin' tha maff
    if X < 0 or X > N:
        return 0
    return math.exp(X * math.log(P) + (N - X) * math.log(1-P))

def howtafindX(N,P):  # this finds how many successes we can have before it is guaranteed calculated by the first time X equals 1 when p is 0.5
    count = 0
    while True:
        probab = [binocd(N,X,p) for p in P]
        if any(prob >= 1 for prob in probab):
            break
        count += 1

    return count

# Captial sigma (Σ) applies the expression after it to all members of a range and then sums the results. VERY IMPORTANT NEED TO REMEMBER

def sigma(X, sigmasums, equation, N, P):  # this is going to be used in the equation for working out the probability
    for i in range(0, X + 1):
        sigmasums += equation(N, i, P)
    return sigmasums


def equation(N,i,P): #stupid fucking function
    return binocd(N,i,P[i%len(P)])

def calcprobs(N, P):
    probabilities = []
    for p in P:
        X = howtafindX(N,[p]) #x for each probability
        result = sigma(X, 0, equation, N, [p])
        probabilities.append(result)
    return probabilities

#chooses which colour to use
def colours(probability):
    if probability <= 0.2:
        return "red"
    elif probability <= 0.5:
        return "orange"
    elif probability <= 0.8:
        return "yellow"
    else:
        return "green"
 # sets up the turtle screen and draws the stuff   
def drawresults(probabilities):
    screen= turtle.Screen()
    screen.setup(width=600, height=400)
    screen.bgcolor("white")
    turtle.speed(0)
    
    square_size = 30
    space = 50
    yposition = 0

    for i, probability in enumerate(probabilities):
        colour=colours(probability)
        turtle.penup()
        turtle.goto(-300+ i * space, yposition)
        turtle.pendown()
        turtle.fillcolor(colour)
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(square_size)
            turtle.left(90)
        turtle.end_fill()
    turtle.hideturtle()
    turtle.done()    
    
X=howtafindX(N,P)
result = sigma(X,sigmasums,equation,N,P)
print(result)
print(X)

drawresults(probability)
