import random
import time

# Interpolation Search Function
def interpolation_search(arr, key):
    low = 0
    high = len(arr) - 1
    probes = 0

    start_time = time.perf_counter()

    while low <= high and key >= arr[low] and key <= arr[high]:

        probes += 1

        # Avoid division by zero
        if arr[low] == arr[high]:
            if arr[low] == key:
                end_time = time.perf_counter()
                return low, probes, end_time - start_time
            break

        # If only one element remains
        if low == high:
            if arr[low] == key:
                end_time = time.perf_counter()
                return low, probes, end_time - start_time
            break

        # Formula for estimating position
        pos = low + int(
            ((high - low) / (arr[high] - arr[low]))
            * (key - arr[low])
        )

        if arr[pos] == key:
            end_time = time.perf_counter()
            return pos, probes, end_time - start_time

        elif arr[pos] < key:
            low = pos + 1

        else:
            high = pos - 1

    end_time = time.perf_counter()
    return -1, probes, end_time - start_time


# Generate Uniform Dataset
def generate_uniform(n):
    return [i * 10 for i in range(1, n + 1)]


# Generate Non-Uniform Dataset
def generate_non_uniform(n):
    arr = []
    value = 1

    for _ in range(n):
        value += random.randint(1, 20)
        arr.append(value)

    return arr


# -------------------- Main Program --------------------

print("\n=== INTERPOLATION SEARCH ===")

print("\nChoose Dataset Type")
print("1. Uniform Distribution")
print("2. Non-Uniform Distribution")

choice = int(input("Enter choice: "))

print("\nChoose Input Method")
print("1. Manual Entry")
print("2. Random Generation")

method = int(input("Enter choice: "))

# Dataset Creation
if method == 1:

    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter elements: ").split()))

else:

    n = int(input("Enter number of elements: "))

    if choice == 1:
        arr = generate_uniform(n)
    else:
        arr = generate_non_uniform(n)

# Dataset Type
if choice == 1:
    print("\nUniform Dataset")
else:
    print("\nNon-Uniform Dataset")

print(arr)

# Check Sorting
if arr != sorted(arr):

    sort_choice = input("\nDataset is unsorted. Sort it? (y/n): ")

    if sort_choice.lower() == 'y':
        arr.sort()
        print("Sorted Array:", arr)

# Search Key
key = int(input("\nEnter search key: "))

# Perform Search
index, probes, exec_time = interpolation_search(arr, key)

# Result
print("\n----- RESULT -----")

if index != -1:
    print(f"Key {key} found at index {index}")
else:
    print(f"Key {key} not found.")

print("Number of Probes/Comparisons :", probes)
print("Execution Time               : {:.6f} seconds".format(exec_time))

# Complexity
print("\nComplexity Analysis")
print("------------------------------")
print("Best Case        : O(1)")
print("Average Case     : O(log log n) (Uniform Data)")
print("Worst Case       : O(n)")
print("Space Complexity : O(1)")
