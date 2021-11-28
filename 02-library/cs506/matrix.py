from functools import reduce
import typing


def get_determinant(matrix: typing.List[typing.List[float]]):
    return determinant_recursive(matrix)


def determinant_recursive(matrix, result=0):
    if len(matrix) == 2 and len(matrix[0]) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

    for index in (list(range(len(matrix)))):
        matrices = [[j for j in i] for i in matrix]
        matrices = matrices[1:]

        for i in range(len(matrices)):
            matrices[i] = matrices[i][0:index] + matrices[i][index+1:]

        result += ((-1) ** (index % 2)) * \
            matrix[0][index] * (determinant_recursive(matrices))

    return int(result)
