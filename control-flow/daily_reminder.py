# daily_reminder.py

# Loop to ensure proper user input
while True:
    task = input("Enter your task for today: ")
    priority = input("Enter the priority level (high/medium/low): ").lower()
    time_bound = input("Is the task time-bound? (yes/no): ").lower()

    # Validate priority input
    if priority not in ("high", "medium", "low"):
        print("Please enter a valid priority level: high, medium, or low.\n")
        continue

    # Validate time_bound input
    if time_bound not in ("yes", "no"):
        print("Please answer 'yes' or 'no' for whether the task is time-bound.\n")
        continue

    break  # Exit loop if inputs are valid

# Base reminder message using match-case
match priority:
    case "high":
        reminder = f"🔴 HIGH PRIORITY: Don't forget to '{task}'."
    case "medium":
        reminder = f"🟠 MEDIUM PRIORITY: Try to complete '{task}' today."
    case "low":
        reminder = f"🟢 LOW PRIORITY: You might work on '{task}' if there's time."
    case _:
        reminder = f"⚪ Task: '{task}'."

# Append message if task is time-bound
if time_bound == "yes":
    reminder += " This is a time-sensitive task that requires immediate attention today!"

# Display the final reminder
print("\nYour Reminder:")
print(reminder)
