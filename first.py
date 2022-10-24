from asyncio.windows_events import NULL
import pyautogui
import time
import pyperclip
import PySimpleGUI as sg
import traceback
# image files must be in the same directory!!!
# for debugging -> pyautogui.alert('This is the message to display.')
global contact
contact = ""
# click functions for windows taskbar
def clickRemedy():
    try:
        remedy = pyautogui.locateCenterOnScreen("sign_in_images\Remedy_icon.png")
        pyautogui.click(remedy)
    except Exception:
        print(traceback.format_exc())

def clickCCL():
    try:
        edge = pyautogui.locateCenterOnScreen("sign_in_images\edge_icon.png")
        pyautogui.click(edge)
        time.sleep(0.5)
        ccl_page = pyautogui.locateCenterOnScreen("sign_in_images\ccl_page.png",confidence=.5)
        pyautogui.click(ccl_page)
    except Exception:
        print(traceback.format_exc())

#functions for locating data inside remedy
def moveToFirmAndCopy():
    try:
        #first we open remedy
        clickRemedy()
        comp = pyautogui.locateCenterOnScreen("sign_in_images\Remedy_comp.png",confidence=0.9)
        pyautogui.click(comp.x+100,comp.y+2)
        pyautogui.rightClick()
        select = pyautogui.locateCenterOnScreen("sign_in_images\select_all.png")
        pyautogui.click(select)
        pyautogui.hotkey('ctrl', 'c')
        global contact
        contact += pyperclip.paste()
        contact += " "
    except Exception:
        print(traceback.format_exc())

def moveToNameAndCopy():
    try:
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
    except Exception:
        print(traceback.format_exc())

def moveToNumberAndCopy():
    try:
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
    except Exception:
        print(traceback.format_exc())

#get all data to your clipboard for a sign in 
def signInFromRemedyToNotePad():
    moveToFirmAndCopy()
    moveToNameAndCopy()
    moveToNumberAndCopy()

def signInToCCL():
    try:
        clickCCL()
        target = pyautogui.locateCenterOnScreen("sign_in_images\contact_ccl.png",confidence=0.9)
        pyautogui.click(target.x+500,target.y)
        pyperclip.copy(contact)
        pyautogui.hotkey('ctrl', 'v')
    except Exception:
        print(traceback.format_exc())

def copySiteFromRemedyToCCL():
    try:
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
        time.sleep(1)
        site = pyautogui.locateCenterOnScreen("sign_in_images\ccl_page.png",confidence=0.8)
        pyautogui.click(site.x,site.y+400)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.click(site.x,site.y+490)
    except Exception:
        print(traceback.format_exc())

def setTimeInCCL():
    try:
        #clickCCL()
        target = pyautogui.locateCenterOnScreen("sign_in_images\enter_time.png",confidence=0.8)
        pyautogui.click(target.x+160,target.y)
        time.sleep(0.01)
        pyautogui.click(target.x+310,target.y-390)
        pyautogui.click(target.x+310,target.y-40)
        target2 = pyautogui.locateCenterOnScreen("sign_in_images\img_save.png",confidence=0.8)
        pyautogui.moveTo(target2)
    except Exception:
        print(traceback.format_exc())

#Setting time for the end of pwcut
def closePowerCut1():
    try:
        closing_time = pyautogui.prompt(text="",title="Enter the closing time")
        clickCCL()
        target1 = pyautogui.locateCenterOnScreen("pwcut_images\datum.png",confidence=0.8)
        pyautogui.click(target1)
        time.sleep(0.2)
        target2 = pyautogui.locateCenterOnScreen("pwcut_images\datum2.png",confidence=0.7)
        pyautogui.click(target2)
        time.sleep(0.2)
        pyautogui.click(target2.x+30,target2.y+50)
        for i in range(5):
            pyautogui.press('backspace')
        pyautogui.typewrite(closing_time)
        pyautogui.hotkey('enter')
        pyautogui.hotkey('enter')
    except Exception:
        print(traceback.format_exc())

#Setting closure code, solution and cause
def closePowerCut2():
    try:
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
    except Exception:
        print(traceback.format_exc())

#Scrolling down for comment and closing inc
def closePowerCut3():
    try:
        pyautogui.scroll(-1000)
        time.sleep(1)
        target1 = pyautogui.locateCenterOnScreen("pwcut_images\enter_comment.png",confidence=0.8)
        pyautogui.click(target1.x,target1.y+50)
        pyautogui.typewrite("Power supply is back")
        target2 = pyautogui.locateCenterOnScreen("pwcut_images\okey.png",confidence=0.8)
        pyautogui.click(target2)
        time.sleep(2)
        target3 = pyautogui.locateCenterOnScreen("pwcut_images\confirm.png",confidence=0.8)
        time.sleep(2)
        pyautogui.click(target3)  #not working properly TODO
        pyautogui.click(target3.x+650,target3.y-40)
    except Exception:
        print(traceback.format_exc())

#dif steps for unittest
def closePowerCut():
    closePowerCut1()
    closePowerCut2()
    closePowerCut3()

def closeINC():
    print("kaki")

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
    layout = [
    [sg.Button("Remedy To Conclusion INC")], 
    [sg.Button("Remedy To Conclusion")],
    [sg.Button("Close Power Cut")],
    [sg.Button("Close Site Entry")],
    [sg.Button("Close INC")],
    [sg.Button("Exit")]
    ]
    window = sg.Window("Kys", layout, size=(300,300),
                    icon='pwcut_images\sadfrog.ico',background_color='green',
                    transparent_color='green',grab_anywhere=True)
    global contact
    # Create an event loop
    while True:
        event, values = window.read()
        if event == "Remedy To Conclusion INC":
            signInFromRemedyToNotePad()
            signInToCCL()
            contact = ""
            setTimeInCCL()
        if event == "Remedy To Conclusion":
            copySiteFromRemedyToCCL()
            signInFromRemedyToNotePad()
            signInToCCL()
            #global contact
            contact = ""
            setTimeInCCL()
        if event == "Close Power Cut":
            closePowerCut()
        if event == "Close Site Entry":
            closeSiteEntry()
        if event == "Close INC":
            closeINC()
        # End program if user closes window or presses the OK button
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()


if __name__ == '__main__':
    main()