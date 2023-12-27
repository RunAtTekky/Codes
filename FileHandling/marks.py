import statistics

def read_marks(file_path):
    with open(file_path, 'r') as file:
        marks = [float(line.strip()) for line in file]
    return marks

def calculate_statistics(marks):
    mean = statistics.mean(marks)
    median = statistics.median(marks)
    mode = statistics.mode(marks)
    return mean, median, mode

def write_statistics(file_path, mean, median, mode):
    with open(file_path, 'w') as file:
        file.write(f"Mean: {mean}\n")
        file.write(f"Median: {median}\n")
        file.write(f"Mode: {mode}\n")

input_file_path = 'input_marks.txt'
output_file_path = 'output_statistics.txt'

# Read marks from the input file
marks = read_marks(input_file_path)

# Calculate mean, median, and mode
mean, median, mode = calculate_statistics(marks)

# Write statistics to the output file
write_statistics(output_file_path, mean, median, mode)

print("Statistics written to", output_file_path)

