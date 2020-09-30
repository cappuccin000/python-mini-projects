import pyautogui
import time


pyautogui.PAUSE = 2.5

pyautogui.press('win')
pyautogui.typewrite("edge",interval=0.1)
pyautogui.typewrite(['enter'])
time.sleep(3)
#link=input("Enter the meeting link:")
pyautogui.hotkey('ctrl','t')
time.sleep(3)
pyautogui.typewrite("https://meet.google.com/sdd-uazh-cmn?authuser=2",interval=0.1)

pyautogui.typewrite(['enter'])
time.sleep(3)
pyautogui.hotkey('ctrl','d')
pyautogui.hotkey('ctrl','e')
time.sleep(6)

joinnow=pyautogui.locateCenterOnScreen('join.png')
time.sleep(3)
pyautogui.click(joinnow)
time.sleep(4)

screen_recorder=pyautogui.locateCenterOnScreen('screen_recorder.png')
time.sleep(3)
pyautogui.click(screen_recorder)

screen=pyautogui.locateCenterOnScreen('screen.png')
time.sleep(3)
pyautogui.click(screen)

system=pyautogui.locateCenterOnScreen('system.png')
time.sleep(3)
pyautogui.click(system)

start=pyautogui.locateCenterOnScreen('start_rec.png')
time.sleep(3)
pyautogui.click(start)

edge_tab=pyautogui.locateCenterOnScreen('edge_tab.png')
time.sleep(3)
pyautogui.click(edge_tab)

meet=pyautogui.locateCenterOnScreen('meet.png')
time.sleep(3)
pyautogui.click(meet)

share=pyautogui.locateCenterOnScreen('share.png')
time.sleep(3)
pyautogui.click(share)



#specify the time of the class



stop=pyautogui.locateCenterOnScreen('stop.png')
time.sleep(3)
pyautogui.click(stop)

save=pyautogui.locateCenterOnScreen('save.png')
time.sleep(3)
pyautogui.click(save)

pyautogui.hotkey('alt','f4')

leave=pyautogui.locateCenterOnScreen('leave.png')
time.sleep(3)
pyautogui.click(leave)

pyautogui.hotkey('alt','f4')

#print(pyautogui.position())
