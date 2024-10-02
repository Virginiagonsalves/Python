def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

    #Input the number
num=int(input("Enter a number to find its factorial:"))

    #Check if the number is negative
if num<0:
        print("Factorial is not defined for negative numbers.")
elif num==0:
        print("Factorial of 0 is 1")
else:
        print("Factorial of",num,"is",factorial(num))
            
        
