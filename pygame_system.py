import pygame as pg
import sys

def main():
    pg.display.set_caption("はじめてのPygame")
    screen = pg.display.set_mode((800, 600))
    clock = pg.time.Clock()
    font = pg.font.Font(None, 80)

    enn = pg.Surface((20, 20))
    pg.draw.circle(enn, (255, 0, 0), (10, 10), 10) #(赤)(直径)
    enn.set_colorkey((0, 0, 0))

    tmr = 0
    while True: #カウント
        for event in pg.event.get():
            if event.type == pg.QUIT: return #必ず書く(✖で閉じる)
        
        txt = font.render(str(tmr), True, (255, 255, 255))
        screen.fill((50, 50, 50))
        screen.blit(txt, [300, 200]) #画面に貼り付けている
        screen.blit(enn, [100, 400])
        pg.display.update()
        tmr += 1        
        clock.tick(1)#1秒当たり1コマ。カウントアップが丁度1秒


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()