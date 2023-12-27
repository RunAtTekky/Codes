def read_names(file_path):
    with open(file_path, 'r') as file:
        names = [line.strip() for line in file]
    return names

def write_sorted_names(file_path, sorted_names):
    with open(file_path, 'w') as file:
        for name in sorted_names:
            file.write(name + '\n')

input_file_path = 'input_names.txt'
output_file_path = 'output_sorted_names.txt'

# Read names from the input file
names = read_names(input_file_path)

# Sort names alphabetically
sorted_names = sorted(names)

# Write sorted names to the output file
write_sorted_names(output_file_path, sorted_names)

print("Sorted names written to", output_file_path)

