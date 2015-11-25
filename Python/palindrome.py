def palindrome(t):
   return t == t[::-1]

my_palindrome = raw_input(“Enter a word to determine if it can read backwards ”)
print “If it gives the word True, it is a palindrome”
print “If it is gives the word False, it is not a palindrome”
print “”
print “It is”, palindrome(my_palindrome)
