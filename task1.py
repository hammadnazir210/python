import random
n=random.randint(1,100)
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
