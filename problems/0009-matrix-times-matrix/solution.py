def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    #dim check, for a and b are mtx of size m x n
    a_n = len(a[0])
    b_m = len(b)
    if a_n != b_m:
        return -1

    #matrixmul one cell at a time
    c = []

    
    for rowIndex_a in range(len(a)):
        row_c = []
        for colIndex_b in range(len(a[0])):
            dot = 0
            for k in range(len(b[0])):
                dot += a[rowIndex_a][k] * b[k][colIndex_b]
            row_c.append(dot)
        c.append(row_c)
            
    return c
