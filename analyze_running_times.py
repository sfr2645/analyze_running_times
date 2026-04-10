import random
from algorithms import recursive_binary_search, iterative_binary_search, sequential_search

arr = sorted([random.randint(1, 100) for _ in range(20)])
target = random.choice(arr) if random.random() < 0.5 else 999

print("Array:", arr)
print("Target:", target)

print("Recursive:", recursive_binary_search(arr, target, 0, len(arr)-1))
print("Iterative:", iterative_binary_search(arr, target))
print("Sequential:", sequential_search(arr, target))