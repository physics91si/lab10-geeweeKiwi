#!/usr/bin/python
import sys

#Python script that returns the roots of a quadratic equation
#of the form a*x^2 + b*x + c = 0
#Enter values for a, b, and c in the command line
#e.g. run: >python quadratic.py 1 2 -15
def main():
    a = sys.argv[1]
    b = sys.argv[2]
    c = sys.argv[3]
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        print("Please input numbers")
        sys.exit(1)
    
    try:
        x1, x2 = find_roots(a, b, c)
        print ("This is x1: %f" %x1)
        print ("This is x2: %f" %x2)
    except ValueError:
        print("The roots are imaginary")
    except ZeroDivisionError:
        try:
            x1 = -1.*c/b
            print("You entered a linear equation, and it's root is %f" %x1)
        except ZeroDivisionError:
            print("You entered a degenerate equation that has no solution")
    
    


def find_roots(a,b,c):
    mid = b**2 - 4*a*c
    sqrt_mid = mid**(1./2)
    x1 = (-b + sqrt_mid)/(2*a)
    x2 = (-b - sqrt_mid)/(2*a)
    return x1, x2


if __name__=="__main__":
        main()
