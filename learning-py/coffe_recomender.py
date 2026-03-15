mood = input("What's your mood? (sad/happy): ").lower()
time_of_the_day = input("What's the time of the day? (morning/afternoon/evening): ").lower()

if mood == "sad":
    if time_of_the_day == "morning":
        print("Best for you will be latte macchiato <3")
    elif time_of_the_day == "afternoon":
        print("Best for you will be iced coffe!")
    else:
        print("No coffeine before sleep!")
elif mood == "happy":
    if time_of_the_day == "morning":
        print("Best for you will be juicy tea")
    elif time_of_the_day == "afternoon":
        print("Best for you will be apple juice")
    else:
        print("Best for you will be iced water")   
else:
    print("Invalid input!")