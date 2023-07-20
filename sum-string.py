def string_sum(str1, str2):
 
    if (len(str1) < len(str2)):
        str1, str2 = str2,str1
 
    m = len(str1)
    n = len(str2)
    ans = ""
 
    # sum the str2 with str1
    carry = 0
    for i in range(n):
 
        # Sum of current digits
        ds = ((ord(str1[m - 1 - i]) - ord('0')) +
                (ord(str2[n - 1 - i]) - ord('0')) +
                carry) % 10
 
        carry = ((ord(str1[m - 1 - i]) - ord('0')) +
                (ord(str2[n - 1 - i]) - ord('0')) +
                carry) // 10
 
        ans = str(ds) + ans
 
    for i in range(n,m):
        ds = (ord(str1[m - 1 - i]) - ord('0') +
                carry) % 10
        carry = (ord(str1[m - 1 - i]) - ord('0') +
                carry) // 10
        ans = str(ds) + ans
 
    if (carry):
        ans = str(carry) + ans
    return ans
 
# Returns True if two substrings of given
# lengths of str[beg..] can cause a positive
# result.
def checkSumStrUtil(Str, beg,len1, len2):
 
    # Finding two substrings of given lengths
    # and their sum
    s1 = Str[beg: beg+len1]
    s2 = Str[beg + len1: beg + len1 +len2]
    s3 = string_sum(s1, s2)
 
    s3_len = len(s3)
 
    # if number of digits s3 is greater than
    # the available string size
    if (s3_len > len(Str) - len1 - len2 - beg):
        return False
 
    # we got s3 as next number in main string
    if (s3 == Str[beg + len1 + len2: beg + len1 + len2 +s3_len]):
 
        # if we reach at the end of the string
        if (beg + len1 + len2 + s3_len == len(Str)):
            return True
 
        # otherwise call recursively for n2, s3
        return checkSumStrUtil(Str, beg + len1, len2,s3_len)
 
    # we do not get s3 in main string
    return False
 
# Returns True if str is sum string, else False.
def isSumStr(Str):
 
    n = len(Str)
 
    # choosing first two numbers and checking
    # whether it is sum-string or not.
    for i in range(1,n):
        for j in range(1,n-i):
            if (checkSumStrUtil(Str, 0, i, j)):
                return True
 
    return False
 
 
# Driver code
print(isSumStr("1212243660"))
print(isSumStr("123456787"))