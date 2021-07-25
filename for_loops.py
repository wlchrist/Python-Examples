#iterate through a 3D array

# Python 3 program to demonstrate working
# of method 1 and method 2.

rows, cols = (5, 5)

# method 2a
arr = [[0] * cols] * rows

arr[0][0] = 1
for row in arr:
    print(row)