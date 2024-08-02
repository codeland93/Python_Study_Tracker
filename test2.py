import json

def check_progress(progress):
    python_progress = {
        'Week 1': 1,
        'Week 2': 2,
        'Week 3': 3,
        'Week 4': 4,
        'Week 5': 5,
        'Week 6': 6,
    }

    week_names = list(python_progress.keys())
    current_week = week_names[progress - 1]
    python_left = 6 - progress

    if progress == 6:
        print("Congratulations! You have completed all the Python lesson weeks.")
    elif progress < python_progress[current_week]:
        print(f"You have completed {progress} Python lesson weeks. You have {python_left} lessons left to study.")
    else:
        print(f"You have completed {progress} Python lesson. You need to study for the next week.")

def percentage_progress(progress):
    python_total = 6
    python_percentage = (progress / python_total) * 100
    return python_percentage

def save_progress(progress, filename='study_progress.json'):
    with open(filename, 'w') as file:
        json.dump(progress, file)

def load_progress(filename='study_progress.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return 0

def main():
    progress = load_progress()
    print("Welcome to the Study Progress Tracker!")

    while True:
        print('''
Menu Options
1 - Add/Update progress
2 - View progress percentage
3 - View remaining lessons
4 - Quit
''')

        choice = input("Choose an option: ")

        if choice == '1':
            user_input = input("Enter your progress (Week number): ")
            try:
                progress = int(user_input)
                if 1 <= progress <= 6:
                    check_progress(progress)
                else:
                    print("Please enter a valid week number (1-6).")
            except ValueError:
                print("Invalid input. Please enter a week number.")
        
        elif choice == '2':
            print(f"Your current Python progress percentage is {percentage_progress(progress)}%")
        
        elif choice == '3':
            python_left = 6 - progress
            print(f"You have {python_left} lessons left to study.")
        
        elif choice == '4':
            save_progress(progress)
            print("Progress saved. Goodbye!")
            break
        
        else:
            print("Invalid option. Please choose again.")

if __name__ == '__main__':
    main()


  

