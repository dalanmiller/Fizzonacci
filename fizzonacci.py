#! /usr/bin/python2.7

"""Daniel MIller's take on 'Fizzonacci' or otherwise Fizzbuzz + a Fibbonacci sequence generator"""
import sys

try: 
        if sys.argv[1]: limit = sys.argv[1] 
except: 
        print "Arguement not supplied in command, requesting..."
        limit = raw_input("What limit do you desire?: ")

a, b = 1, 1 
z = 1

while z < limit: 
        if (b%5 and b%3): print "Fizzbuzz, ", b
        elif b%3:print "Fizz", b 
        elif b%5: print "Buzz", b 
        a,b=b,a+b 
        z += 1 
        



