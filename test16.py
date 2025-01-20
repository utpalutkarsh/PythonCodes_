import time
from datetime import datetime, timedelta

def execute_task():
    print("Task executed at:", datetime.now())

# Define the target time
target_time = "14:30:00"  # Use the 24-hour format
while True:
    current_time = datetime.now()

    # Calculate target time for the next occurrence
    today_target = datetime.strptime(target_time, "%H:%M:%S").replace(
        year=current_time.year, month=current_time.month, day=current_time.day
    )
    if current_time > today_target:
        today_target += timedelta(days=1)  # Move to the next day

    time_difference = (today_target - current_time).total_seconds()
    print(f"Waiting for the next execution at {today_target}...")
    time.sleep(time_difference)

    execute_task()
