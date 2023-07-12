import numpy as np


def computeKnapsackProblemDynamicProgramming(listOfValues=[1,6,18,22,28], listOfWeights=[1,2,5,6,7], maxCapacity=11, n=5):
    K = np.array([[0 for x in range(maxCapacity + 1)] for x in range(n + 1)])

    for it in range(n + 1):
        for cap in range(maxCapacity + 1):
            if it == 0 or cap == 0:
                K[it][cap] = 0
            elif listOfWeights[it - 1] <= cap:
                K[it][cap] = max(listOfValues[it - 1] + K[it - 1][cap - listOfWeights[it - 1]], K[it - 1][cap])
            else:
                K[it][cap] = K[it - 1][cap]

    return K[n][maxCapacity]
print("Solução otima é: ",computeKnapsackProblemDynamicProgramming())