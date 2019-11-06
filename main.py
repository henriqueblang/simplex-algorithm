import numpy as np
from simplex import optimize

def main():

    variables = int(input("How many variables? "))
    restrictionsNum = int(input("How many restrictions? "))+1
    columns = variables + restrictionsNum
    lines = restrictionsNum
    sizeMatrix = columns * lines
    lpp = np.zeros(sizeMatrix)
    auxArray = []

    for i in range(lines):
        for j in range(columns):
            value = float(input("Value [" + str(i+1) + "][" + str(j+1) + "]: "))
            auxArray.append(value)

    lpp = np.array(auxArray)
    lpp = lpp.reshape((lines, columns))

    '''
    [-5, -7, -8, 0, 0, 0],
    [1, 1, 2, 1, 0, 1190],
    [3, 4.5, 1, 0, 1, 4000]
    '''
    
    # Output optimization
    solution = optimize(lpp)

    print("\n\n** Optimal profit")
    print("\tZ*: R$ " + str(solution["profit"]))

    print("** Best investment")
    for decisionVariable in solution["investment"].items():
        print("\t" + decisionVariable[0] + "*: R$", decisionVariable[1])

    print("** Shadow price")
    for auxVariable in solution["shadow"].items():
        print("\t" + auxVariable[0] + "*: R$", auxVariable[1])


if __name__ == "__main__":
    main()