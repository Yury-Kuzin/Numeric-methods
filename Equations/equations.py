def dichotomy(f, a, b, epsilon=.0001):
    while (b - a) > epsilon:
        c = (a + b) / 2
        a, b = (a, c) if f(a) * f(c) < 0.0 else (c, b)
    return (a + b) / 2


def chords(f, a, b, epsilon=0.1):
    while True:
        x = -(f(a) * (b - a)) / (f(b) - f(a)) + a
        y = f(x)
        if epsilon > abs(y):
            return x
        elif f(a) * y < 0:
            b = x
        else:
            a = x


def brute_force(f, a, b, step=0.1):
    x_min = a
    y_min_abs = abs(f(a))
    x = a + step
    while x < b:
        y = abs(f(x))
        if y < y_min_abs:
            x_min = x
            y_min_abs = y
        x += step
    return x_min


def newton(f, f_d, x, epsilon=0.1):
    while True:
        x -= f(x) / f_d(x)
        if epsilon > abs(f(x)):
            return x


