import random
name = input("What is your name? " )
fav_color = input("What is your favorite color? ")
randnum = random.randint(1, 100)

print ("My name is {0} and my favorite color is {1}".format(name, fav_color))
print("The number that I have chosen for you is", randnum)
