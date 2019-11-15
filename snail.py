"""Demonstrate the snail sort."""


def snail_sort(matrix):
    """Unwind a matrix clockwise into a string."""
    new_list = []

    while matrix:
        new_list.extend(matrix.pop(0))
        if not matrix:
            continue

        for i in range(len(matrix)):
            new_list.append(matrix[i].pop())
            if not matrix:
                break
        if not matrix:
            continue

        new_list.extend(reversed(matrix.pop()))
        if not matrix:
            continue

        for i in range(len(matrix) - 1, -1, -1):
            new_list.append(matrix[i].pop(0))
            if not matrix:
                break
    return new_list


MATRIX = [
    [1, 2, 3, 4, 5],
    [16, 17, 18, 19, 6],
    [15, 24, 25, 20, 7],
    [14, 23, 22, 21, 8],
    [13, 12, 11, 10, 9],
]

print(snail_sort(MATRIX))
