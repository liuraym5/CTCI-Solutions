from collections import *

# 1.1: Is Unique
# O(n)
def isUnique(string):
    s = set()
    for char in string:
        if char in s:
            return False
        else:
            s.add(char)
    return True

# 1.2: Check Permutation
# O(n)
def checkPerm(s1, s2):
    if len(s1) != len(s2):
        return False
    else:
        c = Counter(s1)
        for char in s2:
            if c[char] == 0:
                return False
            else:
                c[char] -= 1
        return True

# 1.3: URLify
# O(n)
def urlify(string, length):
    string = string[:length]
    index = 0
    while index < length:
        if string[index] == ' ':
            string = string[:index] + "%20" + string[index+1:]
            length += 2
            index += 3
            continue
        index += 1
    return string[:length]

# 1.4: Palindrome Permutation
# O(n)
def isPalindromePermutation(string):
    # A permutation of a palindrome would have each character appearing an even number of times if string is of even
    # length. If string is of odd length then every character except one character would appear an even number of times.
    c = Counter()
    numSpaces = 0
    # adding each letter of the string into a Counter
    for char in string:
        if char == ' ':
            numSpaces += 1
        else:
            c[char] += 1
    # checking if conditions are satisfied
    odd_flag = False
    for value in c.values():
        if value % 2 == 1:
            if odd_flag is True:
                return False
            odd_flag = True
    if (len(string) % 2 == 0 and odd_flag is False) or (len(string) % 2 == 1):
        return True
    return False

# 1.5: One Away
# O(n)
def oneAway(s1, s2):
    # 0 edits
    if s1 == s2:
        return True
    # otherwise check if 1 edit away
    if abs(len(s1) - len(s2)) > 1:
        return False
    temp = ""
    for i, v in enumerate(s1):
        # Check if adding a character in s2 will make strings equal.
        temp = s2[:i] + v + s2[i:]
        if s1 == temp:
            return True
        # Check if deleting a character in s2 will make strings equal.
        temp = s2[:i] + s2[i+1:]
        if s1 == temp:
            return True
        # Check if replacing a character in s2 will make strings equal.
        temp = s2[:i] + v + s2[i+1:]
        if s1 == temp:
            return True
    return False

# 1.6: String Compression
# O(n)
def stringComp(string):
    new = ''
    current_char = string[0]
    amt = 0
    for c in string:
        if current_char != c:
            new += current_char + str(amt)
            current_char = c
            amt = 0
        amt += 1
    new += current_char + str(amt)
    if len(new) < len(string):
        return new
    return string

# 1.7: Rotate Matrix
# O(n^2)
def rotateMatrix(matrix):
    # [[a b c]          [[g d a]
    #  [d e f]    ->     [h e b]
    #  [g h i]]          [i f c]]
    n = len(matrix)
    rotatedM = [[None for i in range(n)] for i in range(n)]
    for j in range(n):
        for i in reversed(range(n)):
            rotatedM[j][n-i-1] = matrix[i][j]
    return rotatedM

# 1.8: Zero Matrix
# O(n^2)
def zeroMatrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    rzeroes = set()
    czeroes = set()
    for i in range(n):
        if i in rzeroes:
            continue
        for j in range(m):
            if j in czeroes:
                continue
            if matrix[i][j] == 0:
                rzeroes.add(i)
                czeroes.add(j)
                break
    for i in range(n):
        for j in range(m):
            if i in rzeroes:
                matrix[i] = [0 for j in range(m)]
                break
            if j in czeroes:
                matrix[i][j] = 0;

# 1.9: String Rotation
def stringRotation(s1, s2):
    l = len(s1)
    if l != len(s2):
        return False
    start = 0
    end = 0
    for i, c in enumerate(s1):
        if s1[:i+1] == s2[l-i-1:] and s1[i+1:] == s2[:l-i-1]:
            return True
    return False