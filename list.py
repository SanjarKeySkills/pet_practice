def find_maximum_in_list(numbers):
    """
    Finds the maximum value in a given list of numbers.
    Args: numbers: A list of numerical values.
    Returns: The maximum value found in the list, or None if the list is empty. comparing to the first element
    """
    if not numbers:  # Check if the list is empty
        return None
    max_value = numbers[0]  # Initialize max_value with the first element
    # print(max_value)
    for number in numbers:
        if number > max_value:
            max_value = number  # Update max_value if a larger number is found
            print(number)
    return max_value

# Example usage:
# my_list = [3, 1, 4, 1, 5, 9, 2, 6]
my_list = [12, 3, 4, 5, 6, 7, 8, 9, 13]
maximum = find_maximum_in_list(my_list)
print(f"The maximum value in the list {my_list} is: {maximum}")

empty_list = []
maximum_empty = find_maximum_in_list(empty_list)
# print(f"The maximum value in an empty list is: {maximum_empty}"

# -----------------------------------------

def find_minimum_in_list(numbers):
    if not numbers:
        return None
    min_value = numbers[0]
    
    for number in numbers:
        if number < min_valuen
    
    
    
    
# my_list = [3, 1, 4, 1, 5, 9, 2, 6]