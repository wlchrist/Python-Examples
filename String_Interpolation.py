# We're going to learn how to insert numbers into the middle of a string
# You can do this with normal concatenation
# But we want to make clean code, so there's a better way to do it

name = "Warren"
head = 1
legs = 2

print(name + " has " + str(head) + " head and " + str(legs) + " legs")

alien = "Flerb"
alien_heads = 3
alien_legs = 10

# f strings are better, since you can input an integer without the need to convert it to a string manually

print (f"{alien} has {alien_heads} heads and {alien_legs} legs!")

# pre-python 3.6, the same thing could be done with .format(), I'll demonstrate that as well

print("{} has {} heads and {} legs!".format(alien, alien_heads, alien_legs))
