#!/usr/bin/env python

def helloworld():
    print("Hello, World!")

helloworld()    

def mysum(x, y):
    return x+y

def mysum2(x, y, z):
    return z + mysum(x, y)

a = mysum(2, 3)    
print(f"First function: {a}")

b = mysum2(5, 1, 6)
print(f"Second function: {b}")