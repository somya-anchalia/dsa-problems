from typing import List

def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)
    # transposing the matrix
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    print("Transposed Matrix")
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print()

    # reversing each row of the matrix
    for i in range(n):
        matrix[i].reverse()

if __name__ == "__main__":

    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print("Original Matrix")
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print()

    rotate(arr)

    print("Rotated Matrix")
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j], end=" ")
        print()
