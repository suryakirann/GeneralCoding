def reverse(sampleInput):
    return sampleInput[::-1]

def reverse2(sampleInput):
    return ''.join(sample[i] for i in range(len(sample)-1,-1,-1))

def reverse3(sampleInput):
    sampleInput = ""
    for i in sampleInput:
        sampleInput = i + sampleInput
    return sampleInput


sample = "iNueron"
print(reverse(sample))
print(reverse2(sample))
print(reverse3(sample))
print(sample[0]+sample[1])

