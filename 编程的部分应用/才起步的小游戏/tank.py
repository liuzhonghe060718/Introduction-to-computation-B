import pygame

# 初始化 Pygame
pygame.init()

# 设置窗口大小
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 设置窗口标题
pygame.display.set_caption("坦克大战")

# 主游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 点击关闭按钮
            running = False

    # 填充背景颜色
    screen.fill((0, 0, 0))  # 黑色背景

    # 更新屏幕
    pygame.display.flip()

# 退出游戏
pygame.quit()
