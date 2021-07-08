#Importation of the necessary modules
#from microcontroleurs import arduino
import time
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

#Mesuring time needed
t = 60

#Creation of the lists
Temperatures1 = []
Temperatures2 = []
Temperatures3 = []
Temperatures4 = []
Temperatures5 = []
Temperatures6 = []
Temps = []

axes = plt.gca()

#Initialisation of the graphic points (lists)
for i in range (0,239):
    Temperatures1.append(0)
    Temperatures2.append(0)
    Temperatures3.append(0)
    Temperatures4.append(0)
    Temperatures5.append(0)
    Temperatures6.append(0)
    Temps.append(round(i/10))

#Manual definition of the port ("COM5/6 must be changed if necessary)
#ma_carte1 = arduino("COM5")
#ma_carte2 = arduino("COM6")

#R0 is the Resistance of the sensor at 0 °C
R0 = 100
#x is the leading coefficient of the linearization of the mesures
x= 0.378

#During t min, this loop is running every seconds
for i in range(t*60):
    
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
    current_time = now.strftime("%H:%M")
    current_day = now.strftime("%m:%d")

    #Insertion in the lists of the new informations
    Temperatures1.insert(239,T1)
    Temperatures2.insert(239,T2)
    Temperatures3.insert(239,T3)
    Temperatures4.insert(239,T4)
    Temperatures5.insert(239,T5)
    Temperatures6.insert(239,T6)
    Temps.insert(239,current_time)

   
    
    #Placement of all the points
    plt.plot(Temps,Temperatures1, label="T1")
    plt.plot(Temps,Temperatures2, label="T2")
    plt.plot(Temps,Temperatures3, label="T3")
    plt.plot(Temps,Temperatures4, label="T4")
    plt.plot(Temps,Temperatures5, label="T5")
    plt.plot(Temps,Temperatures6, label="T6")
    
     #Saving
    file = open(current_day,"w")
    file.write(" Time : ")
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
    file.write("  Temperatures4 : ")
    T4=str(T4)
    file.write(T4)
    file.write("  Temperatures5 : ")
    T5=str(T5)
    file.write(T5)
    file.write("  Temperatures6 : ")
    T6=str(T6)
    file.write(T6)
    file.write("\r\n")
    file.close()

    #Nice Formatting
    plt.ylabel("Temperatures (°C)")
    plt.xlabel("Time")
    axes.yaxis.set_ticks_position('right')
    axes.yaxis.set_label_position('right')
    plt.legend()
    plt.title("Temperature Acquisition")
    
    #Winbdow display
    plt.show()
    
    #Wait a second
    time.sleep(1)
    
    #Window closing
    plt.close()

    
#ma_carte.fermer()
