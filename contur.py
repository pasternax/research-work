import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.tri as tri


df = pd.read_excel('twentypercent.xlsx')

x = df['kpkm'].values
y = df['ka'].values
z_values = []
for n in range(2, 61):
    z = df['Closest Value']
    if n >= 2 and n <= 6:
        z_value = (z - 3300)**2
    if n >= 7 and n <= 12:
        z_value = (z - 6900)**2
    if n >= 13 and n <= 20:
        z_value = (z - 7100)**2
    if n >= 21 and n <= 30:
        z_value = (z - 12500)**2
    if n >= 31 and n <= 60:
        z_value = (z - 10900)**2
    z_values.append(z_value)

z_new = z_values[0] + z_values[5] + z_values[10] + z_values[18] + z_values[28] + z_values[58]

z_min = np.min(z_new)
z_max = np.max(z_new)

# Создание сечений
section_values = np.linspace(z_min, z_max, num=10)

# Построение графика сечений
triang = tri.Triangulation(x, y)

plt.tricontourf(triang, z_values[58], cmap='viridis')

# Настройка цветовой шкалы, меток и заголовка
plt.colorbar()
plt.xlabel('kpkm')
plt.ylabel('ka')
plt.xlim()
plt.ylim()

# Отображение графика
plt.show()
