import random

def guess_age():
    print("Hello! I'm going to try to guess your age.")
    name = input("What's your name? ")
    
    while True:
        age_guess = random.randint(15, 30)
        
        response = input(f"Is your age {age_guess}? (y/n): ").strip().lower()
        
        if response == 'y':
            print(f"Yay! {name} is {age_guess} years old.")
            break
        else:
            print("Rats! Let me try again.")

guess_age()