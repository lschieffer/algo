""" Guess my number, given a range how many tries will it take to find it?"""

### import files needed ###
import random

### define funcitons to use ###
def mid(f, c):
    t =  (f + c) / 2
    # Solve for round down errors
    if t == c:
#        return c
        t += 1
    print "the floor is " + str(floor) + " and the ceiling is " + str(ceiling)
    return t

def higher_lower(n):
    if  n < secret_num:
        return "lower"
    else:
        return "higher"

### start the game ###
range = raw_input("Please provide a maximum number for our game: ")

# Ensure you have an integer
if range.isdigit():
    print "thanks"
else:
    range = raw_input("I need a positive integer: ")
    while range.isdigit() == False:
        print "common man..."
        range = raw_input("I need a positive integer: ")


# set varriables to use
floor = 0
ceiling = int(range)
fail = ""
out_of_range = False

# choose a random number
secret_num = random.randint(floor,int(range))
print "the secret number is " + str(secret_num)

# Uncomment to force the secret_num and test edge cases: 0, 100
#currently there is an optimization to be made, when the range is 0 - 0 it takes one extra guess
#secret_num = 0
#currently there is an optimizaiton to be made, when the number is the maximum it takes one extra guess
#secret_num = 100
#print "the secret number is " + str(secret_num)


# start guessing
g = mid(floor, ceiling)
count = 0
while g != secret_num:
    count += 1
    # Check for illogical conditions
    if floor > ceiling:
        out_of_range = True
        break
    # Prevent the loop from running too long
    elif count == 25:
        fail = "f"
        break
    # Check to see if you are too high
    elif higher_lower(g) == "higher":
        ceiling = g
        g = mid(floor, ceiling)
    # Check to see if you are too low
    else:
        last_floor = floor
        floor = g
        g = int(g) + int(ceiling)
        g = mid(floor, ceiling)
        # Check to see if I"m repeating on the edge of the range
        if last_floor == g:
            print "repeating"
            g += 1

# Increment counter for success
if fail != "f":
    count += 1

# Disposition the results
if g == secret_num:
    print "Final guess is " +str(g) + ". It took " + str(count) + " tries to guess the number"
elif out_of_range == True:
    print "The secret number was forced outside the range entered..."
else:
    print "The answer is between " + str(floor) + " and " + str(ceiling)
    print "I tried " + str(count) + " times and didn't get it, I give up..."
