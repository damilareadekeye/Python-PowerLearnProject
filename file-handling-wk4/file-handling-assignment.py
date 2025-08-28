# File Handling and Exception Handling Assignment

def read_and_modify_file(filename):
    """
    Reads a file, modifies its content (converts to uppercase),
    and writes the modified content to a new file.
    It also handles exceptions if the file cannot be read.
    """
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("Original content:")
            print(content)

        modified_content = content.upper()

        with open('modified.txt', 'w') as file:
            file.write(modified_content)
            print("\nModified content (in uppercase) written to modified.txt")

    except FileNotFoundError:
        print(f"\nError: The file '{filename}' was not found.")
    except IOError as e:
        print(f"\nError reading or writing file: {e}")

# Main part of the script
if __name__ == "__main__":
    # Error Handling Lab: Ask the user for a filename
    filename_to_read = input("Enter the name of the file to read (e.g., original.txt): ")

    # File Read & Write Challenge: Read, modify, and write file
    read_and_modify_file(filename_to_read)
