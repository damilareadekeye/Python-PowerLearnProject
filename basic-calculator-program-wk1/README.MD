# Basic Calculator Program

This directory contains a simple Python program that functions as a basic calculator. It prompts the user for two numbers and an operation, performs the calculation, and prints the result.

This script is part of the `Python-PowerLearnProject`.

---

## Features

- Addition `+`
- Subtraction `-`
- Multiplication `*`
- Division `/` with explicit handling for division by zero

---

## Program Code

The script is located at `basic-calculator-program/basic-calculator-program.py`.

```python
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
```

---

## Usage

From the root directory of the `Python-PowerLearnProject`, run the program with Python 3.

```bash
python basic-calculator-program/basic-calculator-program.py
```

---

## Example

```
Enter the first number: 10
Enter the second number: 5
Enter an operation (+, -, *, /): +
10 + 5 = 15
```

---

## Requirements

- Python 3.x

---

## Clone The Project Repository

To get a local copy of the entire project, clone the `Python-PowerLearnProject` repository:

```bash
git clone https://github.com/damilareadekeye/Python-PowerLearnProject.git
cd Python-PowerLearnProject
```

---

## Contributing to the Project

If you have cloned the repository and made changes within the `basic-calculator-program` directory, use these commands from the **root** `Python-PowerLearnProject` folder to commit and push your changes.

```bash
# Stage your new or modified files
git add basic-calculator-program/basic-calculator-program.py basic-calculator-program/README.md

# Commit the changes with a descriptive message
git commit -m "feat: Add basic calculator program and README"

# Push the changes to the main branch on GitHub
git push origin main
```

---

## Troubleshooting

- Ensure you are in the correct root directory (`Python-PowerLearnProject`) before running `git` commands.
- If you have trouble pushing, run `git pull` first to integrate any changes from the remote repository before pushing again.
- Verify the remote URL is correct:

```bash
# Verify remote is set correctly from the project root
git remote -v

# It should show:
# origin  https://github.com/damilareadekeye/Python-PowerLearnProject.git (fetch)
# origin  https://github.com/damilareadekeye/Python-PowerLearnProject.git (push)
```

---

## Author

**Damilare Lekan Adekeye**  
Email: damilare@damilareadekeye.com  
Portfolio: https://damilareadekeye.com
