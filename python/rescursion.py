#Fibonacci Recursive
""" def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) """

def fibonacci(n):
    return n if n<=1 else fibonacci(n-1)+fibonacci(n-2)

def printFibonacci(num):
    #print(' '.join(str(fibonacci(i)) for i in range(num)))
    print(*(fibonacci(i) for i in range(num)))

##Factorial Recursion
def genFactorial(num):
    return 1 if num<=1 else num * genFactorial(num-1)  

##Get GCD of numbers in recursive way
def getGCDRecursive(i,j):
    return i if j==0  else getGCDRecursive(j,i%j)

##GCD of given numbers
def getGCD(i,j):
    divsor = 0
    dividend = 0
    
    if i>j:
        dividend = i
        divsor = j
    else:
        dividend = j
        divsor = i
    
    while divsor:
        dividend,divsor = divsor, dividend%divsor
    return dividend
"""     while (divsor != 0): #while divsor:
        quot = dividend%divsor #dividend,divsor = divsor, dividend%divisor
        dividend = divsor
        divsor = quot
    return dividend """
    
# Example usage:
n = 5  # Change this value to generate the nth Fibonacci number
print(f"Fibonacci number at position {n} is: {fibonacci(n)}")
print(f"Fibonacci numbers for input {n} is: {printFibonacci(n)}")
print(genFactorial(n))
print(getGCD(10,6))
print(getGCD(48,18))
print(getGCD(17,17))
print(getGCD(13,17))
print(getGCDRecursive(17,13))
print(getGCDRecursive(48,18))



