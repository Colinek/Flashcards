import os
import random
import time

def select_file():
  # Get the path to the folder containing the question files
  folder_path = os.path.join(os.getcwd(), "questions")

  # Get a list of the available question files in the folder
  files = os.listdir(folder_path)
  question_files = [f for f in files if f.endswith('.csv')]

  # Display the list of available question files
  print("Available question files:\n")
  for i, filename in enumerate(question_files):
    print(f"{i+1}. {filename}")
  # Prompt the user to choose a file
  while True:
    try:
      choice = int(input("\nEnter the number of the file you want to use: "))
      filename = question_files[choice-1]
      break
    except (ValueError, IndexError):
        print("Invalid choice. Please try again.")

  # Get the full path to the selected file
  file_path = os.path.join(folder_path, filename)

  return file_path

# Function to load questions from a file
def load_questions(filename):
    questions = {}
    with open(filename, "r") as f:
        for line in f:
            question, answer = line.strip().split(",")
            questions[question] = answer
    return questions

# Function to display the menu and get the user's choice
def get_menu_choice():
    os.system('clear')
    print("Menu:")
    print("1. Study flashcards")
    print("2. Add flashcards")
    print("3. Quit")
    choice = input("Enter your choice: ")
    while choice not in ["1", "2", "3"]:
      choice = input("Invalid choice. Enter your choice (1-3): ")
    return choice

# Function to ask the user for a new flashcard and add it to the dictionary
def add_flashcard(flashcards):
  question = input("Enter the question: ")
  answer = input("Enter the answer: ")
  flashcards[question] = answer
  print("Flashcard added.")

# Initialize the Leitner system
boxes = [[], [], [], []]

def menu():
  os.system('clear')
  print("=================================================")
  print("=                                               =")
  print("=        F l a s h c a r d   T e s t e r        =")
  print("=                                               =")
  print("=================================================")
  print()
  # Ask the user if they want to load questions from a file
  load_from_file = input("Do you want to load questions from a file? (y/n) ")
  if load_from_file.lower() == "y":
    os.system('clear')
    filename = select_file()
    flashcards = load_questions(filename)
  else:
    os.system('clear')
    print("Goodbye!")
    quit()
  

  # Loop through the menu
  while True:
      choice = get_menu_choice()

      if choice == "1":
          title = os.path.basename(filename)
          os.system('clear')
          title = title.strip(".csv")
          print("="*len(title))
          print(title)
          print("="*len(title))
          print()
          # Study flashcards
          # Shuffle the order of the flashcards in the current box
          current_box = boxes[0]
          if not current_box:
              current_box = list(flashcards.items())
              random.shuffle(current_box)
          random.shuffle(current_box)

          # Loop through the flashcards in the current box
          for question, answer in current_box:
              # Ask the user the question
              user_answer = input(question + " ")

              # Check if the user's answer is correct
              if user_answer.lower() == answer.lower():
                  print("Correct!")
                  # Move the flashcard to the next box
                  if current_box == list(flashcards.items()):
                      boxes[1].append((question, answer))
                  elif current_box == boxes[1]:
                      boxes[2].append((question, answer))
                  elif current_box == boxes[2]:
                      boxes[3].append((question, answer))
              else:
                  print("Incorrect. The correct answer is:", answer)
                  # Move the flashcard to the first box
                  boxes[0].append((question, answer))

          # Check if all boxes are empty
          if not any(boxes):
              print("Congratulations, you have completed all the flashcards!")
              time.sleep(2)
                 
      elif choice == "2":
          # Add flashcards
          add_flashcard(flashcards)

      elif choice == "3":
          # Quit
          menu()

menu()
