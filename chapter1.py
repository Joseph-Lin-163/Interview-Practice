# Check if string has all unique characters. What if cannot use additional data structures?
def isUnique(s):
    # Naive solution: Check each character across all other characters
    # BigO: O(n^2)
    unique = 1
    for idx, letter in enumerate(s):
        # range returns [] when range(10,10) or range(11,10)
        for num in range(idx+1, len(s)):
            if letter == s[num]:
                print("Not unique at positions: {} and {}.".format(idx, num))
                unique = 0

    print(list(enumerate(s)))
    result = "Unique!" if unique == 1 else "Not unique!"
    print(result)

    # Better solution: Can use a set to determine if there is membership
    if len(set(s)) != len(s):
        print("Not unique!")
    else:
        print("Unique!")

    # Not using any data structures, sort the string and then traverse it character by character
    # print(mergesort(s))
    sorted_s = mergesort(s)
    for num in range(len(sorted_s)):
        if num == len(sorted_s) - 1:
            print("Unique!")
            break

        if sorted_s[num] == sorted_s[num+1]:
            print("Not unique!")
            break

    return

# Check if 2 strings are permutations of each other
# Permutation: same characters, different order
def checkPermutation(s1, s2):
    # dictionary w/ the values being the # of appearances and then checking for equality on the dictionaries
    # O(n)
    s1_dict = {}
    s2_dict = {}

    if len(s1) != len(s2):
        print("Not permutations")
        return

    for char in s1:
        if char not in s1_dict.keys():
            s1_dict[char] = 1
        else:
            s1_dict[char] += 1

    for char in s2:
        if char not in s2_dict.keys():
            s2_dict[char] = 1
        else:
            s2_dict[char] += 1

    if s1_dict == s2_dict:
        print("Permutations")
    else:
        print("Not permutations")

    return

# Given input string with the "true length", replace all spaces with '%20'
def urlify(s, truelen):
    url_len = len(s)
    true_idx = truelen - 1
    url_idx = url_len

    s = list(s)

    while (true_idx > -1):
        if s[true_idx] != ' ':
            s[url_idx-1] = s[true_idx]
            url_idx -= 1
            true_idx -= 1
            print(s)
        else:
            s[url_idx - 3:url_idx] = ['%', '2', '0']
            url_idx -= 3
            true_idx -= 1
            print(s)

    print(''.join(s))

# Determine if a string is a permutation of a palindrome
def palindromePermutation(s):
    # Can ignore spaces
    # Use a dictionary and do counts
    # If more than one value is odd, not palindrome. O(n)
    s = s.lower()
    palin_dict = {}
    for char in s:
        if char == ' ':
            continue

        if char not in palin_dict:
            palin_dict[char] = 1
        else:
            palin_dict[char] += 1

    num_odd = 0
    for key in palin_dict.keys():
        if palin_dict[key] % 2 == 1:
            num_odd += 1
            if num_odd > 1:
                print("Not palindrome")

    if num_odd < 2:
        print("Palindrome")

    return

# Check if two strings are one or zero edits away from each other
# Can add, remove, or replace a character
def oneAway(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        print("Not one away")

    s1_idx = 0
    s2_idx = 0

    total_len = len(s1) if len(s1) < len(s2) else len(s2)
    total_replace_allowed = 1 if len(s1) == len(s2) else 0
    total_add_remove_allowed = 1 if len(s1) != len(s2) else 0

    for idx in range(total_len):
        if s1[s1_idx] == s2[s2_idx]:
            s1_idx += 1
            s2_idx += 1
            continue

        if total_replace_allowed:
            total_replace_allowed -= 1
            s1_idx += 1
            s2_idx += 1
            continue

        if total_add_remove_allowed:
            total_add_remove_allowed -= 1
            if len(s1) < len(s2):
                s2_idx += 1
            else:
                s1_idx += 1
            continue

        print("Not one away")
        return

    print("One away")

    return

# Compress string using counts of repeats
# If compressed is not smaller, then return original string
def stringCompression(s):
    compressedString = ''
    mod_count = 0

    repeats = -1
    repeat_char = ''

    for char in s:
        if repeats == -1:
            repeat_char = char
            repeats = 1
            continue

        if char == repeat_char:
            repeats += 1
            continue
        else:
            compressedString += repeat_char + str(repeats)
            mod_count += repeats - 2
            repeat_char = char
            repeats = 1

    # Get last part of string
    compressedString += repeat_char + str(repeats)
    mod_count += repeats - 2

    if mod_count > 0:
        print("Compressed string: {}, space saved: {}".format(compressedString, mod_count))
    else:
        print(s)

    return

# Rotate an image 90 degrees in place, represented by an NxN matrix, each pixel is 4 bytes
def rotateImage(img):

    if len(img[0]) == 1:
        print(img)
        return

    length = len(img[0])
    levels = int(len(img[0])/2)
    for i in range(levels):
        for j in range(i, len(img[0]) - i - 1):
            temp1 = img[i][j]
            temp2 = img[j][length-1-i]
            temp3 = img[length-1-i][length-1-j]
            temp4 = img[length-1-j][i]
            img[j][length-1-i] = temp1
            img[length-1-i][length-1-j] = temp2
            img[length-1-j][i] = temp3
            img[i][j] = temp4

    for row in img:
        print(row)
    return

# Return MxN matrix s.t. if any element is 0, it's row and column is set to 0
def zeroMatrix(matrix):
    zeroes = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                zeroes.append((i,j))

    row_zeroes = set([x[0] for x in zeroes])
    col_zeroes = set([x[1] for x in zeroes])

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in row_zeroes or j in col_zeroes:
                matrix[i][j] = 0

    for row in matrix:
        print(row)

    return

# Determine if s2 is a rotation of s1 using only one call to isSubstring()
def stringRotation(s1,s2):
    if len(s1) != len(s2) or (len(s1) == 0) or (len(s1) == 0):
        print("Not string rotation or strings are empty")

    if isSubstring(s1, s2+s2):
        print("Is string rotation")
    else:
        print("Not string rotation")

    return

# Helper functions
def mergesort(s):
    if len(s) == 1:
        return s
    elif len(s) == 0:
        return ''

    first_half = mergesort(s[0:int(len(s)/2)])
    second_half = mergesort(s[int(len(s)/2):])

    combined = ''
    first_idx = 0
    second_idx = 0

    while (first_idx < len(first_half) or second_idx < len(second_half)):
        if first_idx == len(first_half):
            combined += second_half[second_idx:]
            break
        elif second_idx == len(second_half):
            combined += first_half[first_idx:]
            break

        if first_half[first_idx] < second_half[second_idx]:
            combined += first_half[first_idx]
            first_idx += 1
        else:
            combined += second_half[second_idx]
            second_idx += 1

    return combined

def createImageMatrix(n):
    new_matrix = [[i+(j*n) for i in range(n)] for j in range(n)]
    # for row in new_matrix:
    #     print(row)

    return new_matrix

def createMatrix():
    return [
        [1,3,4,5,7],
        [7,4,2,2,5],
        [0,3,2,0,5],
        [1,2,4,7,9],
        [1,1,2,4,0]
    ]

# returns true if s1 is a substring of s2, false otherwise
def isSubstring(s1, s2):
    pass

if __name__ == "__main__":
    # isUnique("tesfjbm")
    # checkPermutation("test string", "string test")
    # urlify("Mr John Smith    ", 13)
    # palindromePermutation("Tasct Coa")
    # oneAway("pale", "bake")
    # stringCompression("aabcccccaaa")
    # rotateImage(createImageMatrix(5))
    zeroMatrix(createMatrix())
