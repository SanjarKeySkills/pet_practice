# Big O notation understanding task
#write the function  which receives array of numbers and return true, if at leat one duplicate will be in array and put
# 'false' in opposite case
#[1, 2, 3, 4, 5] -> false
#[1, 2, 3, 2, 4] -> (2 num duplicates)

# def has_duplicate_brute_force(nums):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if nums[i] == nums[j]:
#                 return True
#     return False
# ------------------------------------
# Big O: O(n^2)

# Merge Sort
def merge_sort(arr): 
    """Сортировка слиянием - классический пример O(N log N)"""
    if len(arr) <= 1:
        return arr
    
    # Разделяем массив пополам - O(1)
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Рекурсивно сортируем каждую половину - 2 * O(N/2 log N/2)
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Объединяем отсортированные половины - O(N)
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """Слияние двух отсортированных массивов"""
    result = []
    i = j = 0
    
    # Слияние элементов - O(N)
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Добавляем оставшиеся элементы
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Пример использования
arr = [120, 55, 38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(f"Хаха - Это! Отсортированный массив: {sorted_arr}")

# -----------------------------------------
# Встроенная сортировка Python (Timsort)

