#! /usr/bin/python2.7

"""Daniel MIller's take on 'Fizzonacci' or otherwise Fizzbuzz + a Fibbonacci sequence generator"""
import sys

try: 
        if sys.argv[1]: limit = sys.argv[1] 
except: 
        print "Arguement not supplied in command, requesting..."
        limit = int(raw_input("What limit do you desire?: "))

a, b = 1, 1 
z = 1

while z < 100: 
        line = str(z)+". \t "
        if not (b%5 and b%3): line += "Fizzbuzz  -\t" +`b`
        elif b%3:line += "Fizz\t   -\t" + `b` 
        elif b%5:line += "Buzz\t   -\t"+`b` 
        
        print line 

        a,b=b,a+b 
        z += 1 
        



