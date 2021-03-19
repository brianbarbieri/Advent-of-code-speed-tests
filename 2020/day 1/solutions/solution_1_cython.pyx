from libc.math cimport abs  

cpdef int part_1(list data):
    cdef int mini, maxi
    mini = 0
    maxi = -1
    while mini != len(data):
        if data[mini] + data[maxi] == 2020:
            return data[mini] * data[maxi]
        elif data[mini] + data[maxi] > 2020:
            maxi -= 1
        else:
            mini += 1

      