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