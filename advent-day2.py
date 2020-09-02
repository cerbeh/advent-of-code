import itertools as it

sequence = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,9,19,1,10,19,23,2,9,23,27,1,6,27,31,2,31,9,35,1,5,35,39,1,10,39,43,1,10,43,47,2,13,47,51,1,10,51,55,2,55,10,59,1,9,59,63,2,6,63,67,1,5,67,71,1,71,5,75,1,5,75,79,2,79,13,83,1,83,5,87,2,6,87,91,1,5,91,95,1,95,9,99,1,99,6,103,1,103,13,107,1,107,5,111,2,111,13,115,1,115,6,119,1,6,119,123,2,123,13,127,1,10,127,131,1,131,2,135,1,135,5,0,99,2,14,0,0]


def multiply(a,b):
    return a * b

def doSomeMaths(start, arr):
    # Maths
    action = arr[start]
    if action == 99:
        return arr

    # To Replace
    a = arr[start + 3]

    # To multiply
    b = arr[start + 1]
    c = arr[start + 2]
    arr[a] = sum([arr[b], arr[c]]) if action == 1 else multiply(arr[b], arr[c])
    return doSomeMaths(start + 4, arr)

def computer(a, b, arr):
    arr[1] = a
    arr[2] = b
    return doSomeMaths(0, arr)

def counter(noun, verb):
    # If noun == 99 noun = 0 verb + 1
    (newNoun, newVerb) = (noun + 1, verb) if noun != 99 else (0, verb + 1)
    return (newNoun, newVerb)

for noun in range(100):
    for verb in range(100):
        newArray = computer(noun, verb, list(sequence))
        if newArray[0] == 19690720:
            result = (100 * noun + verb)
            break;

# Iterate over
# find 1 or 2
# Do Math
# Move 4 spaces forward on NEW array
# Rinse and repeat til 99
