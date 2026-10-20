def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    a = matrix
    # Your code here
    det = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    if det == 0:
        return None
    di = 1 / det
    i = [[a[1][1] * di, -1 * a[0][1] * di], [-1 * a[1][0]* di, a[0][0]* di]]
    return i
    pass