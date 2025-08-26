# Basic Calculator Program

This repository contains a simple Python program that functions as a basic calculator.  
It prompts the user for two numbers and an operation, performs the calculation, and prints the result.

---

## Features

- Addition `+`
- Subtraction `-`
- Multiplication `*`
- Division `/` with explicit handling for division by zero

---

## Program Code

Save the file as `basic-calculator-program.py`.

~~~python
# Basic Calculator Program

# Ask user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")

# Perform calculation
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please choose +, -, *, or /.")
~~~

---

## Usage

Run the program with Python 3.

~~~bash
python basic-calculator-program.py
~~~

---

## Example
Enter the first number: 10
Enter the second number: 5
Enter an operation (+, -, *, /): +
10 + 5 = 15
---

## Requirements

- Python 3.x

---

## Clone This Repository

To clone this repository to your local machine:

```bash
git clone https://github.com/damilareadekeye/basic-calculator-program.git
cd basic-calculator-program
```

## OR 

## Create the GitHub Repository on the Website

1. Open https://github.com/new  
2. Repository name: `basic-calculator-program`  
3. Visibility: Public  
4. Do not initialize with a README (you already have local files)  
5. Click **Create repository**

---

## Push Your Local Project to GitHub

Execute these commands inside your project folder.

~~~bash
# Initialize git if you have not done so already
git init

# Add files and commit
git add basic-calculator-program.py README.md
git commit -m "Add basic calculator program and README"

# Ensure your branch is named main
git branch -M main

# Add the correct remote. Replace <YourGitHubUsername> with your actual username
git remote add origin https://github.com/<YourGitHubUsername>/basic-calculator-program.git

# Push to GitHub
git push -u origin main
~~~

---

## Alternative: Create the Remote Repository Without Opening a Browser

### Option A - GitHub CLI

Prerequisites: Install GitHub CLI and authenticate once.

~~~bash
# Install GitHub CLI if needed: https://cli.github.com/
# Authenticate once
gh auth login

# Create the repo from the current directory and push in one step
gh repo create basic-calculator-program --public --source=. --push
~~~

### Option B - Visual Studio Code

1. Open the folder in VS Code  
2. Ensure you are signed in to GitHub in VS Code  
3. Open the **Source Control** panel  
4. Click **Publish to GitHub** and follow the prompts  
5. VS Code will create the repository online and push your code

---

## Troubleshooting

- Error: `remote: Repository not found` or the remote still points to an incorrect URL  
  Fix by removing and re-adding the remote.

~~~bash
# Remove the incorrect remote
git remote remove origin

# Add the correct remote. Replace <YourGitHubUsername> with your actual username
git remote add origin https://github.com/<YourGitHubUsername>/basic-calculator-program.git

# Verify
git remote -v

# Push again
git push -u origin main
~~~

- Confirm that the repository actually exists on GitHub at  
  `https://github.com/<YourGitHubUsername>/basic-calculator-program`

---

## Author

**Damilare Lekan Adekeye**  
Email: damilare@damilareadekeye.com  
Portfolio: https://damilareadekeye.com
