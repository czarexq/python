def check_password_strength(password):
    score = 0

    #Lenght Points
    
    if len(password) >= 12:
        score += 3
    elif len(password) >= 8:
        score += 2
    else:
        score = 0

    #Points conditions

    has_upper = any(letter.isupper() for letter in password)
    has_lower = any(letter.islower() for letter in password)
    has_digit = any(letter.isdigit() for letter in password)
    not_isalnum = any(not letter.isalnum() for letter in password)

    if has_upper and has_lower:
        score += 2
    if has_digit:
        score += 2
    if not_isalnum:
        score += 2

    dumb_ahh_passwords = ["password", "12345567", "hasło1234", "87654321"]

    if password in dumb_ahh_passwords:
        score = 0

    #All conditions extra point

    if has_upper and has_lower and has_digit and not_isalnum:
        score += 1

    return min(score, 10)

while True:
    user_input = input("Enter your password or type 'quit' to exit: ")
    if user_input.lower() == "break":
        print("Bye!!")
        break
    else:
        print(f"I rate your password {check_password_strength(user_input)}/10")
        if check_password_strength(user_input) < 4:
            print("You need to change that bruh")