# Assuming 'input.txt' is correctly formatted and exists in the current directory
def read_input_file(file_path):
    # Read input from the file
    with open(file_path, 'r') as file:
        # Split the input into lines and then split each line by spaces
        input_list = file.read().splitlines()

    # Create a comparison list with split values
    comparison_list = [item.split("   ") for item in input_list]

    # Initialize left and right lists
    left_list = []
    right_list = []

    # Populate the left and right lists from the comparison pairs
    for pair in comparison_list:
        left_list.append(int(pair[0]))
        right_list.append(int(pair[1]))

    return left_list, right_list

def calculate_similarity_score(left_list, right_list):
    # Create a dictionary to count occurrences of numbers in the right list
    occurrence_count_dict = {}
    similarity_score = 0

    for num in left_list:
        if num not in occurrence_count_dict:
            occurrence_count_dict[num] = right_list.count(num)  # Count occurrences in right_list
        similarity_score += num * occurrence_count_dict[num]  # Add to similarity score

    return similarity_score

# File path to the input file
input_file = 'input.txt'

# Read the input data
left_list, right_list = read_input_file(input_file)

# Calculate the total similarity score
result = calculate_similarity_score(left_list, right_list)

# Print the result
print("Total similarity score:", result)

