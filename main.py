
'''
coded by:                            
                               ______                         
.---.-.---.-.----.-----.-----.|__    |.-----.-----.-----.----.
|  _  |  _  |   _|  _  |     ||    __||  _  |  _  |  _  |   _|
|___._|___._|__| |_____|__|__||______||   __|_____|_____|__|  
                                      |__|                         
                    
                    
# Discord:
# MEOWPOOP#7345
                                                                                
 ,_     _
 |\\_,-~/
 / _  _ |    ,--.
(  @  @ )   / ,-'
 \  _T_/-._( (
 /         `. \
|         _  \ |
 \ \ ,  /      |
  || |-_\__   /
 ((_/`(____,-'
'''




import requests 
import tkinter as tk 
from datetime import datetime

from tkinter import *

canvas= tk.Tk()
canvas.config(bg="black")
canvas.geometry("600x300")
canvas.title("Bitcoin Tracker")

f1=("poppins", 24, "bold")
f2=("poppins", 22, "bold")
f3=("poppins", 18, "normal")

label =tk.Label(canvas, text = "BTC Price", font =f1)
label.config(fg="yellow")
label.config(bg="black")
label.pack(pady = 20)
label =tk.Label(canvas, text = "by: aaron2poor")
label.config(fg="magenta"),label.pack(anchor=CENTER)
label.config(bg="black")


labelPrice= tk.Label(canvas, font = f2)
labelPrice.pack(pady=20)

labelTime= tk.Label(canvas, font = f3)
labelTime.pack(pady=20)


def trackBitcoin():
    url="https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR"
    response=requests.get(url).json()
    price= response["USD"]
    time = datetime.now().strftime("%H:%M:%S")
    labelPrice.config(text ="RealTime BTC Price: "+str(price)+"$")
    labelPrice.config(fg="white")
    labelPrice.config(bg="black")
    labelTime.config(text="Current Time: " + time)
    labelTime.config(fg="white")
    labelTime.config(bg="black")

    canvas.after(1000, trackBitcoin)
    










trackBitcoin()
canvas.mainloop()
