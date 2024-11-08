import os

def new_file():
    return ""

def open_file():
    filename = input("Enter the filename to open: ")
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.read()
        print(f"File '{filename}' opened successfully.")
        return content
    else:
        print(f"File '{filename}' not found.")
        return ""

def save_file(content):
    filename = input("Enter the filename to save: ")
    with open(filename, 'w') as file:
        file.write(content)
    print(f"File saved as '{filename}'.")

def help_menu():
    """Display the help menu"""
    print("\n--- HELP MENU ---")
    print("1. NEW: Create a new text.")
    print("2. OPEN: Open an existing file.")
    print("3. SAVE: Save the current text to a file.")
    print("4. INSERT: Insert text (word/sentence) or character.")
    print("5. DELETE: Delete text (word/sentence) or character.")
    print("6. QUIT: Exit the editor.")
    print("------------------\n")

def insert_text(content):
    insert_type = input("Insert (word/sentence/character): ").lower()
    if insert_type == "word" or insert_type == "sentence":
        position = int(input("Enter the position to insert at: "))
        text_to_insert = input(f"Enter the {insert_type} to insert: ")
        content = content[:position] + text_to_insert + content[position:]
    elif insert_type == "character":
        position = int(input("Enter the position to insert the character: "))
        char_to_insert = input("Enter the character to insert: ")
        content = content[:position] + char_to_insert + content[position:]
    else:
        print("Invalid insert type.")
    return content

def delete_text(content):
    delete_type = input("Delete (word/sentence/character): ").lower()
    if delete_type == "word" or delete_type == "sentence":
        start_pos = int(input(f"Enter the start position of the {delete_type} to delete: "))
        end_pos = int(input(f"Enter the end position of the {delete_type} to delete: "))
        content = content[:start_pos] + content[end_pos:]
    elif delete_type == "character":
        position = int(input("Enter the position of the character to delete: "))
        content = content[:position] + content[position+1:]
    else:
        print("Invalid delete type.")
    return content

def main():
    content = ""
    while True:
        print("\nOptions: NEW, OPEN, SAVE, INSERT, DELETE, HELP, QUIT")
        choice = input("Enter your choice: ").lower()
        
        if choice == "new":
            content = new_file()
            print("New text file created.")
        elif choice == "open":
            content = open_file()
            print("Current content:\n", content)
        elif choice == "save":
            save_file(content)
        elif choice == "insert":
            content = insert_text(content)
            print("Updated content:\n", content)
        elif choice == "delete":
            content = delete_text(content)
            print("Updated content:\n", content)
        elif choice == "help":
            help_menu()
        elif choice == "quit":
            print("Exiting the text editor.")
            break
        else:
            print("Invalid choice. Type 'HELP' to see available commands.")


main()
