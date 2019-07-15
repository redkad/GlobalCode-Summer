from gpiozero import LED, Button
from signal import pause
from  time import sleep

red = LED(18)
yel = LED(19)
gre = LED(21)
button = Button(2)

def traffic():
    gre.off()
    yel.on()
    sleep(2)
    yel.off()
    red.on()
    sleep(6)
    red.off()
    yel.on()
    sleep(5)
    yel.off()
    gre.on()

gre.off()

button.when_pressed = traffic

pause()