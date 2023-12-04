import numpy as np
from p305 import qsel, qsel_nr, qsel5_nr

l = [15, 3, 7, 2, 12, 9, 1, 6, 14, 11, 4, 8, 13, 5, 10 ] 
ls = l.copy()
ls.sort()
k=0
print(ls[k], ls)

l2 = np.array(l)

a = qsel5_nr(l2, k)
print(a)
print(l2)