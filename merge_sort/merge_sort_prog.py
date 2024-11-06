def merge_sort_c(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort_c(left)
    merge_sort_c(right)
    merge_two_sorted_list(left,right,arr)

def merge_two_sorted_list(left,right,arr):
    len_left = len(left)
    len_right = len(right)
    i = j = k = 0

    while i<len_left and j < len_right:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j+1
        k = k+1
    while i < len_left:
        arr[k] = left[i]
        i = i+1
        k = k+1
    while j < len_right:
        arr[k] = right[j]
        j = j+1
        k = k+1

if __name__ == "__main__":
    test_cases = [
        [10,3,4,5,6,9,8],
        [],
        [2],
        [1,2,3,4],
        [4,3,2,1]
    ]
    for arr in test_cases :
        merge_sort_c(arr)
        print(arr)