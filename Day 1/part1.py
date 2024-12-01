# Function to calculate total distance
def calculate_total_distance(left_list, right_list):
    # Sort both lists
    left_list.sort()
    right_list.sort()
    
    # Sum absolute differences
    total_distance = sum(abs(left - right) for left, right in zip(left_list, right_list))
    
    return total_distance

# Read puzzle input
left_list = []
right_list = []

# Parse the input (assuming the input is stored in a text file 'input.txt')
with open('input.txt', 'r') as file:
    for line in file:
        left, right = map(int, line.split())  # Split and convert to integers
        left_list.append(left)
        right_list.append(right)

# Calculate total distance
result = calculate_total_distance(left_list, right_list)
print("Total distance:", result)
