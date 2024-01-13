import math
import numpy as np
import matplotlib.pyplot as plt

# A recurssive function was design to get fabbonacci number
def fabonacci(n):
    """A function is made called fabonnaci to recursively generate fabonnaci numbers"""
    if (n == 0 or n == 1):
        return n
    else:
        return fabonacci(n - 2) + fabonacci(n - 1)
# A lamda function was made to caliberate the values of the fabonnaci series
log_fab = lambda x : math.log(x+1)
try:
    a = int(input("Enter the number: "))
    lst_1 = [fabonacci(i) for i in range(1, a)]
    # Each elements in the lst_1 as mapped with the lamda function and an array was made
    fabon = np.array(list(map(log_fab,lst_1)))
    # Fabbonacci number array
    # fabo = np.array(lst_1)
    print(fabon)

    # Index number array
    index = np.array([ind for ind in range(len(lst_1))])

    # Quotient of nth term divided by n-1th term numbers array
    lst_2 = [1]
    for x in range(2, len(lst_1)):
        lst_2.append(lst_1[x] / lst_1[x - 1])
    quo = np.array(lst_2)
    print(quo)

    # Difference of nth term divided by n-1th term numbers array
    lst_3 = [0,0]
    for t in range(2, len(lst_2)):
        lst_3.append(lst_2[t] - lst_2[t - 1])
    diff = np.array(lst_3)
    print(diff)

    # Plot labels
    plt.xlabel('Index Numbers')
    plt.ylabel('Values')

    # Plot ticks
    plt.xticks(np.arange(min( index), max(index)+ 4, 2))
    plt.yticks(np.arange(min(fabon), max(fabon)))

    # Plots
    plt.plot(index, fabon, color='blue')
    plt.plot(index[1:], quo, color='orange')
    plt.plot(index[1:], diff, color='green')
    plt.legend(['Log of Fabonnaci numbers', 'Quotient of Fabonnaci numbers', 'Difference of Quotient of Fabonnaci numbers'],
               fontsize='10', loc='best')
    print("\nThe graphs of quotient and difference will not converge")
    plt.show()
except ValueError:
    print("Kindly enter integer number !!!")
