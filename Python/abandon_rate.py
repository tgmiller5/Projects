#This is a quick program for the Abandoned rate calculation helpdesk that can be used daily or monthly
#Calls Presented and Calls Abandoned are the factors

def abandoned(calls_presented, real_abandoned):
    return real_abandoned/calls_presented

calls_presented = float(raw_input("Enter the number of Calls Presented " ))
real_abandoned = float(raw_input("Enter the real abandoned calls number " ))

total_abandoned_presented = (real_abandoned/calls_presented)* 100
overall_total = round(total_abandoned_presented, 2)

print "The total abandoned rate is", overall_total
