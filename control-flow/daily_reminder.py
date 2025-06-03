#!/usr/bin/env python3

def daily_reminder():
    print("🌟 Daily Priority Task Reminder 🌟")
    print("---------------------------------")

    # Loop until valid task input is provided
    while True:
        task = input("Enter your SINGLE priority task for today: ").strip()
        if task:
            break
        print("⚠️  Task cannot be empty. Try again.")

    # Loop until valid priority input is provided
    while True:
        priority = input("Enter task priority (high/medium/low): ").strip().lower()
        if priority in ('high', 'medium', 'low'):
            break
        print("⚠️  Invalid priority. Please enter 'high', 'medium', or 'low'.")

    # Loop until valid time-bound input is provided
    while True:
        time_bound = input("Is this task time-sensitive? (yes/no): ").strip().lower()
        if time_bound in ('yes', 'no'):
            break
        print("⚠️  Please answer 'yes' or 'no'.")

    # Generate reminder using match-case and conditionals
    print("\n🔔 Your Customized Reminder:")
    print(f"Task: {task}")
    
    match priority:
        case 'high':
            urgency = "❗Top priority"
        case 'medium':
            urgency = "⏳ Medium priority"
        case 'low':
            urgency = "💤 Low priority"
    
    time_sensitive_part = " that requires immediate attention today!" if time_bound == 'yes' else " (flexible timing)."
    
    print(f"Status: {urgency}{time_sensitive_part}")

    # Additional encouragement based on priority
    if priority == 'high' and time_bound == 'yes':
        print("\n🚨 Warning! This is critical and time-sensitive! Handle this first!")
    elif priority == 'low' and time_bound == 'no':
        print("\n☕ You can schedule this at your convenience.")
    else:
        print("\n📌 Make sure to address this today.")

if __name__ == "__main__":
    daily_reminder()
