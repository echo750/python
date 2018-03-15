def findMinAndMax(L):
    if L==[]:
       return (None,None)
    min=L[0]
    max=L[0]
    for i in L:
        if i<min:
           min=i
        if i>max:
           max=i
    return (min,max)

# ≤‚ ‘
if findMinAndMax([]) != (None, None):
    print('≤‚ ‘ ß∞‹!')
elif findMinAndMax([7]) != (7, 7):
    print('≤‚ ‘ ß∞‹!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('≤‚ ‘ ß∞‹!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('≤‚ ‘ ß∞‹!')
else:
    print('≤‚ ‘≥…π¶!')