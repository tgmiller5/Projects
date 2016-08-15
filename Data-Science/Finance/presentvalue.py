
#formula for growing perpetituity is C/R-g
#Cash flow number is 12.50
#discount rate which is R will be 8.5
#constant growth rate which is g will be 2.5


#Create input values
cash_flow = float(raw_input("Enter a cash flow number: "))
discount_rate = float(raw_input("Enter a discount rate: "))
growth_rate = float(raw_input("Enter a growth rate: "))
pvgrow = cash_flow/(discount_rate - growth_rate)

#print out value and round to two decimal places
print "The present value of this growing perpetuity is:", round(pvgrow, 2)
