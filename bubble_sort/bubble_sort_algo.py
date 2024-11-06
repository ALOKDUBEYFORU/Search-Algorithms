
def bubble_sort(nums):
    for i in range(0,len(nums)-1):
        swap = False
        for j in range(0,len(nums)-1-i):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                swap = True
        if not swap:
            break
    return nums

if __name__ == "__main__" :
    nums = [1,2,6,4,3,7,8]
    print(bubble_sort(nums))
