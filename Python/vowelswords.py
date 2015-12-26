#Python program created to enter in a sentence and it will tell you have many vowels within that word

print "Enter a sentence and it will output how many vowels and the amount of words there are from the sentence"
print ""

from collections import Counter
mydata = raw_input("Enter a sentence: " )
vowels = "aeiouAEIOU"
for t in vowels:
    print "The vowel count for: ", t, mydata.count(t)

word = Counter(mydata.split())
print "The count of words within the sentence are : ", word

