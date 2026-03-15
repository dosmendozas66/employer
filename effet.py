from turtle import *
from colorsys import *


def afficher_effet(duree_ms=3000):
    bgcolor("black")
    speed(0)

    h = 0

    for i in range(200):
        h += 0.0015
        color(hsv_to_rgb(h, 1, 1))
        goto(0, 0)
        fd(i)
        circle(100, 50)
        rt(10)
        hideturtle()

    ontimer(bye, duree_ms)
    done()


if __name__ == "__main__":
    afficher_effet()
