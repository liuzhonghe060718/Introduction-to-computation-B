import numpy as np
import matplotlib.pyplot as plt

# 参数设置
num_devices = 20  # 网络设备数量
num_resources = 10  # 资源块数量
iterations = 50  # 迭代次数
bees = 30  # 蜂群数量

# 初始化资源需求矩阵 (每个设备对资源块的需求)
np.random.seed(42)
demand_matrix = np.random.randint(1, 5, size=(num_devices, num_resources))


# 定义目标函数: 资源利用率 (利用资源数/总需求)
def calculate_utilization(assignment, demand_matrix):
    assigned_resources = np.sum(np.min(np.stack([assignment, demand_matrix], axis=0), axis=0), axis=0)
    utilization = np.sum(assigned_resources) / np.sum(demand_matrix)
    return utilization


# 初始化蜂群
def initialize_population(bees, num_devices, num_resources):
    return [np.random.randint(0, 2, size=(num_devices, num_resources)) for _ in range(bees)]


# 更新蜜蜂 (基于随机扰动优化)
def update_bees(bee, demand_matrix):
    new_bee = bee.copy()
    rand_device = np.random.randint(0, bee.shape[0])
    rand_resource = np.random.randint(0, bee.shape[1])
    new_bee[rand_device, rand_resource] ^= 1  # 翻转0或1
    if calculate_utilization(new_bee, demand_matrix) > calculate_utilization(bee, demand_matrix):
        return new_bee
    return bee


# 蜂群优化算法
def abc_optimization(demand_matrix, bees, iterations):
    population = initialize_population(bees, demand_matrix.shape[0], demand_matrix.shape[1])
    best_solution = max(population, key=lambda bee: calculate_utilization(bee, demand_matrix))

    history = []
    for _ in range(iterations):
        for i in range(bees):
            population[i] = update_bees(population[i], demand_matrix)
        current_best = max(population, key=lambda bee: calculate_utilization(bee, demand_matrix))
        if calculate_utilization(current_best, demand_matrix) > calculate_utilization(best_solution, demand_matrix):
            best_solution = current_best
        history.append(calculate_utilization(best_solution, demand_matrix))
    return best_solution, history


# 执行实验
best_allocation, utilization_history = abc_optimization(demand_matrix, bees, iterations)

# 随机分配对比
random_allocation = np.random.randint(0, 2, size=(num_devices, num_resources))
random_utilization = calculate_utilization(random_allocation, demand_matrix)

# 输出结果
print("ABC优化后的资源利用率:", calculate_utilization(best_allocation, demand_matrix))
print("随机分配的资源利用率:", random_utilization)

# 可视化结果
plt.figure(figsize=(10, 6))
plt.plot(utilization_history, label="ABC Optimization")
plt.axhline(random_utilization, color='r', linestyle='--', label="Random Allocation")
plt.xlabel("Iterations")
plt.ylabel("Resource Utilization")
plt.title("Resource Utilization: ABC Optimization vs Random Allocation")
plt.legend()
plt.grid()
plt.show()
