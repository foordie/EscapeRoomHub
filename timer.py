import tkinter as tk
import requests
import time

# --- functions ---

def f():
    localtime = time.strftime("%H:%M:%S")
    lbl4['text'] = localtime
    # run again after 1000ms (1s)
    frame.after(1000, f)

# --- main ---

url = 'http://api.openweathermap.org/data/2.5/weather?q=Athlone,ie&appid=ca8b6f0388c49b7d926706a9c498310d'
data = requests.get(url)
read = data.json()
Cname = "City Name: {}".format(read['name'])
TempDeg = "Tempterature: {}".format(read['main']['temp'] - 273.15)
WeaDesc = "Description: {}".format(read['weather'][0]['description'])

frame = tk.Tk()
frame.configure(background='black')
#frame.attributes('-fullscreen', True) #Takes up whole screen, no title bar
#frame.state('zoomed') #Takes up whole screen with title bar on top. (Easier to exit when testing)

currentdate = time.strftime("%d/%m/%Y")

font = ('Times New Roman', 30)

lbl1 = tk.Label(frame, text=Cname, font=font, fg='white', bg='black')
lbl2 = tk.Label(frame, text=TempDeg+'°C', font=font, fg='white', bg='black')
lbl3 = tk.Label(frame, text=WeaDesc, font=font, fg='white', bg='black')

# empty label
lbl4 = tk.Label(frame, font=font, fg='white', bg='black')

lbl5 = tk.Label(frame, text=currentdate, font=font, fg='white', bg='black')
lbl6 = tk.Label(frame, text='*Insert complimentary comment here*', font=('Lucida Handwriting', 25), fg='white', bg='black')

lbl4.pack()
lbl5.pack()
lbl1.pack()
lbl2.pack()
lbl3.pack()
lbl6.pack()

# run first time
f()

frame.mainloop()