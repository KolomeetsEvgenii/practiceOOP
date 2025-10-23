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

"""
A. Неправильные горы
"""
def main(arr):
    current = arr[0]
    current_index = 0
    if len(arr) < 3:
        return False
    if arr[1] < arr[0]:
        return False

    for i in range(1, len(arr) - 1):
        if arr[i] > current:
            current = arr[i]
            current_index = i
            continue
        else:
            break
    for i in range(current_index + 1, len(arr)):
        if arr[i] < current:
            current = arr[i]
            continue
        else:
            return False

    return True


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    result = main(arr)
    print(result)
