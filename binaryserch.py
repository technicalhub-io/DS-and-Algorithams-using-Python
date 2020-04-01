def binary_search(array,key):
    L=0#Lower boun
    U=len(array)-1#Upper bound
    while L<=U:
        mid=(L+U)//2#Mid
        #compare wither mid index value is equal to key
        if array[mid]==key:
            return True
        #if mid index value is not equal to key then check wether greater or lesser
        else:
            if key>array[mid]:
                L=mid+1
            else:
                U=mid-1
    return False
                

array=[2,3,4,5,6,9,7,8]
array.sort()
key=10
if binary_search(array,key):
    print("Found")
else:
    print("Not Found")
