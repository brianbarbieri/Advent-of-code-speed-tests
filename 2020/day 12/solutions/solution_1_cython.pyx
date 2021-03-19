from libc.math cimport abs  

cpdef double part_2(instructions):
    cdef int x_w, y_w, x_s, y_s
    x_w, y_w, x_s, y_s = 10, 1, 0, 0

    cdef int i, d
    cdef str x
    for i in range(len(instructions)):
        x, d = instructions[i][0], instructions[i][1]
        if x == "L":
            if d == 90:
                x_w, y_w = -y_w, x_w
            elif d == 180:
                x_w, y_w = -x_w, -y_w
            elif d == 270:
                x_w, y_w = y_w, -x_w
        elif x == "R":
            if d == 90:
                x_w, y_w = y_w, -x_w
            elif d == 180:
                x_w, y_w = -x_w, -y_w
            elif d == 270:
                x_w, y_w = -y_w, x_w
        elif x == "F":
            x_s += x_w * d
            y_s += y_w * d
        elif x == "N":
            y_w += d
        elif x == "W":
            x_w -= d
        elif x == "S":
            y_w -= d
        elif x == "E":
            x_w += d
    return abs(x_s) + abs(y_s)