import pyautogui
import time
import pyperclip
import PySimpleGUI as sg
# image files must be in the same directory!!!
# for debugging -> pyautogui.alert('This is the message to display.')
global contact
contact = ""
# click functions for windows taskbar
def clickRemedy():
    remedy = pyautogui.locateCenterOnScreen("sign_in_images\Remedy_icon.png")
    pyautogui.click(remedy)

def clickCCL():
    edge = pyautogui.locateCenterOnScreen("sign_in_images\edge_icon.png")
    pyautogui.click(edge)
    time.sleep(0.5)
    ccl_page = pyautogui.locateCenterOnScreen("sign_in_images\ccl_page.png",confidence=.5)
    pyautogui.click(ccl_page)

#functions for locating data inside remedy
def moveToFirmAndCopy():
    #first we open remedy
    clickRemedy()
    #moving to firm
    comp = pyautogui.locateCenterOnScreen("sign_in_images\Remedy_comp.png",confidence=0.9)
    pyautogui.click(comp.x+100,comp.y+2)
    pyautogui.rightClick()
    select = pyautogui.locateCenterOnScreen("sign_in_images\select_all.png")
    pyautogui.click(select)
    pyautogui.hotkey('ctrl', 'c')
    global contact
    contact += pyperclip.paste()
    contact += " "

def moveToNameAndCopy():
    clickRemedy()
    Iname = pyautogui.locateCenterOnScreen("sign_in_images\Remedy_name.png",confidence=.8)
    pyautogui.click(Iname.x+150,Iname.y+2)
    pyautogui.rightClick()
    select = pyautogui.locateCenterOnScreen("sign_in_images\select_all.png")
    pyautogui.click(select)
    pyautogui.hotkey('ctrl', 'c')
    global contact
    contact += pyperclip.paste()
    contact += " "

def moveToNumberAndCopy():
    clickRemedy()
    phone = pyautogui.locateCenterOnScreen("sign_in_images\Remedy_phone.png",confidence=.8)
    pyautogui.click(phone.x+10,phone.y+30)
    pyautogui.rightClick()
    select = pyautogui.locateCenterOnScreen("sign_in_images\select_all.png")
    pyautogui.click(select)
    pyautogui.hotkey('ctrl', 'c')
    global contact
    contact += pyperclip.paste()
    contact += " "

#get all data to your clipboard for a sign in 
def signInFromRemedyToNotePad():
    moveToFirmAndCopy()
    moveToNameAndCopy()
    moveToNumberAndCopy()

def signInToCCL():
    clickCCL()
    target = pyautogui.locateCenterOnScreen("sign_in_images\contact_ccl.png",confidence=0.9)
    pyautogui.click(target.x+500,target.y)
    pyperclip.copy(contact)
    pyautogui.hotkey('ctrl', 'v')

def copySiteFromRemedyToCCL():
    clickRemedy()
    target = pyautogui.locateCenterOnScreen("sign_in_images\site_code.png",confidence=0.8)
    pyautogui.click(target.x-200,target.y)
    pyautogui.rightClick(target.x-200,target.y)
    select = pyautogui.locateCenterOnScreen("sign_in_images\select_all.png",confidence=0.8)
    pyautogui.click(select)
    pyautogui.hotkey('ctrl', 'x')
    clickCCL()
    site = pyautogui.locateCenterOnScreen("sign_in_images\ccl_site.png",confidence=0.8)
    pyautogui.click(site.x+400,site.y)
    time.sleep(4)
    site = pyautogui.locateCenterOnScreen("sign_in_images\ccl_page.png",confidence=0.8)
    pyautogui.click(site.x,site.y+400)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(4)
    pyautogui.click(site.x,site.y+490)

def setTimeInCCL():
    clickCCL()
    target = pyautogui.locateCenterOnScreen("sign_in_images\enter_time.png",confidence=0.8)
    pyautogui.click(target.x+160,target.y)
    time.sleep(0.01)
    pyautogui.click(target.x+310,target.y-390)
    pyautogui.click(target.x+310,target.y-40)

#Setting time for the end of pwcut
def closePowerCut1():
    closing_time = pyautogui.prompt(text="",title="Enter the closing time")
    clickCCL()
    target1 = pyautogui.locateCenterOnScreen("pwcut_images\datum.png",confidence=0.8)
    pyautogui.click(target1)
    time.sleep(0.2)
    target2 = pyautogui.locateCenterOnScreen("pwcut_images\datum2.png",confidence=0.8)
    pyautogui.click(target2)
    time.sleep(0.2)
    pyautogui.click(target2.x+30,target2.y+50)
    for i in range(5):
        pyautogui.press('backspace')
    pyautogui.typewrite(closing_time)
    pyautogui.hotkey('enter')
    pyautogui.hotkey('enter')

#Setting closure code, solution and cause
def closePowerCut2():
    target1 = pyautogui.locateCenterOnScreen("pwcut_images\closure_code.png",confidence=0.8)
    pyautogui.click(target1)
    pyautogui.click(target1.x,target1.y+30)
    pyautogui.click(target1.x,target1.y+80)
    target2 = pyautogui.locateCenterOnScreen("pwcut_images\solution.png",confidence=0.8)
    pyautogui.click(target2.x,target2.y+40)
    pyautogui.typewrite("Power supply is back")
    target3 = pyautogui.locateCenterOnScreen("pwcut_images\cause.png",confidence=0.8)
    pyautogui.click(target3.x,target3.y+20)
    pyautogui.typewrite("hard")
    time.sleep(0.5)
    pyautogui.click(target3.x+350,target3.y-380)

#Scrolling down for comment and closing inc
def closePowerCut3():
    pyautogui.scroll(-1000)
    time.sleep(1)
    target1 = pyautogui.locateCenterOnScreen("pwcut_images\enter_comment.png",confidence=0.8)
    pyautogui.click(target1.x,target1.y+50)
    pyautogui.typewrite("Power supply is back")
    target2 = pyautogui.locateCenterOnScreen("pwcut_images\okey.png",confidence=0.8)
    pyautogui.click(target2)
    time.sleep(3)
    target3 = pyautogui.locateCenterOnScreen("pwcut_images\confirm.png",confidence=0.8)
    time.sleep(2)
    pyautogui.click(target3)  #not working properly TODO  

#dif steps for unittest
def closePowerCut():
    closePowerCut1()
    closePowerCut2()
    closePowerCut3()

def closeSiteEntry():
    clickCCL()
    target1 = pyautogui.locateCenterOnScreen("close_se_images\close_site_entry.png",confidence=0.8)
    pyautogui.click(target1)
    time.sleep(0.5)
    target2 = pyautogui.locateCenterOnScreen("close_se_images\datum_cse.png",confidence=0.8)
    pyautogui.click(target2)
    time.sleep(0.5)
    target3 = pyautogui.locateCenterOnScreen("close_se_images\Blabla.png",confidence=0.8)
    pyautogui.click(target3.x-10,target3.y)
    time.sleep(0.5)
    target4 = pyautogui.locateCenterOnScreen("close_se_images\confirm3213.png",confidence=0.8)
    pyautogui.click(target4)
    time.sleep(0.5)
    target5 = pyautogui.locateCenterOnScreen("close_se_images\ok3213.png",confidence=0.8)
    pyautogui.click(target5)
    time.sleep(0.5)
    target6 = pyautogui.locateCenterOnScreen("close_se_images\close3213.png",confidence=0.8)
    pyautogui.click(target6)

def main():
    sg.theme('DarkPurple4')
    layout = [[sg.Text("Choose one!")], 
    [sg.Button("Remedy To Conclusion")],
    [sg.Button("Close Power Cut")],
    [sg.Button("Close Site Entry")],
    [sg.Button("Exit")]]
    window = sg.Window("Kill me", layout, size=(400,300),icon='pwcut_images\sadfrog.ico',)
    # Create an event loop
    while True:
        event, values = window.read()
        if event == "Remedy To Conclusion":
            copySiteFromRemedyToCCL()
            signInFromRemedyToNotePad()
            signInToCCL()
            contact = "" #nem mukszik properly TODO
            setTimeInCCL()
        if event == "Close Power Cut":
            closePowerCut()
        if event == "Close Site Entry":
            closeSiteEntry()
        # End program if user closes window or presses the OK button
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()


if __name__ == '__main__':
    main()

###################
#garbage_collector#
###################
#def clickNotePad():
#    notepad = pyautogui.locateCenterOnScreen("notepad_icon.png")
#    pyautogui.click(notepad)
#copies clipboard content to notepad
#def copyClipboardToNotePad():
#    clickNotePad()
#    time.sleep(0.5)
#    target = pyautogui.locateCenterOnScreen("notepad_target.png",confidence=.8)
#    pyautogui.click(target.x+600,target.y+20)
#    pyautogui.hotkey('ctrl', 'v')
#    pyautogui.press('space')
#####################################
#def copyWorkCodeFromRemedy():
#    clickRemedy()
#    pyautogui.click(1200,270)
#    pyautogui.dragRel(-300, 0, 0.4)
#    pyautogui.hotkey('ctrl', 'x')
#def pasteWorkCodeToCCLAndClickCode():
#    clickCCL()
#    pyautogui.click(500,180)
#    for i in range(15):
#        pyautogui.press('backspace')  
#    pyautogui.hotkey('ctrl', 'v')
#    time.sleep(1)
#    pyautogui.click(450,220)
#def clickEntryOnWorkCode():
#    pyautogui.click(580,700)
#    time.sleep(1)
#   pyautogui.click(540,830)
#def setUPWorkCode():
#    #needs some work only for chr's now
#    copyWorkCodeFromRemedy()
#    pasteWorkCodeToCCLAndClickCode()
#    time.sleep(2) #could be more idk
#    clickEntryOnWorkCode()