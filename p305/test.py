import numpy as np
from p305 import qsel, qsel_nr, qsel5_nr, qsort_5
from math import ceil

l = [15, 3, 7, 2, 12, 9, 1, 6, 14, 11, 4, 8, 13, 5, 10 ] 
ls = l.copy()
ls.sort()

l2 = np.array(l)
'''
for i in range(len(l)):
    
    a = qsel5_nr(l2, i)
    print(ls[i], end="")
    print(", " + str(a))
    print(" ")
    print("--------------------------------- ")
    print(" ")
'''
print(qsort_5(l2))