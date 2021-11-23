import pygame as pyg
import sys
pyg.init()

c_white = (255, 255, 255)
c_grey = (240, 240, 240)
c_black = (0, 0, 0)

def setup():
    #size = pyg.display.get_desktop_sizes()[-1]
    size = (800, 480)
    display = pyg.display.set_mode(size=size, display=1) #flags=pyg.NOFRAME
    display.fill(c_white)
    font = pyg.freetype.SysFont(pyg.freetype.get_default_font(), 20)
    pyg.display.update()
    return display, font, size

def main_loop(display, font, size):
    feed1, feed2 = setup_rect(300, 100, 500, 100)
    #while True:
    pyg.draw.rect(display, c_black, feed1, border_radius=7)
    pyg.draw.rect(display, c_grey, feed2)
    update_box(font, display, feed2, "test")
    pyg.display.update()
    input()
    return

def setup_rect(x, y, width, height):
    rect1 = pyg.Rect((x, y), (width, height))
    rect2 = rect1.copy()
    rect2 = rect2.inflate(-8, -8)
    return rect1, rect2


def update_box(font, display, box, text):
    return font.render_to(display, box, text)




if __name__ == "__main__":
    display, font, size = setup()
    main_loop(display, font, size)
