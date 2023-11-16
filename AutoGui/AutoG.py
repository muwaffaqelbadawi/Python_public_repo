from time import sleep
import pyautogui as pg

'''
# locate the image on sctreen
res = pg.locateOnScreen("./image.PNG")
print(res)

# get the center coordinate of the image
edit_button = pg.center(res)
print(edit_button)


# locate the center of the image on the screen
pg.locateCenterOnScreen("./image.PNG")

pg.moveTo(edit_button)
'''
# Subscribe to a youtube channel

'''
1. open a new tab on the browser
1. Search youtube.com
3. Search for the channel you want
4. Click on the channel
5. Click on the subscribe button
'''

# a prompt tyo take input
# channel_name = pg.prompt(text="", title="Enter the channel name")
# print(channel_name)

# open new tab
pg.hotkey("ctrl", "alt", "e")
sleep(5)

x, y = pg.locateCenterOnScreen("./blank workbook.PNG", confidence=0.9)
pg.moveTo(x, y, 1)
pg.click()

sleep(2)
pg.hotkey("ctrl", "s")

sleep(2)
x, y = pg.locateCenterOnScreen("./Browse.PNG", confidence=0.9)
pg.moveTo(x, y, 1)
pg.click()

sleep(2)
pg.write("myFile")
x, y = pg.locateCenterOnScreen("./Desktop.PNG", confidence=0.9)
pg.moveTo(x, y, 1)
pg.click()
pg.hotkey("enter")

sleep(2)
x, y = pg.locateCenterOnScreen("./Save.PNG", confidence=0.9)
pg.moveTo(x, y, 1)
pg.click()

x, y = pg.locateCenterOnScreen("./Exit.PNG", confidence=0.9)
pg.moveTo(x, y, 1)
pg.click()

# pg.write("https://www.youtube.com")
# pg.hotkey("enter")
# sleep(10)


# x, y = pg.locateCenterOnScreen("./Search.PNG", confidence=0.9)
# # print(search_bt)
# pg.moveTo(x, y, 1)
# pg.click()

# sleep(3)
# pg.write("edureka!")
# pg.hotkey("enter")


# pg.write("https://www.youtube.com")
# pg.hotkey("enter")
