import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_imgs = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img = pg.transform.flip(bg_imgs, True, False)
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_imgs = [kk_img, pg.transform.rotozoom(kk_img, 10, 1.0)]
    tmr = 0
    num = 0
    x = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        x = num % 3200
        y = tmr % 250
        z = 0
        tmr += 1
        num += 1
        if 0 <= y <= 125:
            z = 0
        else:
            z = 1
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_imgs, [1600-x, 0])
        screen.blit(bg_img, [3200-x, 0])
        screen.blit(kk_imgs[z], [300, 200])
        pg.display.update()       
        clock.tick(500)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()