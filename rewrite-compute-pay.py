# Prompt user to compute pay with overtime pay
# Hours: 45; rate: 10; pay: 475.0

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
