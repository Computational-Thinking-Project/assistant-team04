def transpose(matrix: list[list[int]]) -> list[list[int]]:
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    transposeMatrix = []

    for col in range(cols):
        newRow = []
        for row in range(rows):
            newRow.append(matrix[row][col])
        transposeMatrix.append(newRow)

    return transposeMatrix
