# PRODIGY_CS_03 - Password Complexity Checker

## Description
This project is a Password Complexity Checker developed in Python as part of the Prodigy InfoTech Cyber Security Internship.

The tool evaluates the strength of a password based on multiple security criteria and provides feedback to improve password security.

## Features
- Checks password length
- Detects uppercase letters
- Detects lowercase letters
- Detects numbers
- Detects special characters
- Classifies passwords as:
  - Weak
  - Medium
  - Strong
  - Very Strong
- Provides suggestions for improving weak passwords

## Technologies Used
- Python 3
- Regular Expressions (re module)

## How It Works
The program analyzes a password using the following criteria:

1. Minimum length of 8 characters
2. Presence of uppercase letters
3. Presence of lowercase letters
4. Presence of numbers
5. Presence of special characters

Based on these checks, a strength score is calculated and displayed.

## Example Output

========================================

Password: abc

Strength: Weak

Suggestions:

- Password should be at least 8 characters long
- Add at least one uppercase letter
- Add at least one number
- Add at least one special character

========================================

Password: Password@123

Strength: Very Strong

## Project Structure

PRODIGY_CS_03

├── password_checker.py

└── README.md

## Author

Siya Shinde

Cyber Security Intern at Prodigy InfoTech
