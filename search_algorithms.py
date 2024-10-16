import random
import datetime

def calc_time(function_name,*args):
    def wrapper(*args,**kwargs):
        startdt = datetime.datetime.now()
        result =  function_name(*args,**kwargs)
        enddt = datetime.datetime.now()
        print(f"time taken by {function_name} is {enddt - startdt}")
        return result
    return wrapper

@calc_time
def linear_search(list1,num1):
    for i in list1:
        if i == num1:
            print(f'number found at {i} using', {lambda n=0: sys._getframe(n + 1).f_code.co_name})
            bool1 = True
            return 0
    print(f'number not found using', {lambda n=0: sys._getframe(n + 1).f_code.co_name})
    return -1

@calc_time
def binary_search(list1,num1):
    lnum = 0
    rnum = len(list1)

    while rnum >= lnum:
        midval = int((rnum + lnum) / 2)
        if list1[midval] == num1:
            print(f'number found at {midval} using', {lambda n=0: sys._getframe(n + 1).f_code.co_name})
            bool1 = True
            return 0
        elif list1[midval] > num1:
            rnum = midval - 1
        elif list1[midval] < num1:
            lnum = midval + 1
    print('number not found using', {lambda n=0: sys._getframe(n + 1).f_code.co_name})
    return -1

@calc_time
def binary_search_rev(list1,num1,lnum,rnum):
    midval = int(lnum+rnum/2)
    if len(list1) <= 0 :
        return -1
    elif num1 == list1[midval]:
        print('found the value')
        return midval
    elif num1 < list1[midval]:
        return binary_search_rev(list1,num1,lnum,midval+1)
    elif num1 > list1[midval]:
        return binary_search_rev(list1,num1,midval+1,rnum)


list1 = [i for i in range(100000000)]
num1 = 99999999
result = linear_search(list1,num1)
result = binary_search(list1,num1)
result = binary_search_rev(list1,num1,0,len(list1)-1)

print(result, 'binary search rev')