
# Unsorted array of 10 elements
array = [5, 2, 9, 1, 5, 6, 7, 3, 8, 0]

# Bubble sort algorithm
n = len(array)
for i in range(n):
    for j in range(0, n-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]

print("Sorted array:", array)


# Finding the maximum element
max_element = array[0]
for number in array:
    if number > max_element:
        max_element = number

print("Maximum element:", max_element)

# Finding the largest and second largest elements
first, second = float('-inf'), float('-inf')
for number in array:
    if number > first:
        first, second = number, first
    elif first > number > second:
        second = number

print("Second largest element:", second)

# Reversing the array
n = len(array)
for i in range(n // 2):
    array[i], array[n - i - 1] = array[n - i - 1], array[i]

print("Reversed array:", array)

# Array with duplicates
array = [5, 2, 9, 1, 5, 6, 7, 3, 8, 0, 2, 9]

# Removing duplicates
unique_elements = []
for number in array:
    if number not in unique_elements:
        unique_elements.append(number)

print("Array without duplicates:", unique_elements)

# Array with a missing number (1 to 10, but missing 6)
array = [5, 2, 9, 1, 4, 7, 3, 8, 10]

# Finding the missing number
n = 10
expected_sum = n * (n + 1) // 2
actual_sum = 0
for number in array:
    actual_sum += number

missing_number = expected_sum - actual_sum

print("Missing number:", missing_number)
