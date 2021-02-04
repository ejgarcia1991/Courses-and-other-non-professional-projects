largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num=int(num)
        if(largest==None):
            largest=num
            smallest=num
        if(num>largest):
            largest=num
        elif(num<smallest):
            smallest=num
    except:
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)