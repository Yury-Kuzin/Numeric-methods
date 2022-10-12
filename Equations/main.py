import matplotlib.pyplot as plot
import equations


# (x - 5)^3 - 4 = 0
def f(x): return (x - 5)**3 - 4


a, b = 3, 9

x_array = []
y_array = []
x = a
while x < b:
    x_array.append(x)
    y_array.append(f(x))
    x += 0.1
plot.plot(x_array, y_array)
plot.show()

print(f"Метод грубой силы (перебора) = {equations.brute_force(f, a, b)}")
print(f"Метод хорд = {equations.chords(f, a, b)}")
print(f"Метод дихотомии = {equations.dichotomy(f, a, b)}")
