# Week 5 Practicals

## Problem 1: Baking a Cake

`````python
# Ingredients list
ingredients = ["flour", "eggs", "milk", "butter", "sugar"]

# Mix into batter and put it in pan
mix the bowl until it is batter
pour batter into pan

#set oven to 400 F and cooj for 20 minutes
Temp = 400
time = 20

# Stab the cake with a knife to test it

# Keep baking while batter sticks to the knife
while batter sticks to knife:
    bake 3 more minute
    time = time + 3
    stab cake with knife

# Loop ended so the knife came out clean
take cake out of oven
print("cake is done")
`````



## Problem 2: Fizz Buzz
### The purpose of this is to write pseudocode and actual code for the Fizz Buzz game.
### Pseudocode Script

```python

# for loop for going through the numbers 1 to 100
for x in range(1, 101):
    if x is divisible by 15:     # divisible by both 3 and 5
        print("fizzbuzz")
    elif x is divisible by 3:
        print("fizz")
    elif x is divisible by 5:
        print("buzz")
    else:
        print(x)                 # not divisible by 3 or 5, so print the number

```
#!/usr/bin/env python3

### Python script
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
