import re
import random
import sys

def generate_random_array(size):
    if size <= 0:
        print("Invalid size")
        return None
    
    # Generate random values for the array
    arr = [random.randint(0, 100000) for _ in range(size)]

    # Return the unsorted array
    return arr


def get_file_extension(filename):
    # Split the file name into a list containing the name and extension
    split_filename = filename.split('.')
    
    # If the file has no extension, return an empty string
    if len(split_filename) == 1:
        return ''
    
    # Otherwise, return the last element of the list (the extension)
    return split_filename[-1]


new_array = generate_random_array(int(sys.argv[1]))
# Iterate over the input files
for input_file in sys.argv[2:]:

    with open(input_file, 'r') as f:
        data = f.read()

    new_array_str = ','.join(str(x) for x in new_array)

    if get_file_extension(input_file)=="c":
        data = re.sub(r'#define elems .*', f'#define elems {new_array_str}', data)
    elif get_file_extension(input_file)=="py":
        data = re.sub(r'array =.*', f'array = [{new_array_str}]', data)
    # Write the updated file
    with open(input_file, 'w') as f:
        f.write(data)