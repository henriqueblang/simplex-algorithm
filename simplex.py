import numpy as np
import math

def generateVariablesName(matrix, numRows, numColumns):

    lineVariables = []
    columnVariables = []

    lineVariables.append("Z")

    for i in range(numColumns - numRows):
        columnVariables.append(chr(65 + i))

    for i in range(1, numRows):
        lineVariables.append("X" + str(i))
        columnVariables.append("X" + str(i))

    columnVariables.append("LD")

    return lineVariables, columnVariables

def findPivotColumn(matrix, numColumns):
    columnIndex = -1
    highestNegative = 0

    for i in range(numColumns):
        element = matrix[0, i]

        if element < 0 and element < highestNegative:
            highestNegative = element

            columnIndex = i
        
    return columnIndex

def findPivotLine(matrix, numRows, numColumns, pivotColumn):
    lineIndex = -1
    lowestPositive = math.inf

    for i in range(numRows):
        element = matrix[i, numColumns - 1] 
        pivotColumnValue = matrix[i, pivotColumn]

        element = pivotColumnValue == 0 and math.inf or element / pivotColumnValue

        if element > 0 and element < lowestPositive:
            lowestPositive = element

            lineIndex = i

    return lineIndex
        
def hasNegative(matrix, numColumns):
    for i in range(numColumns):
        if matrix[0, i] < 0:
            return True

    return False

def solve(matrix, numRows, numColumns, lineVariables, columnVariables):

    pivotColumnIndex = findPivotColumn(matrix, numColumns)
    pivotLineIndex = findPivotLine(matrix, numRows, numColumns, pivotColumnIndex)

    lineVariableAux = lineVariables[pivotLineIndex]
    lineVariables[pivotLineIndex] = columnVariables[pivotColumnIndex]
    columnVariables[pivotColumnIndex] = lineVariableAux

    pivot = matrix[pivotLineIndex, pivotColumnIndex]

    pivotLine = matrix[pivotLineIndex, :]

    matrix[pivotLineIndex, :] = np.true_divide(pivotLine, pivot) + 1 - 1

    for i in range(numRows):
        if i != pivotLineIndex:
            matrix[i, :] = np.add(matrix[i, :], matrix[pivotLineIndex, :] * matrix[i, pivotColumnIndex] * -1)
        
    if not hasNegative(matrix, numColumns):
        return matrix, lineVariables, columnVariables

    return solve(matrix, numRows, numColumns, lineVariables, columnVariables)

def optimize(matrix):

    optimizedSolution = {}

    numRows = np.size(matrix, 0)
    numColumns = np.size(matrix, 1)

    lineVariables, columnVariables = generateVariablesName(matrix, numRows, numColumns)

    optimalSolution, newLineVariables, newColumnVariables = solve(matrix, numRows, numColumns, lineVariables.copy(), columnVariables.copy())

    zeroVariables = list(set(newLineVariables[1:]) ^ set(columnVariables[0:(numRows - numColumns)]))
    zeroVariables.sort()

    nonZeroVariables = {}
    for i in range(1, numRows):
        nonZeroVariables[newLineVariables[i]] = optimalSolution[i, numColumns - 1]

    optimalValue = optimalSolution[0, numColumns - 1]

    # Python 3.5+
    optimizedSolution["investment"] = {**(dict([(var, 0) for var in zeroVariables])), **(dict([(i, nonZeroVariables[i]) for i in sorted(nonZeroVariables.keys())]))}

    optimizedSolution["shadow"] = dict([(newColumnVariables[i], matrix[0][i]) for i in range(numColumns - numRows, numColumns - 1)])

    optimizedSolution["profit"] = optimalValue

    return optimizedSolution