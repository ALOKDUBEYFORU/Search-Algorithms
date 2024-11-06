def bubble_sort(elements,key_name):
    for i in range(0,len(elements)-1):
        swap = False
        for j in range(0,len(elements)-1-i):
            if elements[j][key_name] > elements[j+1][key_name]:
                elements[j],elements[j+1] = elements[j+1],elements[j]
                swap = True
        #print(elements)
        if not swap:
            break
    return elements

elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
print(bubble_sort(elements,'transaction_amount'))

print(bubble_sort(elements,'name'))