variable = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bounded = input("Is it time-bound? (yes/no): ")

match priority :
    case "high":
        if time_bounded == "yes":
            print("Reminder: ", variable," is a ", priority," task that requires immediate attention today!")
    case "medium":
        if time_bounded == "yes":
            print("Reminder: ", variable," is a ", priority," task that requires immediate attention today!")
    case "medium":
        if time_bounded == "yes":
            print("Reminder: ", variable," is a ", priority," task that requires immediate attention today!")
    case "low":
        if time_bounded == "no":
            print("Note : ", variable," is a ", priority," task. Consider completing it when you have free time.")