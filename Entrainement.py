import math
import cmath
import matplotlib.pyplot as plt

# Définir les constantes
pi = math.pi
sin = math.sin
cos = math.cos

# Définir la fonction f
def f(t):
    if -10 <= t <= 10:
        return sin(pi * t)
    else:
        return 0

def g(t):
    if -10 <= t <= 10:
        return 2 * cos(3 * pi * t)
    else:
        return 0

def h(t):
    if -10 <= t <= 10:
        return 1.5 * sin(1.5 * pi * t) + 2
    else:
        return 0

def i(t):
    if -10 <= t <= 10:
        return 3 * cos(2 * pi * t) - 1.5 * sin(4 * pi * t)
    else:
        return 0

# Fonction générale pour la transformée de Fourier
def transformee_fourier(func, T):
    def F(omega):
        sum_ = 0
        for t in T:
            sum_ += 0.01 * func(t) * cmath.exp(-1j * omega * t)
        return abs(sum_)
    return F
T = [i * 0.01 for i in range(-1000, 1001)]
fT = [f(t) for t in T]
# Tester les fonctions g, h, et i
functions = [g, h, i]
function_names = ['g', 'h', 'i']

for func, name in zip(functions, function_names):
    fT = [func(t) for t in T]
    plt.plot(T, fT)
    plt.xlabel('t')
    plt.ylabel(f'{name}(t)')
    plt.title(f'Courbe représentative de {name}')
    plt.show()

    F = transformee_fourier(func, T)
    FW = [F(omega) for omega in W]
    plt.plot(W, FW)
    plt.xlabel('omega')
    plt.ylabel(f'{name.upper()}(omega)')
    plt.title(f'Courbe représentative de la transformée de Fourier de {name}')
    plt.show()