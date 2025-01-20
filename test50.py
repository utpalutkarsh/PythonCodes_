import schedule
import time

# Define the task to be executed
def job():
    print("\033[1mHappy Birthday, Motu!\033[0m")

# Schedule the task to run at a specific time (e.g., every day at 14:30)
schedule.every().day.at("01:11").do(job)

# Keep the script running to check the scheduled time
while True:
    schedule.run_pending()
    time.sleep(1)
