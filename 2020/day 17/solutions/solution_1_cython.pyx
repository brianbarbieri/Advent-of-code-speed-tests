cimport numpy as np
import numpy as np
cimport cython

ctypedef np.int_t DTYPE_t

@cython.boundscheck(False) # turn off bounds-checking for entire function
@cython.wraparound(False)  # turn off negative index wrapping for entire function
cpdef np.ndarray[DTYPE_t, ndim=3] change_states_p1(np.ndarray[DTYPE_t, ndim=3] a):
    cdef np.ndarray[DTYPE_t, ndim=3] new_state
    cdef int i, j, k

    new_state = np.zeros((a.shape[0], a.shape[1], a.shape[2]), dtype=np.int)
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            for k in range(a.shape[2]):
                kernel_value = a[max(0,i-1):min(a.shape[0], i+2),max(0,j-1):min(a.shape[1], j+2),max(0,k-1):min(a.shape[2], k+2)].sum() - a[i,j,k] 
                if a[i,j,k] == 1: # if active
                    if kernel_value in [2, 3]:
                        new_state[i,j,k] = 1
                    else:
                        new_state[i,j,k] = 0
                else: # if not active
                    if kernel_value == 3:
                        new_state[i,j,k] = 1
                    else:
                        new_state[i,j,k] = 0
    return new_state

@cython.boundscheck(False) # turn off bounds-checking for entire function
@cython.wraparound(False)  # turn off negative index wrapping for entire function
cpdef np.ndarray[DTYPE_t, ndim=4] change_states_p2(np.ndarray[DTYPE_t, ndim=4] a):
    cdef np.ndarray[DTYPE_t, ndim=4] new_state
    cdef int i, j, k, l

    new_state = np.zeros((a.shape[0], a.shape[1], a.shape[2], a.shape[3]), dtype=np.int)
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            for k in range(a.shape[2]):
                for l in range(a.shape[3]):
                    kernel_value = a[max(0,i-1):min(a.shape[0], i+2),max(0,j-1):min(a.shape[1], j+2),max(0,k-1):min(a.shape[2], k+2),max(0,l-1):min(a.shape[3], l+2)].sum() - a[i,j,k,l] 
                    if a[i,j,k,l] == 1: # if active
                        if kernel_value in [2, 3]:
                            new_state[i,j,k,l] = 1
                        else:
                            new_state[i,j,k,l] = 0
                    else: # if not active
                        if kernel_value == 3:
                            new_state[i,j,k,l] = 1
                        else:
                            new_state[i,j,k,l] = 0
    return new_state