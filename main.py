import numpy as np
from simplex import optimize

def main():

    variables = int(input("How many variables? "))
    restrictionsNum = int(input("How many restrictions? ")) + 1
    columns = variables + restrictionsNum
    lines = restrictionsNum
    sizeMatrix = columns * lines
    lpp = np.zeros(sizeMatrix)
    auxArray = []

    print("\nFrom Z:")
    for i in range(variables):
        auxArray.append(-1 * float(input("\t" + str(i+1) + "º coeficient: ")))

    [auxArray.append(0) for k in range(1, restrictionsNum)]
        
    auxArray.append(0)

    for i in range(1, restrictionsNum):
        print("From " + str(i) + "º restriction:" )
        for j in range(variables):
            auxArray.append(float(input("\t" + str(j+1) + "º coeficient: ")))
        for k in range(1, restrictionsNum):
            auxArray.append(1) if k == i else auxArray.append(0)
                
        auxArray.append(float(input("\tThis restriction is <= than: ")))
    
    lpp = np.array(auxArray)
    lpp = lpp.reshape(lines, columns)

    print("\nThis is your LPP matrix: \n" + str(lpp))

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