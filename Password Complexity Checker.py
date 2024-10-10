import re

def password_strength_checker(password):
    # Criteria checks
    length_check = len(password) >= 8
    upper_check = re.search(r"[A-Z]", password)
    lower_check = re.search(r"[a-z]", password)
    number_check = re.search(r"[0-9]", password)
    special_check = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    # Feedback on password strength
    strength = 0
    if length_check:
        strength += 1
    if upper_check:
        strength += 1
    if lower_check:
        strength += 1
    if number_check:
        strength += 1
    if special_check:
        strength += 1

    # Give feedback based on the strength score
    if strength == 5:
        return "Password is very strong!"
    elif 3 <= strength < 5:
        return "Password is strong!"
    elif 2 <= strength < 3:
        return "Password is weak, consider improving it."
    else:
        return "Password is very weak!"

# Test the function
password = input("Enter your password: ")
print(password_strength_checker(password))
