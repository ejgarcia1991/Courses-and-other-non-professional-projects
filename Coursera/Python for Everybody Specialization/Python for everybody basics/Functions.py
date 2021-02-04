def computepay(h,r):
    h2=h
    extra=0
    if(h>40):
        h2=40
        extra=(h-40)*r*1.5
    return h2 * r + extra

hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))

p = computepay(hrs,rate)
print("Pay",p)