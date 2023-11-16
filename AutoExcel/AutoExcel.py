from time import sleep
import pyautogui as pg


pg.hotkey("ctrl", "alt", "e")

sleep(10)
x, y = pg.locateCenterOnScreen("./blank workbook.PNG", confidence=0.9)
pg.moveTo(x, y, 0)
pg.click()

sleep(2)
x, y = pg.locateCenterOnScreen("./Data.PNG", confidence=0.9)
pg.moveTo(x, y, 1)
pg.click()

sleep(3)
x, y = pg.locateCenterOnScreen("./FromTxt.PNG", confidence=0.9)
pg.moveTo(x, y, 1)
pg.click()

sleep(3)
x, y = pg.locateCenterOnScreen("./Desktop.PNG", confidence=0.5)
pg.moveTo(x, y, 1)
pg.click()

sleep(3)
x, y = pg.locateCenterOnScreen("./Sample.PNG", confidence=0.9)
pg.moveTo(x, y, 1)
pg.doubleClick()

sleep(3)
x, y = pg.locateCenterOnScreen("./Next.PNG", confidence=0.9)
pg.moveTo(x, y, 1)
pg.doubleClick()

sleep(2)
x, y = pg.locateCenterOnScreen("./Semicolon.PNG", confidence=0.9)
pg.moveTo(x, y, 1)
pg.click()

sleep(2)
x, y = pg.locateCenterOnScreen("./Comma.PNG", confidence=0.9)
pg.moveTo(x, y, 1)
pg.click()

sleep(2)
x, y = pg.locateCenterOnScreen("./Space.PNG", confidence=0.9)
pg.moveTo(x, y, 1)
pg.click()

sleep(2)
x, y = pg.locateCenterOnScreen("./Next.PNG", confidence=0.9)
pg.moveTo(x, y, 1)
pg.click()

sleep(2)
pg.hotkey("enter")

sleep(2)
pg.hotkey("enter")

sleep(2)
x, y = pg.locateCenterOnScreen("./Insert.PNG", confidence=0.9)
pg.moveTo(x, y, 1)
pg.click()

sleep(6)
x, y = pg.locateCenterOnScreen("./Chart.PNG", confidence=0.9)
pg.moveTo(x, y, 1)
pg.click()

# print(x, y)
# x,y = 20,10
# Select the chart
sleep(2)
x += 10
y += 60
pg.moveTo(x, y, 1)
pg.click()

# print(x, y)

sleep(7)
x, y = pg.locateCenterOnScreen("./Email.PNG", confidence=0.9)
pg.moveTo(x, y, 1)
pg.click()

sleep(10)
pg.write("muwaffaq.elbadawi@gmail.com")

sleep(3)
x, y = pg.locateCenterOnScreen("./Send.PNG", confidence=0.9)
pg.moveTo(x, y, 1)
pg.click()
