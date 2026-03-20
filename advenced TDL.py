import json
import time
from check_date import validate_date
from check_date import validate_end_date

def print_task(task, i):
    done = "✔️" if task["done"] == True else " "
    print(f"{i}. [{done}] {task['title']} | {task['priority'].upper()}")
    print(f"   🗓️ {task['start_date']} -> {task['end_date']}")
    print(f"   📝 {task['description']}")
    print("-" * 30)

def save_tasks(Tasks):
    with open(r"C:\Users\pc\Desktop\TDL.json", "w") as f:
        json.dump(Tasks, f)
    with open(r"C:\Users\pc\Desktop\To_do_list.txt", "w", encoding="utf-8") as file:
        file.write("To do list:\n")
        for i, task in enumerate(Tasks, 1):
            file.write("-" * 30 + "\n")
            file.write(f"{i}. {task['title']} | {task['priority'].upper()}\n")
            file.write(f"   🗓️ {task['start_date']} -> {task['end_date']}\n")
            file.write(f"   📝 {task['description']}\n")
            file.write("-" * 30 + "\n")

try:
    with open(r"C:\Users\pc\Desktop\TDL.json", "r") as f:
        Tasks = json.load(f)
                
except FileNotFoundError:
    Tasks = []

repeat = "y"

while repeat == "y":

    print("-" * 30)
    print("1. Add Task")
    print("2. Edit Task")
    print("3. Delete Task")
    print("4. Show Tasks")
    print("5. Quick Task")
    print("6. Exit")
    print("-" * 30)

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice < 1 or choice > 6:
                print("Invalid choice. Please enter a number between 1 and 6.")
                continue
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    

    if choice == 1:

        title = input("Enter task: ")

        description = input("Enter description for this task: ")

        while True:
            start_date = input("Enter start date for this task: ")
            if not validate_date(start_date):
                print("Invalid date format. Please use YYYY-MM-DD format.")
            else:
                break
        
        while True:
            end_date = input("Enter end date for this task: ")
            if not validate_date(end_date):
                print("Invalid date format. Please use YYYY-MM-DD format.")
            elif not validate_end_date(start_date, end_date):
                print("End date must be after start date.")
            else:
                break
        while True:
            priority = input("Enter priority for this task(low, medium, high): ")
            if priority in ["low", "medium", "high"]:
                break
            print("Invalid priority. Please enter low, medium, or high.")

        Tasks.append({
            "title": title,
            "description": description,
            "start_date": start_date,
            "end_date": end_date,
            "priority": priority,
            "done": False
        })

        print("Task added successfully!")

    elif choice == 2:

        if not Tasks:
            print("No tasks found!")

        else:
            for i, task in enumerate(Tasks, 1):
                print(f"{i}. {task['title']}")

            while True:
                try:
                    num = int(input("Enter task number to change (negative or null to stop): "))
                except ValueError:
                    print("Please enter a valid number!")
                    continue
                if num <= 0:
                    break
                if 1 <= num <= len(Tasks):

                    print("Which field do you want to edit?")
                    print("1. Title")
                    print("2. Description")
                    print("3. Start Date")
                    print("4. End Date")
                    print("5. Priority")
                    print("6. Done")
                    print("7. Exit")
                    
                    while True:
                        try:
                            field_choice = int(input("Enter field number to edit: "))
                            if 1 <= field_choice <= 7:
                                break
                            else:
                                print("Please enter a valid field number!")
                        except ValueError:
                            print("Please enter a valid number!")

                    if field_choice == 1:
                        new_title = input("Enter new title for this task: ")
                        Tasks[num - 1]["title"] = new_title
                        print("Task changed successfully!")
                    elif field_choice == 2:
                        new_description = input("Enter new description for this task: ")
                        Tasks[num - 1]["description"] = new_description
                        print("Task changed successfully!")
                    elif field_choice == 3:
                        while True:
                            new_s_date = input("Enter new start date (DD-MM-YYYY): ")
                            if validate_date(new_s_date):
                                Tasks[num-1]["start_date"] = new_s_date
                                print("Task changed successfully!")
                                break
                            print("Invalid date!")
                    elif field_choice == 4:
                        while True:
                            new_e_date = input("Enter new end date(DD-MM-YYYY): ")
                            if not validate_date(new_e_date):
                                print("Invalid date!")
                            elif not validate_end_date(Tasks[num-1]["start_date"], new_e_date):
                                print("End date must be after start date.")
                            else:
                                Tasks[num-1]["end_date"] = new_e_date
                                print("Task changed successfully!")
                                break
                    
                    elif field_choice == 5:
                        while True:
                            new_priority = input("Enter new priority for this task(low, medium, high): ")
                            if new_priority in ["low", "medium", "high"]:
                                break
                            print("Invalid priority. Please enter low, medium, or high.")
                        Tasks[num - 1]["priority"] = new_priority
                        print("Task changed successfully!")
                    elif field_choice == 6:
                        while True:
                            ndone = input("Enter new done status for this task(t/f): ")
                            if ndone == "t":
                                ndone = True
                                break
                            elif ndone == "f":
                                ndone = False
                                break
                            else:
                                print("Invalid input! Please enter t or f.")
                                continue
                        Tasks[num - 1]["done"] = ndone
                        print("Task changed successfully!")
                    
                    elif field_choice == 7:
                        break

    elif choice == 3:
        if not Tasks:
            print("No tasks found!")
        else:
            for i, task in enumerate(Tasks, 1):
                print(f"{i}. {task['title']}")
            while True:
                try:
                    num = int(input("Enter task number to delete (negative or null to stop): "))
                except ValueError:
                    print("Please enter a valid number!")
                    continue

                if num <= 0:
                    break
                if 1 <= num <= len(Tasks):
                    Tasks.pop(num - 1)
                    print("Task deleted successfully!")
                else:
                    print("Task not found!")
    elif choice == 4:
        if not Tasks:
            print("No tasks found!")
        else:
            for i, task in enumerate(Tasks, 1):
                print_task(task, i)
    
    elif choice == 5:
        # A timer used for quick tasks

        task_name = input("Enter task name: ")
        while True:
            try:
                minutes = int(input("Enter time in minutes: "))
                if minutes > 0:
                    break
                else:
                    print("Please enter a number greater than 0!")
            except ValueError:
                print("Please enter a valid number!")

        total_seconds = minutes * 60

        while total_seconds > 0:
            minutes = total_seconds // 60
            seconds = total_seconds % 60
            timer = f"{minutes:02d}:{seconds:02d}"
            print(f"\rremaining time for {task_name}: {timer}", end="")
            time.sleep(1)
            total_seconds -= 1

        print(f"\nTime's up for {task_name}!")

    elif choice == 6:
        ext = input("Do you want to save the tasks? (y/n): ")
        if ext == "y":
            save_tasks(Tasks)
            exit("Tasks saved successfully!")
        else:
            exit()

    repeat = input("Do you want to repeat? (y/n): ")
    if repeat == "n":
        break

save_tasks(Tasks)

print("~" * 30)
print("Tasks saved successfully!")
print("Thank you for using the to do list app!")
print("~" * 30)