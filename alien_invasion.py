from pygame import *
import pygame
from pygame.sprite import Group

from scoreboard import Scoreboard
from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    pygame.mixer.init(channels=0)
    pygame.mixer.init(channels=1)
    pygame.mixer.init(channels=2)
    pygame.mixer.init(channels=3)
    pygame.mixer.init(channels=4)

    back_sound = pygame.mixer.Sound("music/back.wav")
    pygame.mixer.Channel(0).play(back_sound)

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )

    # 设置标题
    pygame.display.set_caption("外星人入侵")

    # 创建开始按钮
    play_button = Button(ai_settings, screen, "PLAY")

    # 创建一艘飞船、一个用于存储子弹的编组和一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建一个用于存储游戏统计信息的实例,并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 开始游戏循环
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()
