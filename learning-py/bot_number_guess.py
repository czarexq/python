import random

count = 0
low = 1
high = 100

print("Think of number 1-100")

while True:
    guess = (low + high) // 2
    count += 1
    question = input(f"Is your number {guess}? (yes/lower/higher): ").lower()
    
    if question == "lower":
        high = guess - 1
    elif question == "higher":
        low = guess + 1
    elif question == "yes":
        print(f"YAAY I GUESSED IT AT MY {count} attempt")
        break
    else:
        print("Invalid operation")