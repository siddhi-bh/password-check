#CLI version

import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Use at least 8 characters.")

    # Upper and lowercase
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Mix uppercase and lowercase letters.")

    # Numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number.")

    # Symbols
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one special symbol.")

    # Final rating
    if score == 4:
        return "✅ Strong password!", feedback
    elif score == 3:
        return "🟡 Moderate password.", feedback
    else:
        return "🔴 Weak password!", feedback

# Run it
password = input("🔐 Enter your password: ")
strength, suggestions = check_password_strength(password)
print("\nPassword Strength:", strength)
if suggestions:
    print("Suggestions to improve:")
    for s in suggestions:
        print("-", s)
