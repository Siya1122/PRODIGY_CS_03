import re

def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Password should be at least 8 characters long")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add at least one number")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add at least one special character")

    if score <= 2:
        strength = "Weak"
    elif score == 3:
        strength = "Medium"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    print("\n" + "=" * 40)
    print("Password:", password)
    print("Strength:", strength)

    if suggestions:
        print("Suggestions:")
        for s in suggestions:
            print("-", s)

test_passwords = [
    "abc",
    "abc123",
    "Password123",
    "Password@123"
]

for pwd in test_passwords:
    check_password_strength(pwd)
