import os

def select_file():
    # Get the path to the folder containing the question files
    folder_path = os.path.join(os.getcwd(), "questions")

    # Get a list of the available question files in the folder
    files = os.listdir(folder_path)
    question_files = [f for f in files if f.endswith('.csv')]

    # Display the list of available question files
    print("Available question files:")
    for i, filename in enumerate(question_files):
        print(f"{i+1}. {filename}")

    # Prompt the user to choose a file
    while True:
        try:
            choice = int(input("Enter the number of the file you want to use: "))
            filename = question_files[choice-1]
            break
        except (ValueError, IndexError):
            print("Invalid choice. Please try again.")

    # Get the full path to the selected file
    file_path = os.path.join(folder_path, filename)

    return file_path

x = select_file()
print(x)
