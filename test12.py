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
    return (f(x + h) - f(x)) / h


def deriv3(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


def f(x):
    return x ** 2 * log(x)


def fder(x):
    return x * (2. * log(x) + 1)


x = 1
for h in [1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-9]:
    err2 = deriv(f, x, h) - fder(x)
    err3 = deriv3(f, x, h) - fder(x)
    print("%5f -- err2 = %7.4g err3 = %7.4g" % (h, err2, err3))
