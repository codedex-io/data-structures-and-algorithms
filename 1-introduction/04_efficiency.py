# Efficiency Demo
# Codédex

import random

# Algorithm 1
def linear_search(arr, target):
    guesses = 0
    for i in range(len(arr)):
        guesses += 1  # Counting each guess
        if arr[i] == target:
            print(f"Found {target} in {guesses} guesses using linear search.")
            return i
    print(f"{target} not found after {guesses} guesses using linear search.")
    return -1

# Algorithm 2
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    guesses = 0  # Counting guesses

    while left <= right:
        guesses += 1
        mid = (left + right) // 2

        if arr[mid] == target:
            print(f"Found {target} in {guesses} guesses using binary search.")
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    print(f"{target} not found after {guesses} guesses using binary search.")
    return -1

# Change these values
range_low = 1
range_high = 100000

numbers = [i for i in range(range_low, range_high + 1)]
random_num = random.randint(range_low, range_high)

print(f"Your secret number is {random_num}")

linear_search(numbers, random_num)
binary_search(numbers, random_num)
