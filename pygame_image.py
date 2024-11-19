import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    tmr = 0

     # こうかとん画像を読み込み、左右反転
    kk_img = pg.image.load("fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])#screen  Surface に背景画像surfaceを描画
        screen.blit(kk_img, [300, 200])
        pg.display.update()
        tmr += 1        
        clock.tick(200)#FPSを指定


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()