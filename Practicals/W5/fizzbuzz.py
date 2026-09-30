#!/usr/bin/env python3

# fizzbuzz loop
for x in range(1, 100):
    if x % 15 == 0:      # divisible by both 3 and 5
        print("fizzbuzz")
    elif x % 3 == 0:     
        print("fizz")
    elif x % 5 == 0:    
        print("buzz")
    else:                # not divisible by either so just print the number
        print(x)
