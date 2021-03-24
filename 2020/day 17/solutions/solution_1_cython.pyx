# full function
cimport numpy as np
import numpy as np

cpdef np.ndarray change_states_p1(np.ndarray a):
    cdef np.ndarray new_state
    cdef int i, j, k

    new_state = np.zeros((a.shape[0], a.shape[1], a.shape[2]))
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

cpdef np.ndarray change_states_p2(np.ndarray a):
    cdef np.ndarray new_state
    cdef int i, j, k, l

    new_state = np.zeros((a.shape[0], a.shape[1], a.shape[2], a.shape[3]))
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