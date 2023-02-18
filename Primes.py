import math
import time

import matplotlib.pyplot as plt
import numpy as np
from numba import njit

t_0 = time.time()


@njit
def conv_pol_cart(coordinates):
    r = coordinates[0]
    theta = coordinates[1]
    x = 0
    y = 0
    if theta < math.pi / 2:
        x = r / math.sqrt(1 + math.tan(theta) ** 2)
        y = x * math.tan(theta)
    elif theta == math.pi / 2:
        y = r
        x = 0
    elif math.pi / 2 < theta <= math.pi:
        theta = math.pi - theta
        x = -r / math.sqrt(1 + math.tan(theta) ** 2)
        y = -x * math.tan(theta)
    elif math.pi < theta < 3 * math.pi / 2:
        theta -= math.pi
        x = -r / math.sqrt(1 + math.tan(theta) ** 2)
        y = x * math.tan(theta)
    elif theta == 3 * math.pi / 2:
        y = -r
        x = 0
    elif 3 * math.pi / 2 < theta <= 2 * math.pi:
        theta = 2 * math.pi - theta
        x = r / math.sqrt(1 + math.tan(theta) ** 2)
        y = -x * math.tan(theta)
    elif theta > 2 * math.pi:
        while theta > 2 * math.pi:
            theta -= 2 * math.pi
        return conv_pol_cart([r, theta])
    return [x, y]


def primesList(n):
    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    primes = []
    for l in range(2, n + 1):
        if prime[l]:
            primes.append(l)
    return primes


numbers = 100000
allPrimes = primesList(numbers)
x_coordinates = []
y_coordinates = []
x_coordinates_comp = []
y_coordinates_comp = []
for k in range(numbers + 1):
    cartesian_coordinates = conv_pol_cart(np.array([k, k]))
    if k in allPrimes:
        x_coordinates.append(cartesian_coordinates[0])
        y_coordinates.append(cartesian_coordinates[1])
    else:
        x_coordinates_comp.append(cartesian_coordinates[0])
        y_coordinates_comp.append(cartesian_coordinates[1])

size_primes = [j for j in np.linspace(1, 5, len(x_coordinates))]
size_comp = [m for m in np.linspace(1, 5, len(x_coordinates_comp))]
plt.style.use('dark_background')
plt.rcParams["figure.figsize"] = 22, 10
plt.scatter(x_coordinates_comp, y_coordinates_comp, size_comp, 'yellow')
plt.scatter(x_coordinates, y_coordinates, size_primes, 'green')
plt.gca().set_aspect("equal")
t_1 = time.time()
print(t_1 - t_0)
plt.show()
