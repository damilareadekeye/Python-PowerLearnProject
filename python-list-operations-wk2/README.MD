
# Python List Operations

This repository contains a Python script that demonstrates fundamental list manipulations. It initializes an empty list and progressively modifies it by adding, inserting, extending, removing, and sorting elements, finally printing the modified list and the index of a specific element.

This script is part of the `Python-PowerLearnProject`.

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

The script is located at `python-list-operations/list_operations.py`.

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

Navigate to the project directory and run the script with Python 3.

```bash
python python-list-operations/list_operations.py
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

## Clone The Project Repository

To get a local copy of the project, clone the `Python-PowerLearnProject` repository:

```bash
git clone https://github.com/damilareadekeye/Python-PowerLearnProject.git
cd Python-PowerLearnProject```

---

## Contributing to the Project

If you have cloned the repository and made changes within the `python-list-operations` directory, use these commands from the root `Python-PowerLearnProject` folder to commit and push your changes.

```bash
# Stage your new or modified files
git add python-list-operations/list_operations.py python-list-operations/README.md

# Commit the changes with a descriptive message
git commit -m "feat: Update list operations script and README"

# Push the changes to the main branch on GitHub
git push origin main
```

---

## Troubleshooting

- Ensure you are in the correct root directory (`Python-PowerLearnProject`) before running `git` commands.
- If you have trouble pushing, run `git pull` first to integrate any changes from the remote repository before pushing again.
- Verify the remote URL is correct:

```bash
# Verify remote is set correctly
git remote -v

# It should show:
# origin  https://github.com/damilareadekeye/Python-PowerLearnProject.git (fetch)
# origin  https://github.com/damilareadekeye/Python-PowerLearnProject.git (push)
```

---

## Author

**Damilare Lekan Adekeye**  
Portfolio: https://damilareadekeye.com
