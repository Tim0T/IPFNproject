#Importation of the necessary modules
#from microcontroleurs import arduino
import time
from datetime import datetime
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
from matplotlib import style
import matplotlib.animation as animation
import numpy as np

#Creation of the lists
Temperatures1 = []
Temperatures2 = []
Temperatures3 = []
Temperatures4 = []
Temperatures5 = []
Temperatures6 = []
Temps = []

#Initialisation of the graphic points (lists)
for i in range (0,359):
    Temperatures1.append(0)
    Temperatures2.append(0)
    Temperatures3.append(0)
    Temperatures4.append(0)
    Temperatures5.append(0)
    Temperatures6.append(0)
    Temps.append(359-i)

#Manual definition of the port ("COM5/6 must be changed if necessary)
#ma_carte1 = arduino("COM5")
#ma_carte2 = arduino("COM6")

#R0 is the Resistance of the sensor at 0 °C
R0 = 100
#x is the leading coefficient of the linearization of the mesures
x = 0.378

#Opening of the saving file
file = open("current_day.txt","w")
 
def get_back_values():
     
    #Measuring of the resistance
    #R1=ma_carte1.resistance_pt100(2,3,4,5)
    #R2=ma_carte1.resistance_pt100(6,7,8,9)
    #R3=ma_carte1.resistance_pt100(10,11,12,13)
    #R4=ma_carte2.resistance_pt100(2,3,4,5)
    #R5=ma_carte2.resistance_pt100(6,7,8,9)
    #R6=ma_carte2.resistance_pt100(10,11,12,13)
    
    #Definition of the Temperature from the resistance ( it can be necessary to modify the data)
    #T1=(R1-R0)/x
    #T2=(R2-R0)/x
    #T3=(R3-R0)/x
    #T4=(R4-R0)/x
    #T5=(R5-R0)/x
    #T6=(R6-R0)/x
    
    T1 = 150
    T2 = 120
    T3 = 115
    T4 = 220
    T5 = 165
    T6 = 300
    
    #Write the result in the console
    print("T1 =", T1)
    print("T2 =", T2)
    print("T3 =", T3)
    print("T4 =", T4)
    print("T5 =", T5)
    print("T6 =", T6)
    
    #suppress the oldest temperature and time
    del Temperatures1[0]
    del Temperatures2[0]
    del Temperatures3[0]
    del Temperatures4[0]
    del Temperatures5[0]
    del Temperatures6[0]
    del Temps [0]

    #Measuring of the curent time
    #Extraction of the time
    now = datetime.now()
    #Definition of the form
    current_time = now.strftime("%H:%M:%S")
    current_day = now.strftime("%m:%d")

    for i in range (0,358):
        Temps[i]=int(Temps[i])+1

    #Insertion in the lists of the new informations
    Temperatures1.insert(359,T1)
    Temperatures2.insert(359,T2)
    Temperatures3.insert(359,T3)
    Temperatures4.insert(359,T4)
    Temperatures5.insert(359,T5)
    Temperatures6.insert(359,T6)
    Temps.insert(359,0)
    
    
    #Saving
    
    file.write(" Time : ")
    current_time = str(current_time)
    file.write(current_time)
    file.write(" Temperatures1 : ")
    T1=str(T1)
    file.write(T1)
    file.write(" Temperatures2 : ")
    T2=str(T2)
    file.write(T2 )
    file.write(" Temperatures3 : ")
    T3=str(T3)
    file.write(T3)
    file.write(" Temperatures4 : ")
    T4=str(T4)
    file.write(T4)
    file.write(" Temperatures5 : ")
    T5=str(T5)
    file.write(T5)
    file.write(" Temperatures6 : ")
    T6=str(T6)
    file.write(T6)
    file.write("\n")

    return Temps, Temperatures1, Temperatures2, Temperatures3, Temperatures4, Temperatures5, Temperatures6

#Definition of the update function
def update_graph (dt):
    x, y1, y2, y3, y4, y5, y6 = get_back_values()    
    ax.clear()
    ax.set_ylim(0,500 , auto=False)
    ax.set_xlim(360,0 , auto=False)
    ax.set_xlabel('Time')
    ax.set_ylabel('Temperatures', color='g')
    ax.plot(x, y1, label="T1")
    ax.plot(x, y2, label="T2")
    ax.plot(x, y3, label="T3")
    ax.plot(x, y4, label="T4")
    ax.plot(x, y5, label="T5")
    ax.plot(x, y6, label="T6")
    
    #Creation of the indications
    label1 = tk.Label(text="Temperature 1 (°C)")
    label1.place(x=90,y=300,height =20)

    labelt1 = tk.Label(text=y1[358])
    labelt1.place(x=125,y=350,height =20)

    label2 = tk.Label(text="Temperature 2 (°C)")
    label2.place(x=240,y=300,height =20)

    labelt2 = tk.Label(text=y2[358])
    labelt2.place(x=275,y=350,height =20)

    label3 = tk.Label(text="Temperature 3 (°C)")
    label3.place(x=390,y=300,height =20)

    labelt3 = tk.Label(text=y3[358])
    labelt3.place(x=425,y=350,height =20)

    label4 = tk.Label(text="Temperature 4 (°C)")
    label4.place(x=540,y=300,height =20)
    
    labelt4 = tk.Label(text=y4[358])
    labelt4.place(x=575,y=350,height =20)

    label5 = tk.Label(text="Temperature 5 (°C)")
    label5.place(x=690,y=300,height =20)
    
    labelt5 = tk.Label(text=y5[358])
    labelt5.place(x=725,y=350,height =20)

    label6 = tk.Label(text="Temperature 6 (°C)")
    label6.place(x=840,y=300,height =20)
    
    labelt6 = tk.Label(text=y6[358])
    labelt6.place(x=875,y=350,height =20)
    
def closing():
    #close the saving file
    file.close()
    #eject the card
    #ma_carte.fermer()
    
#Creation of the window
app = tk.Tk()
#Name the window
app.wm_title("Temperature Monitoring")
#import formatting
style.use("ggplot")
fig = Figure(figsize=(10,5), dpi=100)
#Place the Graph in the top of the window
ax = fig.add_subplot(211)
ax.set_xlabel('Temps')
ax.set_ylabel('Temperatures', color='g')
fig.set_tight_layout(True)
 
graph = FigureCanvasTkAgg(fig, master=app)
canvas = graph.get_tk_widget()
canvas.grid(row=0, column=0)

ani = animation.FuncAnimation(fig, update_graph, interval=500)
app.protocol("Closing Window",closing)

app.mainloop()




    

