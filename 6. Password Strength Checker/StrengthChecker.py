import string

def getInput(prompt):
    while True:
        userInput = input(prompt).strip()
        if not userInput:
            print("\nInvalid Input\n")
        else:
            return userInput

def isLong(password):
    return len(password) >= 8

def isLower(password):
    return any(char.islower() for char in password)

def isUpper(password):
    return any(char.isupper() for char in password)

def isSpecial(password):
    for char in password:
        if char in string.punctuation:
            return True
    return False


def isDigit(password):
    return any(char.isdigit() for char in password)

password = getInput("Enter password: ")

score = 0
suggestion = []

if isLong(password):
    score += 1
else:
    suggestion.append("Make your password at least 8 characters long.")

if isUpper(password):
    score += 1
else:
    suggestion.append("Add at least one uppercase letter (A-Z).")

if isLower(password):
    score +=1
else:
    suggestion.append("Add at least one lowercase letter (a-z).")

if isSpecial(password):
    score += 1
else:
    suggestion.append("Add at least one special character (e.g., !@#$%).")

if isDigit(password):
    score += 1
else:
    suggestion.append("Add at least one digit (0-9).")

match score:
    case 0:
        print("Very weak 😞")
    case 1:
        print("Very weak 😞")
    case 2:
        print("Weak 😐")
    case 3:
        print("Moderate 🙂")
    case 4 | 5:
        print("Strong 💪")

if score <=3 :
    print("\nSuggestions to improve your password:\n")
    for suggest in suggestion:
        print(f"- {suggest}")