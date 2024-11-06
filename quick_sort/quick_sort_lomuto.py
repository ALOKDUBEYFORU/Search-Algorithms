def quicksort(arr, low, high):
    if len(arr) == 1 :
        return
    if low < high  :
        p = lomuto_partition(arr,low,high)
        quicksort(arr,low,p-1)
        quicksort(arr,p+1,high)

def lomuto_partition(arr,low,high):
    pivot = arr[high]
    p_index = low

    for i in range(low,high):
        if arr[i] <= pivot:
            arr[p_index],arr[i] = arr[i],arr[p_index]
            p_index = p_index+1

    arr[p_index],arr[high] = arr[high],arr[p_index]
    return i

if __name__ == "__main__":
    A = [4,2,7,3,1,9,6,0,8]
    low,high = 0,len(A)-1
    print('before sorting',A)
    quicksort(A,low,high)
    print('after sorting',A)