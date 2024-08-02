def add_quest(quest_items):
    item = input("What would you like to add to your quest? ")
    quest_items.append(item)
    print(f"Added {item} to your quest")

def view_quest(quest_items):
    if not quest_items:
        print("You have no quests")
    else:
        print("Your quests:")
        for i, item in enumerate(quest_items, start=1):
            print(f"{i}. {item}")

def remove_quest(quest_items):
    if not quest_items:
        print("You have no quests to remove")
    else:
        view_quest(quest_items)
        index = int(input("Which quest would you like to remove? ")) - 1
        if 0 <= index < len(quest_items):
            removed_item = quest_items.pop(index)
            print(f"Removed {removed_item} from your quest")
        else:
            print("Invalid index")        

def main():
    quest_items = []
    flag = True
    while flag:
        ans = input('''
Menu Options
a - Add quest
b - View quests                               
c - Remove quest
d - Quit               
''')

        if ans == 'a':
            add_quest(quest_items)  # Adding a quest
        elif ans == 'b':
            view_quest(quest_items)  # Viewing a quest
        elif ans == 'c':
            remove_quest(quest_items)  # Removing a quest
        elif ans == 'd':
            flag = False  # Quitting the program
        else:
            print("Invalid option, please choose again.")

if __name__ == '__main__':
    main()
