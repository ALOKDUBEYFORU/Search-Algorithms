
def merge_sort_e(elements,key,order="asc"):
    if len(elements) <=1 :
        return
    mid = len(elements)//2

    left = elements[:mid]
    right = elements[mid:]
    merge_sort_e(left,key,order)
    merge_sort_e(right,key,order)

    merge_two_sorted_list(left,right,elements,key,order)

def merge_two_sorted_list(left,right,elements,key,order):
    len_left = len(left)
    len_right = len(right)

    i = j = k = 0
    while i < len_left and j < len_right:
        if order == 'asc':
            if left[i][key] <= right[j][key]:
                elements[k] = left[i]
                i = i+1
            else:
                elements[k] = right[j]
                j = j+1
        else:
            if left[i][key] >= right[j][key]:
                elements[k] = left[i]
                i = i+1
            else:
                elements[k] = right[j]
                j = j+1
        k = k+1

    while i < len_left:
        elements[k] = left[i]
        i = i+1
        k = k+1
    while j < len_right:
        elements[k] = right[j]
        j = j+1
        k = k+1

if __name__ == "__main__":
    elements = [
            { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
            { 'name': 'rajab', 'age': 12,  'time_hours': 3},
            { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
            { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
        ]
    merge_sort_e(elements,'age',order='desc')
    print(elements)