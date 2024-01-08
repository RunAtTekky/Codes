def binarySearch(lst: list,start: int, end: int, target: int) -> int:
    if start > end:
        return -1
    mid = int((start+end)/2)

    if lst[mid] < target:
        return binarySearch(lst,mid+1,end,target)
    elif lst[mid] > target:
        return binarySearch(lst, start, mid-1, target)
    else:
        return mid

lst = [3,4,5,6,7,8,9]
print(f"This is the list: {lst}\nEnter the target number: ")
target= int(input())

ind = binarySearch(lst,0,len(lst)-1,target)

if ind == -1:
    print("Target not found.")
else:
    print(f"Index of target is {ind}")
