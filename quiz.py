import random
n=random.randint(1,100)
if(n%29==0):
    a=-1
    Guesses=0


    while(a != n):
        a=int(input("Enter a Number: "))
        if(a>n):
            print("Lower Number Please")
        elif(a<n):
            print("Higher Number Please")

        Guesses+=1    


    print(f"You Guess the number {n} in {Guesses} attempts")    
else:
    print("random number is not divided by 29")

