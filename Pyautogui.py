import pyautogui
import webbrowser
import time

#Criando uma pasta nova.

#pyautgui.rightClick()
#pyautgui.move(xOffset=300, yOffset= 340, duration=2)
#pyautgui.move(xOffset=150, yOffset= 0 ,duration= 2)
#pyautoui.click()

#Copiando Pastas
#for i in range(2):
   # pyautogui.moveTo(203,153, 2)
   # pyautogui.dragTo(220,732, button='left',duration=2)


#Desafio

#posição do mouse para realizar a digitação: 1621,514


webbrowser.open('https://cursoautomacao.netlify.app/')

time.sleep(2)
pyautogui.moveTo(1519,622)
pyautogui.click()
pyautogui.typewrite('Thiago')
time.sleep(3)
pyautogui.screenshot('foto.jpg')
pyautogui.moveTo(43,314)
pyautogui.click()

time.sleep((3))
pyautogui.scroll(-1500)
time.sleep(3)

pyautogui.moveTo(483,676)
pyautogui.click()
time.sleep(3)
pyautogui.moveTo(602,663)
pyautogui.click()
time.sleep(3)


pyautogui.moveTo(664,675)
pyautogui.click()
time.sleep(3)
pyautogui.moveTo(602,663)
pyautogui.click()
time.sleep(3)


pyautogui.moveTo(861,680)
pyautogui.click()
time.sleep(3)
pyautogui.moveTo(602,663)
pyautogui.click()
time.sleep(3)



pyautogui.moveTo(1046,704)
pyautogui.click()
time.sleep(3)
pyautogui.moveTo(602,663)
pyautogui.click()
time.sleep(3)


pyautogui.moveTo(1229,670)
pyautogui.click()
time.sleep(3)
pyautogui.moveTo(602,663)
pyautogui.click()
time.sleep(3)

reposta =  pyautogui.confirm(text='pode realizar o último download?', title='Confirmando ação', buttons=['Sim', 'Não'])

if reposta == 'Sim':
    pyautogui.moveTo(1409, 714)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(602, 663)
    pyautogui.click()
    time.sleep(3)
    pyautogui.alert(text='Finalizou todo o procedimento', title='Automação', button='SUCESSO')

else:
    print(pyautogui.alert(text='Finalizou todo o procedimento, sem baixar o aruqivo JSON', title='Automação', button='SUCESSO'))







