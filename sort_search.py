def bubble_sort_2d(arr):
    n = len(arr)
    m = len(arr[0])
    total_element = n * m
    for i in range (total_element - 1):
        for j in range (total_element - 1 - i):
            row1 = j // m
            col1 = j % m
            row2 = (j + 1)//m
            col2 = (j + 1) % m
            if arr[row1][col1] > arr[row2][col2]
            arr[row1][col1]arr[]
