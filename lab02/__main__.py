import matplotlib.pyplot as plt

from lab01 import utils

if __name__ == '__main__':

    # Initial data
    V = 1
    D = 0.1
    T = 5
    L = 10
    print("input Peclet's number")
    Pe = float(input())
    print("input Courant's number")
    Ku = float(input())

    h = D / V * Pe
    tau = h / V * Ku
    n = int(L / h + 1)
    n1 = int(T / tau + 1)
    DL = (n - 1) * h
    TT = (n1 - 1) * tau

    # Print init data
    print(f"V = {V}\nD = {D} \nDL = {DL}\nh = {h}\ntau = {tau}\nTT = {TT}\n")

    y = [0. for _ in range(n)]
    y[1] = 1
    ZD = D / (h ** 2)
    n11 = n1 - 1
    a = [0. for _ in range(n)]
    b = [0. for _ in range(n)]
    c = [1. for _ in range(n)]
    f = [0. for _ in range(n)]
    f[0] = 1  # utils.damb1(t1)
    for i in range(0, n11):
        t1 = i * tau
        for j in range(1, n - 1):
            a[j] = ZD + V / (h * 2.)
            b[j] = ZD - V / (h * 2.)
            c[j] = a[j] + b[j] + 1. / tau
            f[j] = y[j] / tau
        y = utils.tdma(a, b, c, f, n)
    f[n - 1] = 0  # utils.damb0(t1)

    x = [x / n * 10 for x in range(n)]

    x_t = [x / 10.0 for x in range(100)]
    y_t = [utils.precise_solution(x / 10.0, T, V, D) for x in range(100)]
    plt.xlabel('$x$')
    plt.ylabel('$t$')
    plt.plot(x, y, "r+")
    plt.plot(x_t, y_t)
    plt.show()

    # Чисельний розв'язок
    # input pecle's number pe = V*h/D
    # input current number cu = V*tau/h
