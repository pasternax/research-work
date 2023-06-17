import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.tri as tri


df = pd.read_excel('z_new.xlsx')
x = df['kpkm'].values
y = df['ka'].values
z_new = df['z_new'].values

# Вычисление порогового значения для выбора 20% наименьших точек
threshold = np.percentile(z_new, 20)

# Создание триангуляции
triang = tri.Triangulation(x, y)
c_values = z_new
# Отображение только 20% наименьших точек
selected_points = np.where(z_new <= threshold)
plt.tripcolor(triang, c_values, cmap='viridis')
plt.colorbar()
plt.triplot(triang, color='0.7')
plt.plot(x[selected_points], y[selected_points], 'ro')

plt.xlabel('kpkm')
plt.ylabel('ka')
plt.title('20% наименьших точек z_new')

plt.show()
