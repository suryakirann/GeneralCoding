arr = [1,2,3,4,5]
arr2 = [1,2,3,4,5,6]
t_string = "Reverse"
arr_2 = []
swap = 0


def getReversedString(in_string):
    return in_string[::-1]

def getReversedString_2(in_string):
    return ''.join(in_string[i] for i in range(len(in_string)-1, -1, -1))

def getReversedString_3(in_string):
    t_string2 = ""
    for i in in_string:
        t_string2 = i + t_string2
    return t_string2

def getReversedArray(in_array):
    for i in range(len(in_array)-1, -1, -1):
        arr_2.append(in_array[i])
    return arr_2

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
        

print(getReversedString(t_string))
print(getReversedString_2(t_string))
print(getReversedString_3(t_string))
print(getReversedArray(arr))
print(getReversedArray_2(arr2))
print(len(arr))

print(*(x**2 for x in range(10)))
a = [x**2 for x in range(3)]
print(a)

j = ''.join(str(s) for s in range(10))
print(j)
k = [*iter(range(10))]
print(k)
print(*iter(range(10)))

file_path = "C:\xyz"
with open(file_path, 'r') as fp:
    for line in fp:
        print(line)