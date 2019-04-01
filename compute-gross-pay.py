#Prompt user for hours and rate per hour to compute gross pay. Hours should be 35, rate should be 2.75, pay should be 96.25

hrs = input("Enter Hours: ")
rte = input ("Enter Rate: ")
h = float(hrs)
r = float(rte)

if h > 40:
    reg = 40*r
    ot = (h-40)*1.5*r
    final = reg + ot

else: 
    final = h*r

print ("pay should be", final)
