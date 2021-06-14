# Function to swap two characters in a character array
'''def swap(ch, i, j):
    temp = ch[i]
    ch[i] = ch[j]
    ch[j] = temp


# Recursive function to generate all permutations of a string
def permutations(ch, curr_index=0):
    if curr_index == len(ch) - 1:
        print(''.join(ch))

    for i in range(curr_index, len(ch)):
        swap(ch, curr_index, i)
        permutations(ch, curr_index + 1)
        swap(ch, curr_index, i)
s = "ABC"
permutations(list(s))'''

def permutations(s):
    # create a list to store (partial) permutations
    partial = []

    # initialize the list with the first character of the string
    partial.append(s[0])

    # do for every character of the specified string
    for i in range(1, len(s)):

        # consider previously constructed partial permutation one by one

        # iterate backward
        for j in reversed(range(len(partial))):

            # remove the current partial permutation from the list
            curr = partial.pop(j)

            # Insert the next character of the specified string into all
            # possible positions of current partial permutation.
            # Then insert each of these newly constructed strings into the list

            for k in range(len(curr) + 1):
                partial.append(curr[:k] + s[i] + curr[k:])

    print(partial, end='')
s = "ABCD"
permutations(list(s))