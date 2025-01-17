import sys
import pygame
from settings import Settings

class AlienInvasion:
    def __init__(self):
        pygame.init()#初始化游戏让模块正常工作
        self.clock=pygame.time.Clock()#控制帧率
        self.settings=Settings()

        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))#创建一个显示窗口
        pygame.display.set_caption("Alien Invasion")

        self.bg_color=(230,230,230)#设置背景色
    def run_game(self):#开始游戏主循环
        while True:
            for event in pygame.event.get():#侦听事件，构建事件循环
                if event.type==pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)   #每次循环重绘屏幕，FILL方法用于处理SURFACE，接受一个颜色实参
            pygame.display.flip()#让最近绘制的屏幕可见
            self.clock.tick(60)#设置帧率，一般动态游戏为60，越高越牛逼
if __name__=='__main__':
    ai=AlienInvasion()
    ai.run_game()