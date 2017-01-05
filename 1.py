import math

totalPages = float(raw_input())
pageToFound = float(raw_input())

turnsFromBegin = math.ceil((pageToFound - 1) / 2 )
turnsFromLast = int((totalPages - pageToFound) / 2 )

if turnsFromBegin < turnsFromLast:
    print (int(turnsFromBegin))
else:
    print (int(turnsFromLast))
