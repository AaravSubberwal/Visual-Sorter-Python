import random
import time
import os

class Control:
    @staticmethod
    def clear_terminal():
        os.system('clear' if os.name == 'posix' else 'cls')
        print("\033[H", end="")
    
    @staticmethod
    def printit(lst, cursor,name=""):
        Control.clear_terminal()
        print("\033[36m"+(45*"     ")+name)
        for i in range(len(lst)):      #ewww
            line=""
            if(cursor==i): 
                for j in range(lst[i]):
                    line+="#  "
                print("\033[31m",line,"\n\033[36m")
                continue
            for j in range(lst[i]):
                    line+="#  "
            print(line,"\n")
        time.sleep(t)

    @staticmethod
    def endit(lst,name=""):
        for i in range(len(lst),-1,-1):
            Control.printit(lst,i,name)
        Control.printit(lst,-1,name)

class Sorts:
    def __init__(self, program):
        self.program = program

    def bubble_sort(self, arr):
        n = len(arr)
        name = "Bubble Sort"
        self.program.printit(arr, -1, name)
        for i in range(n):
            swapped = False  
            for j in range(0, n - i - 1):
                self.program.printit(arr, j, name)
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True 
            if not swapped:  
                break
        self.program.endit(arr, name)

    
    def selection_sort(self, arr):
        n = len(arr)
        name = "Selection Sort"
        self.program.printit(arr, -1, name)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                self.program.printit(arr, j, name)
                if arr[j] < arr[min_index]: 
                    min_index = j
            if min_index != i: 
                arr[i], arr[min_index] = arr[min_index], arr[i]
        self.program.endit(arr, name)



    def insertion_sort(self, arr):
        name="Insertion Sort"
        self.program.printit(arr, -1,name)
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                self.program.printit(arr, j,name)
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        self.program.endit(arr,name)

    def merge_sort(self, arr):
        name="Merge Sort"
        self.program.printit(arr, -1,name)
        n = len(arr)
        current_size = 1
        while current_size < n:
            for left in range(0, n, 2 * current_size):
                mid = min(left + current_size - 1, n - 1)
                right = min(left + 2 * current_size - 1, n - 1)
                self.merge(arr, left, mid, right)            
            current_size *= 2
        self.program.endit(arr,name)

    def merge(self, arr, left, mid, right):
        left_sub = arr[left:mid + 1]
        right_sub = arr[mid + 1:right + 1]
        name="Merge Sort"
        i, j, k = 0, 0, left
        while i < len(left_sub) and j < len(right_sub):
            if left_sub[i] <= right_sub[j]:
                arr[k] = left_sub[i]
                i += 1
            else:
                arr[k] = right_sub[j]
                j += 1
            k += 1
            self.program.printit(arr, k,name)
        while i < len(left_sub):
            arr[k] = left_sub[i]
            i += 1
            k += 1
        while j < len(right_sub):
            arr[k] = right_sub[j]
            j += 1
            k += 1
    
    def quick_sort(self,arr):
        name="Quick Sort"
        self.program.printit(arr,-1,name)
        n = len(arr)
        stack = [(0, n - 1)]  
        while stack:
            low, high = stack.pop()
            if low < high:
                pi = self.partition(arr, low, high)  
                stack.append((low, pi - 1))
                stack.append((pi + 1, high))  
        self.program.endit(arr,name)

    def partition(self,arr, low, high):
        name="Quick Sort"
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            self.program.printit(arr,j,name)
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1


if __name__ == "__main__":
    t=0.004
    program = Control()
    sorter = Sorts(program)

    arr = list(range(1, 53))
    random.shuffle(arr)
    sorter.bubble_sort(arr.copy())
    time.sleep(1)
    sorter.selection_sort(arr.copy())
    time.sleep(1)
    t=0.02
    sorter.insertion_sort(arr.copy())
    time.sleep(1)
    sorter.merge_sort(arr.copy())
    time.sleep(1)
    sorter.quick_sort(arr)

    