from arraystrings import *
if unique_char("abcd") == True:
    print "worked"

if unique_char("abcdd") == True:
    print "worked"
else:
    print "not unique"


reverse_str(["h","e", "l", "l", "o"])

if anagrams("abcc", "bcca") == True:
    print "anagrams"
else:
    print "not anagrams"


rotate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 4)

if str_rotation("abcdc", "bcdca") == True:
    print "rotation"
else:
    print "not rotation"

