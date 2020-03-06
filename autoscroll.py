import webbrowser
import time
import keyboard
import mouse

URL = "https://shackla.github.io/InformaTV/"
PAUSE = 0.01
LIMIT = 8000

class AutoScroll:

    def openPage(URL):
        webbrowser.open(URL,new=0, autoraise=True)
        keyboard.press("F11")
        keyboard.release("F11")

    def scrollDown():
        mouse.move(10,10,absolute=False,duration=1)
        for i in range(1,LIMIT):
            mouse.wheel(-0.01)
            time.sleep(PAUSE)
            print("Down")

    def scrollUp():
        for i in range(1,LIMIT):
            mouse.wheel(0.01)
            time.sleep(PAUSE)
            print("Up")



if __name__ == "__main__":
    AutoScroll.openPage(URL)
    while True:
        AutoScroll.scrollDown()
        time.sleep(PAUSE)
        AutoScroll.scrollUp()
        time.sleep(PAUSE)
