import re

# Define the paths for the input log file and the output filtered log file
input_log_file_path = r'C:\Users\surya\OneDrive\Documents\github\GeneralCoding\python\results.log'
output_log_file_path = r'C:\Users\surya\OneDrive\Documents\github\GeneralCoding\python\filtered_logfile.log'

# Define the regex pattern to search for and the replacement word
pattern = r'\baddress\b'  # Example pattern: match the word 'ERROR'
replacement = 'Address'  # Word to replace 'ERROR' with

# Compile the regex pattern for efficiency
regex = re.compile(pattern)

# Open the input log file in read mode and the output log file in write mode
with open(input_log_file_path, 'r') as log_file, open(output_log_file_path, 'w') as output_file:
    # Iterate over each line in the input log file
    for line in log_file:
        # Check if the line matches the regex pattern
        if regex.search(line):
            # Replace the matching keyword with the replacement word
            modified_line = regex.sub(replacement, line)
            # Write the modified line to the output file
            output_file.write(modified_line)

print(f"Lines containing the pattern '{pattern}' have been modified and written to {output_log_file_path}")

# To replace the keyword in the same file that is read
replacement2 = 'Address'
# Read the contents of the file
with open(output_log_file_path, 'r') as file:
    file_contents = file.read()

# Perform the replacement on the contents
modified_contents = regex.sub(replacement2, file_contents)

# Write the modified contents back to the same file
with open(output_log_file_path, 'w') as file:
    file.write(modified_contents)

print(f"Occurrences of '{pattern}' have been replaced with '{replacement2}' in {output_log_file_path}")

# instead of reading the entire file into memory buffer read line by line
import os
temp_file_path = f'{output_log_file_path}.tmp'
# Open the original file for reading and a temporary file for writing
with open(output_log_file_path, 'r') as original_file, open(temp_file_path, 'w') as temp_file:
    # Iterate over each line in the original file
    for line in original_file:
        # Replace the matching keyword with the replacement word
        modified_line = regex.sub(replacement, line)
        # Write the modified line to the temporary file
        temp_file.write(modified_line)

# Replace the original file with the temporary file
os.replace(temp_file_path, output_log_file_path)