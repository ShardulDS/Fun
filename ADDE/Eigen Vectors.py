import prettytable as pt
import numpy as np
from tkinter import Tk, Label, StringVar, Button, Entry


def main():
    a = np.array([[2, 1, 1],
                  [0, 1, 0],
                  [1, 1, 2]])
    eigen = np.linalg.eig(a)
    b = pt.PrettyTable(border=False, header=False)
    for k in a:
        b.add_row(k)
    print('Matrix')
    print(b)
    b = pt.PrettyTable(border=False)
    b.add_column('Eigen Values', eigen[0])
    print(b)
    b = pt.PrettyTable(border=False)
    for i in range(3):
        b.add_column(f'Eigen vector of X{i+1}', eigen[1][i])
        print(b)
        b = pt.PrettyTable(border=False)


if __name__ == '__main__':
    main()
