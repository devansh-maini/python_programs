#For Binary Search the list  should be Sorted

n = int(input("Enter The number of element in list: "))

arr = []

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    arr.append(num)

data = int(input("Enter the element you want to search: "))

def BinarySearch(data):
    l = 0
    r = n - 1
    while l <= r:
        mid = (l+r)//2
        
        if data == arr[mid]:
            return f"Yes the element is in the list and at index {mid} and location is {mid+1}."
            
        elif data < arr[mid]: 
            r = mid - 1
            
        else:
            l = mid + 1
            
    return f"No! the element is not present in this list. "
    
    
result = BinarySearch(data)

print(result)
