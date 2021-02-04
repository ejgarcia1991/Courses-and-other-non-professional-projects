hrs = input("Enter Hours:")
h = float(hrs)
rph = input("Enter rate per hour:")
rph = float(rph)
if(h>40):
    extra = (h-40)*rph*1.5
    h=40
pay = h * rph + extra
print(pay)