"""Hey welcome to my module called module1 from package package"""

def isEven(num):
    """Check whether a number is even or not"""
    if num % 2 == 0:
        return True
    return False


def factorial(num):
    """Generates factorial of a number"""
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact

pi = 3.14
gravity = 9.9


def isOdd(num):
    """Check whether a number is odd or not"""
    if num % 2 == 0:
        return False
    return True
