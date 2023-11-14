from p205 import time_kruskal, time_kruskal_2
from p205 import greedy_tsp, dist_matrix
from p205 import len_circuit, exhaustive_tsp
import numpy

test = numpy.array([[0,2,1,10,25],[2,0,18,5,5],[1,18,0,20,2],[10,5,20,0,8], [25,5,2,8,0]])
lista = greedy_tsp(test,4)
#time_kruskal(20, 10, 20, 2)
#time_kruskal_2(20, 10, 20, 2)

print(exhaustive_tsp(test))