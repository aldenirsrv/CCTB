# from functools import reduce
import shutil
import os

filename = "student_scores.txt"

def save_avg_data(lines):
    # Define the name of the file
    avg_file_name = "avg_score.txt"
    # remove the file is exists
    if os.path.exists(avg_file_name):
        os.remove(avg_file_name)
    
    # create always a new file
    with open(avg_file_name, 'a') as file:
        file.writelines(lines)

def file_calculation(file_path):
    with open(file_path, 'r') as file:
         # Skip the header line
        header = file.readline()
        agv_data = []
        for line in file:
            # Split by whitespace 
            parts = line.split()  # Split by whitespace (can be space or tab)
            
            # Get the first element of the array (the name)
            name = parts[0]

            # convert object to array and cast each element to int
            scores = list(map(int, parts[1:]))

            # Calculate the average of the scores
            average_score = sum(scores) / len(scores)
            
            # Append every agerage in a array
            agv_data.append(f'{name}: {average_score:.2f}\n')
    
    # Call function to generate file
    save_avg_data(agv_data)

def file_operations():
    if os.path.exists(filename):
        # Create a temp file to avoid mistakes on the main file
        temp_file = shutil.copyfile(filename, "temp_file.txt")
        # Calculate the avg
        file_calculation(temp_file)
        # remove the temporary file
        os.remove(temp_file)
    else:
        print("File don't exists")

file_operations()