g =  int(raw_input())

for i in range(0,g):

    word = raw_input()
    abre = raw_input()
    wordUpper = word.upper()

    if abre in wordUpper:
        print 'YES'
    else:
        print 'NO'
