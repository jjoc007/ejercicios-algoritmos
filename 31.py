#palindromo
#https://www.hackerrank.com/challenges/palindrome-index

def isPalindrome(s):
    n = len(s)

    for i in range(0, n/2 ):
        if s[i] != s[n-i-1]:
            return False

    return True


g =  int(raw_input())


for i in range(0,g):

    word = raw_input()

    if isPalindrome(word):
        print '-1'
    else:
        for j in range(0,len(word)):
            wordAux = word[:j] + word[j+1:]
            print wordAux
            if isPalindrome(wordAux):
                print j
                break