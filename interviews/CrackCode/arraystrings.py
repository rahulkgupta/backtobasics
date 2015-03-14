#Implement an algorithm to determine if a string has all unique characters. What if you can not use additional data structures?

def unique_char(chars):
    arr = [False] * 256
    for chr in chars:
        if arr[ord(chr)] == True:
            return False
        arr[ord(chr)] = True
    return True


def reverse_str(chars):
    end = len(chars) - 1
    start = 0
    while start < end:
        temp = chars[start]
        chars[start] = chars[end]
        chars[end] = temp
        start = start + 1
        end = end - 1
    print chars

def anagrams(string1, string2):
    arr = [0] * 256
    for chr in string1:
        arr[ord(chr)] = arr[ord(chr)] + 1
    for chr in string2:
        arr[ord(chr)] = arr[ord(chr)] - 1
    for i in range(1, len(arr)):
        if arr[i] != 0:
            return False
    return True

#assuming mat[i] is a row in the matrix
def rotate(mat, n):
    #iterating through columns
    for i in range(0, n/2):
        for j in range(i, n-1-i):
            tl = mat[i][j] 
            tr = mat[j][n-1-i]
            br = mat[n-1-i][n-1-j]
            bl = mat[n-1-j][i]
            mat[i][j] = bl
            mat[j][n-1-i] = tl
            mat[n-1-i][n-1-j] = tr
            mat[n-1-j][i] = br
    print mat

def str_rotation(string1, string2):
    if len(string1) != len(string2):
        return False
    string1 = string1 + string1
    if string1.find(string2) == -1:
        return False
    return True





