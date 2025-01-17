import numpy as np
import matplotlib.pyplot as plt


# 定义蜂群优化算法（Artificial Bee Colony）
class ABC:
    def __init__(self, num_bees, num_iterations, problem_size):
        self.num_bees = num_bees
        self.num_iterations = num_iterations
        self.problem_size = problem_size
        self.lower_bound = 0  # 问题的下边界
        self.upper_bound = 1  # 问题的上边界
        self.position = np.random.uniform(self.lower_bound, self.upper_bound, (self.num_bees, self.problem_size))
        self.fitness = np.zeros(self.num_bees)

    def evaluate_fitness(self):
        """评估每个蜂群个体的适应度"""
        for i in range(self.num_bees):
            self.fitness[i] = self._fitness_function(self.position[i])

    def _fitness_function(self, x):
        """一个简单的适应度函数，您可以根据实际需求进行修改"""
        return np.sum(x ** 2)  # 这里简单使用平方和，实际可以根据网络性能进行定义

    def search(self):
        """进行蜂群优化的搜索过程"""
        for iteration in range(self.num_iterations):
            self.evaluate_fitness()
            best_bee = np.argmin(self.fitness)
            best_position = self.position[best_bee]
            print(f"Iteration {iteration + 1}: Best Fitness = {self.fitness[best_bee]}")

            # 在每一代后显示蜜蜂位置
            self._update_positions(best_position)
            self.plot_positions(iteration)

    def _update_positions(self, best_position):
        """更新每个蜂群的位置"""
        for i in range(self.num_bees):
            if np.random.rand() < 0.5:
                self.position[i] = self.position[i] + np.random.uniform(-1, 1, self.problem_size)
            else:
                self.position[i] = best_position + np.random.uniform(-1, 1, self.problem_size)

    def plot_positions(self, iteration):
        """绘制当前蜜蜂位置"""
        plt.clf()  # 清除当前的图像
        plt.scatter(self.position[:, 0], self.position[:, 1], color='red')
        plt.title(f"Bee Colony Positions - Iteration {iteration + 1}")
        plt.xlabel("Resource 1")
        plt.ylabel("Resource 2")
        plt.xlim(self.lower_bound, self.upper_bound)
        plt.ylim(self.lower_bound, self.upper_bound)
        plt.draw()  # 实时绘制图形
        plt.pause(0.5)  # 暂停 0.1 秒以便显示


# 仿真参数
num_bees = 30
num_iterations = 50
problem_size = 2  # 假设有两个资源变量

# 创建并运行蜂群优化算法
abc = ABC(num_bees, num_iterations, problem_size)
plt.figure()  # 创建图形窗口
abc.search()

plt.show()  # 在所有迭代完成后展示最终的图形
