from libc.math cimport abs  

cpdef int part_1(instructions):
        direction = {
            0 : "N",
            90 : "W",
            180 : "S",
            270 : "E"
        }
        cdef int x_s, y_s, a
        x_s, y_s, a = 0, 0, 270

        cdef int i, d
        cdef str x
        for i in range(len(instructions)):
            x, d = instructions[i][0], instructions[i][1]
            if x in ["L",  "R"]:
                if x == "L":
                    a += d
                else:
                    a -= d
                a %= 360
            elif x == "F":
                x = direction[a]
            if x == "N":
                y_s += d
            elif x == "W":
                x_s += d
            elif x == "S":
                y_s -= d
            elif x == "E":
                x_s -= d
        return abs(x_s) + abs(y_s)


cpdef int part_2(instructions):
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