# import sys

# def main():
#     n = int(sys.stdin.readline().rstrip())
#     arr = list(map(int, sys.stdin.readline().split()))
#     output_numbers = sorted(set(arr))
#     if len(output_numbers) < n:
#         for _ in range(len(output_numbers), n):
#             output_numbers.append('_')
#     print(' '.join(map(str, output_numbers)))


# if __name__ == '__main__':
#     main()

import sys


def main():
    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().split()))

    seen = set()
    unique = []

    for num in arr:
        if num not in seen:
            seen.add(num)
            unique.append(num)

    output_numbers = unique + ['_'] * (n - len(unique))

    print(' '.join(map(str, output_numbers)))


if __name__ == '__main__':
    main()

arr = list(map(int, input().split()))
target = int(input())

# Бинарный поиск
left, right = 0, len(arr)

while left < right:
    mid = (left + right) // 2
    if arr[mid] < target:
        left = mid + 1
    else:
        right = mid

print(left)

# def find_element(sorted_numbers, element):
#     left, right = 0, len(sorted_numbers)

#     while left < right:
#         mid = (left + right) // 2
#         if sorted_numbers[mid] < element:
#             left = mid + 1
#         else:
#             right = mid

#     return left


# arr = [1, 1, 1, 1]
# print(find_element(arr, 1))

# def delete_dublikat(sorted_numbers):
#     arr = []
#     arr.append(sorted_numbers[0])
#     for i in range(1, len(sorted_numbers)):
#         if sorted_numbers[i] != sorted_numbers[i - 1]:
#             arr.append(sorted_numbers[i])
        
    
#     result = arr + ['_'] * (len(sorted_numbers) - len(arr))
#     return result


# print(delete_dublikat([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

example_array = [6, 5, 3, 1, 8, 7, 2, 4]


def bubble_sort(data):
    swapped = True
    last_index = len(data) - 1
    while swapped:
        swapped = False
        for item_index in range(last_index):
            if data[item_index] > data[item_index + 1]:
                data[item_index], data[item_index + 1] = data[item_index + 1], data[item_index]
                swapped = True
        last_index -= 1

    return data


print(bubble_sort(example_array))
