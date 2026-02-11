import random 
r=random.randint(1,100)
while True:
    guess=int(input("guess the number:"))
    if guess>r:
        print("the number lower")
    elif guess<r:
        print("The number higher")    
    else:
        print("Congratulations🎉")   
        break 