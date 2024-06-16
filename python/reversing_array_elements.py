arr = [1, 2, 3, 4, 5]
#method - 1: built-in reverse()
arr.reverse() 
print(arr)

#method - 2: slicing
reversed_arr = arr[::-1]
print(reversed_arr)

#method - 3: reversed()
revrs_arr = list(reversed(reversed_arr))
print(revrs_arr)

#method - 4: for loop
revrs_arr2 = []
for i in range(len(revrs_arr)-1, -1, -1):
    revrs_arr2.append(arr[i])
print(revrs_arr2)

arr = [1,2,3,4,5]
arr2 = [1,2,3,4,5,6]
swap = 0
def getReversedArray_2(in_array):
    d_ctr = len(in_array)-1
    c_ptr = len(in_array)//2
    for i in range(c_ptr):
        swap = in_array[i]
        in_array[i] = in_array[d_ctr]
        in_array[d_ctr] = swap
        if d_ctr != c_ptr:
            d_ctr -= 1
    return in_array

print(getReversedArray_2(arr))
print(getReversedArray_2(arr2))

