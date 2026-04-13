from algorithms import recursive_binary_search, iterative_binary_search, sequential_search

arr = [3, 5, 8, 12, 14, 18, 21]
arr.sort()

target1 = 12  
target2 = 9 

index = recursive_binary_search(arr, target1, 0, len(arr) - 1)
print(f"{target1} found at index {index}" if index != -1 else f"{target1} not found")

index = recursive_binary_search(arr, target2, 0, len(arr) - 1)
print(f"{target2} found at index {index}" if index != -1 else f"{target2} not found")

index = iterative_binary_search(arr, target1)
print(f"{target1} found at index {index}" if index != -1 else f"{target1} not found")

index = iterative_binary_search(arr, target2)
print(f"{target2} found at index {index}" if index != -1 else f"{target2} not found")

index = sequential_search(arr, target1)
print(f"{target1} found at index {index}" if index != -1 else f"{target1} not found")

index = sequential_search(arr, target2)
print(f"{target2} found at index {index}" if index != -1 else f"{target2} not found")
