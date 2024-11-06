def num_to_find(numbers,num,left,right,index_arr=[]):
    mid = (left+right)//2
    if left > right:
        return -1
    if numbers[mid] == num:

        i = mid
        while numbers[i] == numbers[mid] :
            index_arr.append(i)
            i = i-1

        i = mid+1
        while numbers[i] == numbers[mid] :
            index_arr.append(i)
            i = i+1
        return index_arr

    elif num > numbers[mid] :
        left = mid+1
    else:
        right = mid-1
    return num_to_find(numbers, num, mid + 1, right, index_arr)

numbers = [1,4,6,9,11,15,15,15,21,34,34,56]
num = 15
index_arr = []
print(num_to_find(numbers,num,0,len(numbers),index_arr))
