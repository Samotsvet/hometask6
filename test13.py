from math import log

def deriv(f, x, h):
    """ Вычисляет производную `f` в точке `x` с шагом `h`.
    Вычисляет производную, используя односторонню разностную схему со степенью аппроксимации $O(h^2)$.

    Parameters
    ----------
    f : callable
        Функция, которую нужно продифференцировать
    x : float
        Точка, в которой нужно дифференцировать функцию
    h : float
        Шаг

    Rerurns
    -------
    fder : производная f(x) в точке x с шагом h.
    """
    x0 = x
    x1 = x + h
    x2 = x + (h * 2)
    return (-3 * f(x0) + 4 * f(x1) - f(x2)) / (2 * h)


def f(x):
    if x == 0:
        # предел $x^2 log(x)$ при $x-> 0$ равен нулю, хотя log(x) не определен в x=0
        return 0.0
    else:
        return x ** 2 * log(x)


def fder(x):
    if x == 0:
        return 0.0
    else:
        return x * (2 * log(x) + 1)

x = 0
for h in [1e-2, 1e-3, 1e-4, 1e-5]:
    err = deriv(f, x, h) - fder(x)
    print("%5f -- %7.4g" % (h, err))
