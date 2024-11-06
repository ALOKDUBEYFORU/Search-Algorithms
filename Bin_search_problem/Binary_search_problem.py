def binary_search_method(start,end,num,arr1):
    mid = (start + end)//2
    if num == arr1[mid]:
        return mid

    if start == end and arr1[mid] != num:
        return -1

    if num < arr1[mid]:

        return binary_search_method(start,mid,num,arr1)
    else:
        return binary_search_method(mid,end,num,arr1)

if __name__ == "__main__":
    numbers = [1,4,6,9,10,5,7]
    numbers = sorted(numbers)
    print(numbers)
    print(binary_search_method(0,len(numbers),5,numbers))