def binary_search(arr, target):
    key= 77
    numbers={11,22,33,44,55,66,77,88,99}
    low = 0
    high = len(arr) - 1
    found= False

    while start <= end:
        mid =(low+high)//2
        if numbers[mid] ==key:
            print("Found Element at pos", mid)
            found = True
        elif key<numbers[mid]:
            end = mid-1
        else:
            start=mid+1    
    if not found:
        print(f"{key}Not found in the list")        