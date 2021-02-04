score = float(input("Enter Score: "))
if(score<0 or score >1):
    print("Error")
    
if(score>=0.9):
    print("A")
elif(score>=0.8):
    print("B")
elif(score>=0.7):
    print("B")
elif(score>=0.6):
    print("B")
else:
    print("F")