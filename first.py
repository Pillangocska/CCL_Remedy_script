import pyautogui
import time
# image files must be in the same directory!!!
# for debugging -> pyautogui.alert('This is the message to display.')

# click functions for windows taskbar
def clickRemedy():
    remedy = pyautogui.locateCenterOnScreen("remedy_icon.png")
    pyautogui.click(remedy)
    
def clickNotePad():
    notepad = pyautogui.locateCenterOnScreen("notepad_icon.png")
    pyautogui.click(notepad)

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

def moveToNameAndCopy():
    clickRemedy()
    Iname = pyautogui.locateCenterOnScreen("remedy_name.png",confidence=.8)
    pyautogui.click(Iname.x+150,Iname.y+2)
    pyautogui.rightClick()
    select = pyautogui.locateCenterOnScreen("select_all.png")
    pyautogui.click(select)
    pyautogui.hotkey('ctrl', 'c')

def moveToNumberAndCopy():
    clickRemedy()
    phone = pyautogui.locateCenterOnScreen("remedy_phone.png",confidence=.8)
    pyautogui.click(phone.x+10,phone.y+30)
    pyautogui.rightClick()
    select = pyautogui.locateCenterOnScreen("select_all.png")
    pyautogui.click(select)
    pyautogui.hotkey('ctrl', 'c')

#copies clipboard content to notepad
def copyClipboardToNotePad():
    clickNotePad()
    time.sleep(0.5)
    target = pyautogui.locateCenterOnScreen("notepad_target.png",confidence=.8)
    pyautogui.click(target.x+600,target.y+20)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('space')

#get all data to your clipboard for a sign in 
def signInFromRemedyToNotePad():
    #firm -> notepad
    moveToFirmAndCopy()
    copyClipboardToNotePad()
    #name -> notepad
    moveToNameAndCopy()
    copyClipboardToNotePad()
    #phone -> notepad
    moveToNumberAndCopy()
    copyClipboardToNotePad()
    #cuting data from notepad
    time.sleep(0.5)
    target = pyautogui.locateCenterOnScreen("notepad_target.png",confidence=.8)
    pyautogui.rightClick(target.x+600,target.y+20)
    allTarget = pyautogui.locateCenterOnScreen("notepad_all.png")
    pyautogui.click(allTarget)
    pyautogui.hotkey('ctrl', 'x')

def copyWorkCodeFromRemedy():
    clickRemedy()
    pyautogui.click(1200,270)
    pyautogui.dragRel(-300, 0, 0.4)
    pyautogui.hotkey('ctrl', 'x')

def pasteWorkCodeToCCLAndClickCode():
    clickCCL()
    pyautogui.click(500,180)
    for i in range(15):
        pyautogui.press('backspace')  
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.click(450,220)

def clickEntryOnWorkCode():
    pyautogui.click(580,700)
    time.sleep(1)
    pyautogui.click(540,830)

def setUPWorkCode():
    #needs some work only for chr's now
    copyWorkCodeFromRemedy()
    pasteWorkCodeToCCLAndClickCode()
    time.sleep(2) #could be more idk
    clickEntryOnWorkCode()

def signInToCCL():
    clickCCL()
    target = pyautogui.locateCenterOnScreen("contact_ccl.png",confidence=0.9)
    pyautogui.click(target.x+500,target.y)
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
    site = pyautogui.locateCenterOnScreen("ccl_page.png",confidence=0.8)
    pyautogui.click(site.x,site.y+400)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)
    pyautogui.click(site.x,site.y+490)

def setTimeInCCL():
    clickCCL()
    target = pyautogui.locateCenterOnScreen("enter_time.png",confidence=0.8)
    pyautogui.click(target.x+160,target.y)
    target1 = pyautogui.locateCenterOnScreen("enter_time1.png",confidence=0.9)
    pyautogui.click(target1)
    target2 = pyautogui.locateCenterOnScreen("enter_time2.png",confidence=0.9)
    pyautogui.click(target2)
    
def main():
    #printing out the size of the screen
    #screenWidth, screenHeight = pyautogui.size()
    #print(screenWidth)
    #print(screenHeight)
    
    #setUPWorkCode()
    copySiteFromRemedyToCCL()
    signInFromRemedyToNotePad()
    signInToCCL()
    setTimeInCCL()
    
    #end signal
    print("program closing...")

if __name__ == '__main__':
    main()
