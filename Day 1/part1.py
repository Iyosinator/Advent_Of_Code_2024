def calculate_total_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()
    total_distance = sum(abs(left - right) for left, right in zip(left_list, right_list))
    return total_distance
left_list = []
right_list = []
with open('input.txt', 'r') as file:
    for line in file:
        left, right = map(int, line.split())  
        left_list.append(left)
        right_list.append(right)
result = calculate_total_distance(left_list, right_list)
print("Total distance:", result)
