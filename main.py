import numpy as np
import matplotlib.pyplot as plt

def plot_signals(x, y1, y2, title):
    plt.figure(figsize=(8, 4))
    plt.plot(x, y1, label='Початковий сигнал')
    plt.plot(x, y2, label='Сигнал з реверсом')
    plt.title(title)
    plt.xlabel('Час')
    plt.ylabel('Значення')
    plt.legend()
    plt.grid(True)
    plt.show()

# Створення початкового сигналу
t = np.linspace(0, 10, 1000)
original_signal = np.sin(t)  # Приклад початкового сигналу (синусоїди)

# Реверс сигналу (догори донизу)
reversed_signal = original_signal[::-1]

# Показ початкового сигналу та сигналу з реверсом
plot_signals(t, original_signal, reversed_signal, 'Реверс по часу')
