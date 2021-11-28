import pygame as pyg
import sys
import time

pyg.init()

c_white = (255, 255, 255)
c_grey = (240, 240, 240)
c_black = (0, 0, 0)
days = {"Mon": "Ma", "Tue": "Ti", "Wed": "Ke", "Thu": "To", "Fri": "Pe", "Sat": "La", "Sun": "Su"}
months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12"}
tim = ""
upper_font = pyg.freetype.SysFont("arial", 17)
news_font = pyg.freetype.SysFont("timesnewroman", 20)

testi_lamp = "Sisä: 22.5 C Ulko: -13.4 C"


def setup():
    #size = pyg.display.get_desktop_sizes()[-1]
    size = (800, 480)
    display = pyg.display.set_mode(size=size) #flags=pyg.NOFRAME #display=1
    display.fill(c_white)
    
    pyg.display.update()
    return display, size

def main_loop(display, size):
    feed1, feed2 = setup_rect(280, 100, 500, 100)

    pyg.draw.rect(display, c_black, feed1, border_radius=7)
    pyg.draw.rect(display, c_grey, feed2)
    update_box(news_font, display, feed2, "TeSt")
    pyg.draw.line(display, c_black, (0, 20), (800, 20), 3)
    update_box(upper_font, display, (600, 0), testi_lamp)
    while True:
        clock = time.asctime().split()
        clock[0] = days[clock[0]]
        clock[1] = months[clock[1]]
        update_time(clock, display)

        
        pyg.display.update()
        #input()

def setup_rect(x, y, width, height):
    rect1 = pyg.Rect((x, y), (width, height))
    rect2 = rect1.copy()
    rect2 = rect2.inflate(-6, -6)
    return rect1, rect2


def update_box(font, display, box, text):
    return font.render_to(display, box, text)


def update_time(clock, display):
    display.fill(c_white, rect=(0, 0, 180, 15))
    word = clock[2]+"."+clock[1]+"."+clock[4]+" "+clock[3] 
    tim = word
    update_box(upper_font, display, (0, 0), tim)
    


if __name__ == "__main__":
    display, size = setup()
    main_loop(display, size)
