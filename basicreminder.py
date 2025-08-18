import time
from datetime import datetime

def set_reminder():
    reminder_time = input("Enter reminder time (HH:MM 24-hour format): ")
    message = input("Enter your reminder message: ")

    while True:
        now = datetime.now().strftime("%H:%M")
        if now == reminder_time:
            print("\n⏰ Reminder!")
            print("Message:", message)
            break
        time.sleep(30)  # check every 30 seconds

if __name__ == "__main__":
    print("🔔 Simple Python Reminder App 🔔")
    set_reminder()
