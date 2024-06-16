import re
from datetime import datetime

def process_log_file(file_pointer, task_id):
    # Regular expressions to match start and end lines
    start_pattern = re.compile(r'\[(.*?)\] start: ' + re.escape(task_id))
    end_pattern = re.compile(r'\[(.*?)\] end: ' + re.escape(task_id))

    # Initialize variables to store start and end times
    start_time = None
    end_time = None

    # Read the log file line by line
    for line in file_pointer:
        #start_match = start_pattern.search(line)
        #if start_match:
        if start_match := start_pattern.search(line):
            #start_time = datetime.strptime(start_match.group(1), "%Y-%m-%d %H:%M:%S")
            start_time = datetime.strptime(start_match[1], "%Y-%m-%d %H:%M:%S")
        
        #end_match = end_pattern.search(line)
        #if end_match:
        if end_match := end_pattern.search(line):
            #end_time = datetime.strptime(end_match.group(1), "%Y-%m-%d %H:%M:%S")
            end_time = datetime.strptime(end_match[1], "%Y-%m-%d %H:%M:%S")

    if start_time and end_time:
        print(f"Task: {task_id}")
        print(f"Start Time: {start_time}")
        print(f"End Time: {end_time}")
    else:
        print(f"Task {task_id} is incomplete or not found.")

# Create a sample log file
with open('log_file.log', 'w') as log_file:
    log_file.write("""[2024-06-10 08:00:00] start: task 1
[2024-06-10 08:01:00] start: task 2
[2024-06-10 08:10:00] end: task 1
[2024-06-10 08:15:00] end: task 2
""")

# Define the task ID you're interested in
task_id = "task 1"

# Open the log file
with open('log_file.log', 'r') as log_file:
    # Call the method with the file pointer and the task ID
    process_log_file(log_file, task_id)
