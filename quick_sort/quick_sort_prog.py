
def hoare_partition(elements,start,end):
    #Let us consider the starting element as pivot index
    pivot_index = start
    #let us store the value present in the pivot index into pivot variable.
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start = start + 1
        while elements[end] > pivot:
            end = end - 1
        if start < end:
            elements[start],elements[end] = elements[end],elements[start]
    elements[pivot_index],elements[end] = elements[end],elements[pivot_index]
    return end



def quick_sort_c(elements,start,end):
    if start < end:
        pi = hoare_partition(elements,start,end)
        quick_sort_c(elements,start,pi-1)
        quick_sort_c(elements,pi+1,end)

if __name__ == "__main__":
    elements = [11,9,29,7,2,30]
    print(elements)
    quick_sort_c(elements,0,len(elements)-1)
    print(elements)
