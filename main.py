import math
import curses
import time

def julia(x,y,a):
    s = 0
    for iter in range(150):
        if (math.sqrt(x**2 +y**2)>2):
            return s
        else:
            tx = x**2 - y**2 +0.7*math.cos(a)
            y = 2*x*y +0.7*math.sin(a)
            x = tx
            s = iter
    return s


def mapping(n):
    chr = ''
    if n in range(10): chr = '.'
    elif n in range(10, 50): chr = '"'
    elif n in range(50, 80): chr = 'O'
    elif n in range(80, 120): chr = '8'
    elif n >120 : chr = '#'
    return chr



def main(window):
    rows , cols = window.getmaxyx()
    while True:
        for c in range(-600, 600):
            window.clear()
            for j in range(rows-1):
                for i in range(cols-1):
                    tj = ((2*j-rows)/rows)*2
                    ti = ((2*i-cols)/cols)*2
                    t = mapping(julia(ti,tj,c/100)) 
                    window.addstr(j, i ,t)
            window.refresh()
if __name__ == '__main__':
    curses.wrapper(main)
