#This is a game based on coin tossing to determine if it is heads or tails

#create a variable and use random
import random
heads = 0
tails = 0
number_of_tries = 0 


while number_of_tries < 50:
    number_of_tries = number_of_tries + 1
    coin_toss = random.randint(1, 2)
#two choices, if 1 is chosen at random it will be Heads, if two is selected, then it will be tails
    if coin_toss == 1:
        #print('Coin toss - Heads')
        heads = heads + 1
    elif coin_toss == 2:
        #print('Coin toss - Tails')
        tails = tails + 1
head = float(heads)
tail = float(tails)
average_percent_head = head/number_of_tries
average_percent_tail = tail/number_of_tries

total = number_of_tries
print "-------Print Summary of Coin Tosses------------------------------"
print "The number of coin toss for heads: ", heads
print "The number of coin toss for tails: ", tails
print  "The total number of tries", total
print "The percentage of coin toss for heads are", average_percent_head
print "The percentage of coin toss for tails are", average_percent_tail


