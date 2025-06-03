# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task for today: ")
priority = input("Enter the priority level (high/medium/low): ").lower()
time_bound = input("Is the task time-bound? (yes/no): ").lower()

# Process the task using match-case based on priority
match priority:
    case "high":
        reminder = f"🔴 HIGH PRIORITY: Don't forget to '{task}'."
    case "medium":
        reminder = f"🟠 Medium priority task: You should work on '{task}' today."
    case "low":
        reminder = f"🟢 Low priority task: Consider doing '{task}' if you have time."
    case _:
        reminder = f"⚪ Task: '{task}' (Unspecified priority)."

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " This is a time-sensitive task that requires immediate attention today!"

# Display the final reminder
print("\nYour Reminder:")
print(reminder)
