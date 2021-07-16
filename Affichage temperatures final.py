#Importation of the necessary modules
from microcontroleurs import arduino
from datetime import datetime
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib import style
import matplotlib.animation as animation
import time

#Creation of the lists used to save the value of the temperature and the time associated
Temperatures1 = []
Temperatures2 = []
Temperatures3 = []
Temperatures4 = []
Temperatures5 = []
Temperatures6 = []
Temps = []

#Initialisation of the lists
for i in range (0,359):
    Temperatures1.append(0)
    Temperatures2.append(0)
    Temperatures3.append(0)
    Temperatures4.append(0)
    Temperatures5.append(0)
    Temperatures6.append(0)
    Temps.append(359-i)

#Manual definition of the port ("COM5/6 must be changed if necessary)
ma_carte1 = arduino("COM5")
ma_carte2 = arduino("COM6")

#R0 is the Resistance of the sensor at 0 °C
R0 = 100
#x is the leading coefficient of the linearization of the mesures
x = 0.378

#Extraction of the time
now = datetime.now()

#Definition of the form that i want for the document of save
current_day = time.strftime("%Y-%m-%d-%H-%M")
#Definition of the kind of document that i want for the save
extension=".txt"
#The finale name of the document that fuse the two last arguments
file_name=current_day+extension

#Opening and creation of the saving file in the wrinting mode (w)
file = open(file_name,"w")
 

#Def that allow me to measure , save and return the new lists every 10s
def get_back_values():
     
    #Measuring of the resistance
    R1=ma_carte1.resistance_pt100(2,3,4,5)
    R2=ma_carte1.resistance_pt100(6,7,8,9)
    R3=ma_carte1.resistance_pt100(10,11,12,13)
    R4=ma_carte2.resistance_pt100(2,3,4,5)
    R5=ma_carte2.resistance_pt100(6,7,8,9)
    R6=ma_carte2.resistance_pt100(10,11,12,13)
    
    #Definition of the Temperature from the resistance ( it can be necessary to modify the data, especially x)
    T1=(R1-R0)/x
    T2=(R2-R0)/x
    T3=(R3-R0)/x
    T4=(R4-R0)/x
    T5=(R5-R0)/x
    T6=(R6-R0)/x
    
    #If needed to tests
    #T1 = 30
    #T2 = 20
    #T3 = 40
    #T4 = 150
    #T5 = 450
    #T6 = 400
    
    
    #Warning system, if the temeprature of a captor is higher than 400 , error window appear
    if T1 >= 400 :
        labelerror1 = tk.Label(text="High Température!")
        labelerror1.place(x=90,y=400,height =20)
    if T2 >= 400:
        labelerror2 = tk.Label(text="High Température!")
        labelerror2.place(x=240,y=400,height =20)
    if T3 >= 400:
        labelerror3 = tk.Label(text="High Température!")
        labelerror3.place(x=390,y=400,height =20)
    if T4 >= 400:
        labelerror4 = tk.Label(text="High Température!")
        labelerror4.place(x=540,y=400,height =20)
    if T5 >= 400:
        labelerror5 = tk.Label(text="High Température!")
        labelerror5.place(x=690,y=400,height =20)
    if T6 >= 400:
        labelerror6 = tk.Label(text="High Température!")
        labelerror6.place(x=840,y=400,height =20)
        
    #Warning system, if the temeprature of a captor is lower than 40 , error window appear
    if T1 <= 40:
        labelerror21 = tk.Label(text="Low Température!")
        labelerror21.place(x=90,y=400,height =20)
    if T2 <= 40:
        labelerror22 = tk.Label(text="Low Température!")
        labelerror22.place(x=240,y=400,height =20)
    if T3 <= 40:
        labelerror23 = tk.Label(text="Low Température!")
        labelerror23.place(x=390,y=400,height =20)
    if T4 <= 40:
        labelerror24 = tk.Label(text="Low Température!")
        labelerror24.place(x=540,y=400,height =20)
    if T5 <= 40:
        labelerror25 = tk.Label(text="Low Température!")
        labelerror25.place(x=690,y=400,height =20)
    if T6 <= 40:
        labelerror26 = tk.Label(text="Low Température!")
        labelerror26.place(x=840,y=400,height =20)
    
    
    #Write the result in the console to have a second way to take a look at the results
    print("T1 =", T1)
    print("T2 =", T2)
    print("T3 =", T3)
    print("T4 =", T4)
    print("T5 =", T5)
    print("T6 =", T6)
    
    #Suppress the oldest temperature and time
    del Temperatures1[0]
    del Temperatures2[0]
    del Temperatures3[0]
    del Temperatures4[0]
    del Temperatures5[0]
    del Temperatures6[0]
    del Temps [0]

    
    #Definition of the form needed for the time
    current_time = now.strftime("%H:%M:%S")
    
    #The time incrementation
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
    
    
    #Saving system
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
    
    #Return the time and temperatures
    return Temps, Temperatures1, Temperatures2, Temperatures3, Temperatures4, Temperatures5, Temperatures6



#Definition of the graphical update function
def update_graph (dt):
    #Extract with help of the last fo=unction, the new lists
    x, y1, y2, y3, y4, y5, y6 = get_back_values()   
    #Reste the graph
    ax.clear()
    #Define the limits of the graphic view in x and y lines
    ax.set_ylim(0,500 , auto=False)
    ax.set_xlim(360,0 , auto=False)
    #Name the axes
    ax.set_xlabel('Time')
    ax.set_ylabel('Temperatures', color='g')
    
    #Place all the temperatures with corresponding time 
    ax.plot(x, y1, label="T1", color = 'b' )
    ax.plot(x, y2, label="T2", color = 'g')
    ax.plot(x, y3, label="T3", color = 'r')
    ax.plot(x, y4, label="T4" , color = 'k')
    ax.plot(x, y5, label="T5" , color ='c')
    ax.plot(x, y6, label="T6" , color = 'm')
    
    #Creation of the real time indications with the associated colour and value
    label1 = tk.Label(text="Temperature 1 (°C)", fg = 'blue')
    label1.place(x=90,y=300,height =20)
    #Just Present the last measure of the list from the captor 1
    labelt1 = tk.Label(text=y1[358])
    labelt1.place(x=125,y=350,height =20)

    label2 = tk.Label(text="Temperature 2 (°C)", fg = 'green' )
    label2.place(x=240,y=300,height =20)
    #Just Present the last measure of the list from the captor 2
    labelt2 = tk.Label(text=y2[358])
    labelt2.place(x=275,y=350,height =20)

    label3 = tk.Label(text="Temperature 3 (°C)",fg = 'red')
    label3.place(x=390,y=300,height =20)
    #Just Present the last measure of the list from the captor 3
    labelt3 = tk.Label(text=y3[358])
    labelt3.place(x=425,y=350,height =20)

    label4 = tk.Label(text="Temperature 4 (°C)" , fg = 'black')
    label4.place(x=540,y=300,height =20)
    #Just Present the last measure of the list from the captor 4
    labelt4 = tk.Label(text=y4[358])
    labelt4.place(x=575,y=350,height =20)

    label5 = tk.Label(text="Temperature 5 (°C)", fg ='cyan')
    label5.place(x=690,y=300,height =20)
    #Just Present the last measure of the list from the captor 5
    labelt5 = tk.Label(text=y5[358])
    labelt5.place(x=725,y=350,height =20)

    label6 = tk.Label(text="Temperature 6 (°C)", fg = 'magenta')
    label6.place(x=840,y=300,height =20)
    #Just Present the last measure of the list from the captor 6
    labelt6 = tk.Label(text=y6[358])
    labelt6.place(x=875,y=350,height =20)


#When the graphic window is closed, i close the connexion with the cards and close the document of saving that allow a clean save
def closing():
    #close the saving file
    file.close()
    #eject the card
    ma_carte1.fermer()
    ma_carte2.fermer()
    
#Creation of the window
app = tk.Tk()
#Name the window
app.wm_title("Temperature Monitoring")
#import formatting
style.use("ggplot")
fig = Figure(figsize=(10,5), dpi=100)
#Place the Graph in the top of the window
ax = fig.add_subplot(211)
#Rename for the first time execution the axes
ax.set_xlabel('Temps')
ax.set_ylabel('Temperatures', color='g')
#Allow the window to be shown
fig.set_tight_layout(True)

#Definition of the canvas
graph = FigureCanvasTkAgg(fig, master=app)
canvas = graph.get_tk_widget()
canvas.grid(row=0, column=0)

#Allow python to animate the hraphic part
ani = animation.FuncAnimation(fig, update_graph, interval=1000)
app.protocol("Closing Window",closing)

#Execute the loop
app.mainloop()




    

