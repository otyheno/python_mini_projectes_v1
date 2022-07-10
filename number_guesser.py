
import random

top_of_range = input("Type an Number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range<=0:
        print("Please type a number greater than 0")
        quit()
else:
    print("Please type a number next time")
    quit()   
#randrange generates random number upto -1 stop, randint generates random number including the stop value
random_number = random.randrange(top_of_range)
#print(random_number)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Guess a Number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue
    
    if user_guess == random_number:
        print("Hurray...You Got It")
        break
    else:
        print("Ooops! Thats not correct") 
        
print("You got It in", guesses, "guesses")