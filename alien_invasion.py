import sys
import pygame
#导入设置屏幕类
from settings import Settings
#导入飞船类
from ship import Ship
#导入鉴定事件模块
import game_functions as gf
#导入编组类
from pygame.sprite import Group
#导入外星人类
from alien import Alien
#导入游戏统计信息类
from game_status import GameStatus
#导入按钮类
from button import Button
#导入计分类
from scoreboard import Scoreboard

def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	ai_settings = Settings()
	#设置主屏幕的大小
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	#设置游戏的主题
	pygame.display.set_caption("Alien Invasion")
	#创建一艘飞船
	ship = Ship(ai_settings,screen)
	#创建一个用于存储子弹的编组
	bullets = Group()
	#创建一个存储外星人的编组
	aliens = Group()
	#创建外星人群
	gf.create_fleet(ai_settings,screen,ship,aliens)
	#创建一个用户存储游戏统计信息的实例
	status = GameStatus(ai_settings)
	#创建play按钮
	play_button = Button(ai_settings,screen,"Play")
	#创建记分牌
	sb = Scoreboard(ai_settings,screen,status)
	#开始游戏的主循环
	while True:
		#监视键盘和鼠标事件
		gf.check_events(ai_settings,screen,status,sb,play_button,ship,aliens,bullets)
		if status.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,status,sb,ship,aliens,bullets)
			gf.update_aliens(ai_settings,screen,status,sb,ship,aliens,bullets)
		gf.update_screen(ai_settings,screen,status,sb,ship,aliens,bullets,play_button)
		
run_game()
