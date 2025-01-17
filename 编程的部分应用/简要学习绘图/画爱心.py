import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 爱心的参数化方程
def heart_shape(t):
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    return x, y

# 绘制爱心
t = np.linspace(0, 2 * np.pi, 1000)
x, y = heart_shape(t)

# 初始化绘图
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)
ax.axis("off")

# 爱心路径和填充
heart_line, = ax.plot([], [], color='red', lw=2)
heart_fill = ax.fill([], [], color='pink', alpha=0.5)[0]

# 添加文字
text = ax.text(0, 0, "Love Python", color="white", fontsize=16,
               ha="center", va="center", fontweight="bold")

# 动画更新函数
def update(frame):
    scale = 1 + 0.1 * np.sin(frame / 10)  # 让爱心跳动
    x_scaled = x * scale
    y_scaled = y * scale
    heart_line.set_data(x_scaled, y_scaled)
    heart_fill.set_xy(np.column_stack((x_scaled, y_scaled)))
    return heart_line, heart_fill

# 动画对象
ani = FuncAnimation(fig, update, frames=np.arange(0, 200), interval=50, blit=True)

# 显示动画
plt.show()
