def mergeSort(array):
    length=len(array)
    if length!=1:
        mid=length//2
        left=array[0:mid]
        right=array[mid:length]
        mergeSort(left)
        mergeSort(right)
    else:
        return array

def mergeSort2(left,right):


arr = []
for _ in range(int(input())): arr.append(int(input()))

