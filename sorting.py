import random
import time
import os
t=0.02

def printit(lst,cursor):
    clear_terminal()
    for i in range(len(lst)):
        if(cursor==i):       #ewww 
            for j in range(lst[i]):
                print("\033[33m#\033[0m",end=" ") 
            print("\n")
            continue
        for j in range(lst[i]):
            print("#",end=" ")
        print("\n")
    time.sleep(t)

def endit(lst):
    for i in range(len(lst),-1,-1):
        printit(lst,i)
    printit(lst,-1)

def sortlabel(string):
    pass

def clear_terminal():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("\033[H", end="")

def bubble_sort(arr):
    n = len(arr)
    printit(arr,-1)
    for i in range(n):
        for j in range(0, n - i - 1):
            printit(arr,j)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    endit(arr)
    
def selection_sort(arr):
    n = len(arr)
    printit(arr,-1)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            printit(arr,j)
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    endit(arr)

def insertion_sort(arr):
    printit(arr,-1)
    n=len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            printit(arr,j)
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    endit(arr)

def merge_sort(arr):
    printit(arr,-1)
    n = len(arr)
    current_size = 1
    while current_size < n:
        for left in range(0, n, 2 * current_size):
            mid = min(left + current_size - 1, n - 1)
            right = min(left + 2 * current_size - 1, n - 1)
            merge(arr, left, mid, right)
        
        current_size *= 2
    endit(arr)

def merge(arr, left, mid, right):
    left_sub = arr[left:mid + 1]
    right_sub = arr[mid + 1:right + 1]
    i, j, k = 0, 0, left
    while i < len(left_sub) and j < len(right_sub):
        if left_sub[i] <= right_sub[j]:
            arr[k] = left_sub[i]
            i += 1
        else:
            arr[k] = right_sub[j]
            j += 1
        k += 1
        printit(arr,k)
    while i < len(left_sub):
        arr[k] = left_sub[i]
        i += 1
        k += 1
    while j < len(right_sub):
        arr[k] = right_sub[j]
        j += 1
        k += 1
    
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        printit(arr,j)
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr):
    printit(arr,-1)

    n = len(arr)
    stack = [(0, n - 1)]  

    while stack:
        low, high = stack.pop()

        if low < high:
            pi = partition(arr, low, high) 
            stack.append((low, pi - 1)) 
            stack.append((pi + 1, high))  
    endit(arr)


numbers = list(range(1, 73))
random.shuffle(numbers)
bubble_sort(numbers.copy())
selection_sort(numbers.copy())
insertion_sort(numbers.copy())
merge_sort(numbers.copy())
quick_sort(numbers.copy())

