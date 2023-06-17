import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import matplotlib.tri as tri

df = pd.read_excel('Mn_values2.xlsx')

x = df['kpkm'].values
y = df['ka'].values
z_values = []
for n in range(2, 61):
    z = df[f'time {n}']
    print(z)
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
print(z_values[0])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
triang = tri.Triangulation(x, y)
plt.tricontourf(triang, z_new, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D')


def update(frame):
    ax.clear()
    ax.set_xlabel('kpkm')
    ax.set_ylabel('ka')
    ax.set_zlabel('Z')
    ax.set_zlim(min(z_values[frame]), max(z_values[frame]))
    ax.set_xlim(x.min(), x.max())
    ax.set_ylim(y.min(), y.max())
    ax.set_title(f'график при {z_values[frame].name}')
    ax.autoscale(enable=False, axis='both')
    surf = ax.plot_trisurf(x, y, z_values[frame])


animation = FuncAnimation(fig, update, frames=len(z_values), interval=500, repeat=True)
plt.show()