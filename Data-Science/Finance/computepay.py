#This is compute the pay based on hourly rate and if it is time and a half

def computepay(h, r):
    if   h <= 40:
         p = r * h
         
    else:
         p = r * 40 + (r * 1.5 * (h-40))
         return p
try:
    inp = raw_input("Enter Hours:")
    hours = float(inp)
    inp = raw_input("Enter rate:")
    rate = float(inp)
except:
    print "Error please enter numeric input"
    quit()


pay = computepay(hours, rate)
print "The pay will be", pay
