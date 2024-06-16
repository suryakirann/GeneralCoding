##
#Use case:1
#  Open a new python file and write lines that match a particular criteria
#  from a give log file

# path to log location
input_log_file_path = r'C:\Users\surya\OneDrive\Documents\github\GeneralCoding\python\results.log'
output_log_file_path = r'C:\Users\surya\OneDrive\Documents\github\GeneralCoding\python\parsed.log'
keyword = 'wr_xtnh'

with open(input_log_file_path, 'r') as log_file, open(output_log_file_path, 'w') as parsed_file:
    for line in log_file:
        if keyword in line:
            parsed_file.write(line)

print(f"Lines containing the keyword '{keyword}' have been written to {output_log_file_path}")
            
        
        
        
    
