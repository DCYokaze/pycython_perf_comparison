# cython: language_level=3
# distutils: language = c++
from libcpp.vector cimport vector

cpdef int count_increases_cpp(list depths):
    cdef int increase_counter, current_depth, depth
    current_depth = depths[0]
    increase_counter = 0
    for depth in depths[1:]:
        if depth > current_depth:
            increase_counter += 1
        current_depth = depth
    return increase_counter

