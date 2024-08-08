input_string = input("Enter a list of numbers separated by spaces: ")
arr = list(map(int, input_string.split()))
print("Unsorted list:", arr)
n = len(arr)
for i in range(n):
    min_index = i
    for j in range(i+1, n):
        if arr[j] < arr[min_index]:
            min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
print("Sorted list:", arr)
