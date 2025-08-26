```markdown
# Python List Operations

This repository contains a Python script that demonstrates fundamental list manipulations. 
It initializes an empty list and progressively modifies it by adding, inserting, extending, removing, and sorting elements, finally printing the modified list and the index of a specific element.

---

## Features

- **Initialization**: Creates an empty list.
- **Appending**: Adds elements to the end of the list.
- **Inserting**: Inserts an element at a specific index.
- **Extending**: Appends all items from another list.
- **Popping**: Removes the last element from the list.
- **Sorting**: Sorts the list in ascending order.
- **Indexing**: Finds the index of a specific value.

---

## Program Code

Save the file as `list_operations.py`.

```python
# Week Two Assignment

# Step 1: Create an empty list
my_list = []

# Step 2: Append elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Step 3: Insert 15 at the second position (index 1)
my_list.insert(1, 15)

# Step 4: Extend my_list with
my_list.extend()

# Step 5: Remove the last element
my_list.pop()

# Step 6: Sort my_list in ascending order
my_list.sort()

# Step 7: Find and print the index of value 30
index_of_30 = my_list.index(30)
print("Final list:", my_list)
print("Index of 30:", index_of_30)
```

---

## Usage

Run the program with Python 3.

```bash
python list_operations.py
```

---

## Example Output
```
Final list:
Index of 30: 3
```
---

## Requirements

- Python 3.x

---

## Clone This Repository

To clone this repository to your local machine:

```bash
git clone https://github.com/damilareadekeye/python-list-operations.git
cd python-list-operations```

## OR 

## Create the GitHub Repository on the Website

1. Open https://github.com/new  
2. Repository name: `python-list-operations`  
3. Visibility: Public  
4. Do not initialize with a README (you already have local files)  
5. Click **Create repository**

---

## Push Your Local Project to GitHub

Execute these commands inside your project folder.

```bash
# Initialize git if you have not done so already
git init

# Add files and commit
git add list_operations.py README.md
git commit -m "Add python list operations script and README"

# Ensure your branch is named main
git branch -M main

# Add the correct remote
git remote add origin https://github.com/damilareadekeye/python-list-operations.git

# Push to GitHub
git push -u origin main
```

---

## Alternative: Create the Remote Repository Without Opening a Browser

### Option A - GitHub CLI

Prerequisites: Install GitHub CLI and authenticate once.

```bash
# Install GitHub CLI if needed: https://cli.github.com/
# Authenticate once
gh auth login

# Create the repo from the current directory and push in one step
gh repo create python-list-operations --public --source=. --push
```

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

```bash
# Remove the incorrect remote
git remote remove origin

# Add the correct remote
git remote add origin https://github.com/damilareadekeye/python-list-operations.git

# Verify
git remote -v

# Push again
git push -u origin main
```

- Confirm that the repository actually exists on GitHub at  
  `https://github.com/damilareadekeye/python-list-operations`

---

## Author

**Damilare Lekan Adekeye**  
Portfolio: https://damilareadekeye.com
```