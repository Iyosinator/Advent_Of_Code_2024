def read_input_file(file_path):
    with open(file_path, 'r') as file:
        input_list = file.read().splitlines()
    comparison_list = [item.split("   ") for item in input_list]
    left_list = []
    right_list = []
    for pair in comparison_list:
        left_list.append(int(pair[0]))
        right_list.append(int(pair[1]))

    return left_list, right_list

def calculate_similarity_score(left_list, right_list):
    occurrence_count_dict = {}
    similarity_score = 0

    for num in left_list:
        if num not in occurrence_count_dict:
            occurrence_count_dict[num] = right_list.count(num)  
        similarity_score += num * occurrence_count_dict[num]  
    return similarity_score


input_file = 'input.txt'
left_list, right_list = read_input_file(input_file)
result = calculate_similarity_score(left_list, right_list)
print("Total similarity score:", result)

