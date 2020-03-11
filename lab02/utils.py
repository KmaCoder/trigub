from math import exp, sqrt

from scipy import special


def precise_solution(x, t, v, d):
    return 1 / 2 * (special.erfc([(x - v * t) / (2 * sqrt(d * t))])[0] + exp(v * x / d) *
                    special.erfc([(x + v * t) / (2 * sqrt(d * t))])[0])


def tdma(a, b, c, f, n):
    alpha = [0., b[0] / c[0]]
    beta = [0., f[0] / c[0]]
    x = [0 for _ in range(n)]
    for i in range(1, n - 1):
        q = c[i] - a[i] * alpha[i]
        alpha.append(b[i] / q)
        beta.append((f[i] + a[i] * beta[i]) / q)

    x[n - 1] = (f[n - 1] - a[n - 1] * beta[n - 1]) / (c[n - 1] + a[n - 1] * alpha[n - 1])

    for i in reversed(range(n - 1)):
        x[i] = alpha[i + 1] * x[i + 1] + beta[i + 1]

    return x


def damb1(_):
    return 1.


def damb0(_):
    return 0.
