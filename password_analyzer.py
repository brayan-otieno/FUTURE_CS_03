# import re for regular expressions
import re

# function to assess the strength of a password and initialize value to 0
def assess_password_strength(password):
    score = 0

    # check if the password length is at least 12 characters
    if len(password) >= 12:  # corrected 'paswword' to 'password'
        score += 1

    # check for at least one uppercase letter
    if re.search(r'[a-z]', password):  # corrected to search for lowercase
        score += 1

    # check for at least one special character
    if re.search(r'[!@#$%^&*(),.?":|<>]', password):  # removed unnecessary space
        score += 1

    # check if the password is in the common password list
    common_passwords = {"password", "123456", "123456789", "qwerty", "abc123"}
    if password.lower() in common_passwords:  # added parentheses for method call
        return "Very weak: Use a strong password."

    # Return strength assessment based on score
    if score < 2:
        return "Password is weak."
    elif score == 2:
        return "Moderate Password strength." 
    else: 
        return "Strong Password."   

# Define a function to generate a report on password strength
def generate_report(password):

    # Assess the password strength
    strength = assess_password_strength(password)  
    recommendations = []  

    # Generate recommendations based on the strength
    if "Weak" in strength:
        recommendations.append("Increase Password length and complexity.")
    if "Very weak" in strength:
        recommendations.append("Avoid weak passwords.")

    # create a report dictionary
    report = {
        "Password": password,
        "Strength Assessment": strength,
        "Recommendations": recommendations
    }                       
    return report

# Define main function to run the password analyzer
def main():
    # Prompt the user to enter a password
    password = input("Enter a password:")

    # Generate a report based on the entered password
    report = generate_report(password)

    # Print the report
    print("\n--- Password Strength Report ---")
    print(f"Password: {report['Password']}")
    print(f"Strength Assessment: {report['Strength Assessment']}")  # removed duplicate word

    # Print recommendations if any
    if report["Recommendations"]:  # corrected the key name
        for recommendation in report["Recommendations"]:  # corrected the key name
            print(f"- {recommendation}")
    else:
        print("No recommendations needed. Good job!")  # corrected the spelling of print

# Run the main function when the script is executed
if __name__ == "__main__":
    main()                 
