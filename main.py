import pygame as pg 

pg.init()
class Game:
    def __init__(self) -> object:
        window_size: tuple =(300,300)
        pg.display.set_caption("моя играть твоя игра он такая как и твоя")
        self.screen = pg.display.set_mode(window_size)
        self.screen.fill((0, 0, 255))

        pg.display.flip()
            

        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

a = Game()