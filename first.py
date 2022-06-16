import pyautogui
import time
import pyperclip
# image files must be in the same directory!!!
# for debugging -> pyautogui.alert('This is the message to display.')
global contact
contact = ""
# click functions for windows taskbar
def clickRemedy():
    remedy = pyautogui.locateCenterOnScreen("remedy_icon.png")
    pyautogui.click(remedy)

def clickCCL():
    edge = pyautogui.locateCenterOnScreen("edge_icon.png")
    pyautogui.click(edge)
    time.sleep(0.5)
    ccl_page = pyautogui.locateCenterOnScreen("ccl_page.png",confidence=.5)
    pyautogui.click(ccl_page)

#functions for locating data inside remedy
def moveToFirmAndCopy():
    #first we open remedy
    clickRemedy()
    #moving to firm
    comp = pyautogui.locateCenterOnScreen("remedy_comp.png",confidence=0.9)
    pyautogui.click(comp.x+100,comp.y+2)
    pyautogui.rightClick()
    select = pyautogui.locateCenterOnScreen("select_all.png")
    pyautogui.click(select)
    pyautogui.hotkey('ctrl', 'c')
    global contact
    contact += pyperclip.paste()
    contact += " "

def moveToNameAndCopy():
    clickRemedy()
    Iname = pyautogui.locateCenterOnScreen("remedy_name.png",confidence=.8)
    pyautogui.click(Iname.x+150,Iname.y+2)
    pyautogui.rightClick()
    select = pyautogui.locateCenterOnScreen("select_all.png")
    pyautogui.click(select)
    pyautogui.hotkey('ctrl', 'c')
    global contact
    contact += pyperclip.paste()
    contact += " "

def moveToNumberAndCopy():
    clickRemedy()
    phone = pyautogui.locateCenterOnScreen("remedy_phone.png",confidence=.8)
    pyautogui.click(phone.x+10,phone.y+30)
    pyautogui.rightClick()
    select = pyautogui.locateCenterOnScreen("select_all.png")
    pyautogui.click(select)
    pyautogui.hotkey('ctrl', 'c')
    global contact
    contact += pyperclip.paste()
    contact += " "

#get all data to your clipboard for a sign in 
def signInFromRemedyToNotePad():
    moveToFirmAndCopy()
    print(contact)
    moveToNameAndCopy()
    print(contact)
    moveToNumberAndCopy()
    print(contact)

def signInToCCL():
    clickCCL()
    target = pyautogui.locateCenterOnScreen("contact_ccl.png",confidence=0.9)
    pyautogui.click(target.x+500,target.y)
    pyperclip.copy(contact)
    pyautogui.hotkey('ctrl', 'v')

def copySiteFromRemedyToCCL():
    clickRemedy()
    target = pyautogui.locateCenterOnScreen("site_code.png",confidence=0.8)
    pyautogui.click(target.x-200,target.y)
    pyautogui.rightClick(target.x-200,target.y)
    select = pyautogui.locateCenterOnScreen("select_all.png",confidence=0.8)
    pyautogui.click(select)
    pyautogui.hotkey('ctrl', 'x')
    clickCCL()
    site = pyautogui.locateCenterOnScreen("ccl_site.png",confidence=0.8)
    pyautogui.click(site.x+400,site.y)
    time.sleep(5)
    site = pyautogui.locateCenterOnScreen("ccl_page.png",confidence=0.8)
    pyautogui.click(site.x,site.y+400)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(5)
    pyautogui.click(site.x,site.y+490)

def setTimeInCCL():
    clickCCL()
    target = pyautogui.locateCenterOnScreen("enter_time.png",confidence=0.8)
    pyautogui.click(target.x+160,target.y)
    time.sleep(0.01)
    pyautogui.click(target.x+310,target.y-390)
    pyautogui.click(target.x+310,target.y-40)
    
def main():
    #setUPWorkCode()
    copySiteFromRemedyToCCL()
    signInFromRemedyToNotePad()
    signInToCCL()
    setTimeInCCL()

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