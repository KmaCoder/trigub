import matplotlib.pyplot as plt

from lab01 import utils

if __name__ == '__main__':
    V = 1
    D = 0.1
    T = 5

    x_t = [x / 10.0 for x in range(100)]
    y_t = [utils.precise_solution(x / 10.0, T, V, D) for x in range(100)]
    plt.xlabel('$x$')
    plt.ylabel('$t$')
    plt.plot(x_t, y_t)
    plt.show()
