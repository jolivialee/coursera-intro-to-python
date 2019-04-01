# Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate)
# Hours: 45; rate: 10; pay: 475.0

def computepay(h,r):
    if h <= 40:
        return(h*r)
    elif h > 40:
        return(((h-40)*0.5*r)+(h*r))

hrs = input("Enter Hours:")
h = float(hrs)
rte = input("Enter Rate:")
r = float(rte)

p = computepay(h,r)
print("Pay",p)
