import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simps


def trapezoidal_integration(f, interval):
    n = f.shape[0]
    a, b = interval
    h = (b - a) / n
    sum_sides = 2 * np.sum(f) - f[0] - f[n - 1]
    return h * sum_sides / 2


def fourier_series(func, interval, harmonics):
    a, b = interval
    x = np.linspace(a, b, 1000)
    y = func(x)
    l = (b - a) / 2
    a_0 = simps(y, x) / l
    a_n = lambda n: simps(y * np.cos(n * np.pi * x / l), x)/l
    b_n = lambda n: simps(y * np.sin(n * np.pi * x / l), x)/l
    series = a_0/2 + sum([a_n(k) * np.cos(k * np.pi * x/l) + b_n(k) * np.sin(k * np.pi * x/l) for k in range(1, harmonics + 1)])
    #fig, ax = plt.subplots(2, 2)
    fourier = 0
    actual = 0
    labels = ['Fourier Series', 'Actual Function']
    '''for n in range(1, harmonics + 1):
        a_n = np.trapz(y * np.cos(n * np.pi * x / l), x) * np.cos(n * np.pi * x / l) / l
        b_n = np.trapz(y * np.sin(n * np.pi * x / l), x) * np.sin(n * np.pi * x / l) / l
        series += a_n + b_n
        if 996 <= n <= 999:
            plt.subplot(2, 2, n-995)
            fourier = plt.plot(x, series)
            actual = plt.plot(x, y)
            plt.gca().set_title(f'{n} harmonics')'''
    fourier = plt.plot(x, series)
    actual = plt.plot(x, y)
    plt.gca().set_title(f'1000 harmonics')
    plt.legend([fourier, actual], labels=labels, loc="upper left")
    plt.show()


def a_func(p):
    return p - np.square(p)


def main(func):
    func(a_func, [-np.pi, np.pi], 1000)


if __name__ == '__main__':
    main(fourier_series)
