def remove_duplicates(input_list):

    unique_set = set(input_list)

    return list(unique_set)


input_list = [1, 2, 2, 3, 4, 4, 5, 5, 1, 6]
unique_list = remove_duplicates(input_list)

print(f"Before: {input_list}")
print(f"After: {unique_list}")

