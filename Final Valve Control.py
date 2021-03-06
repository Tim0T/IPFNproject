# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 14:48:32 2021

@author: tim
"""
#Before all, enter in the Console : pip install pyfirmata2

#Import necessary Packages

import time
from tkinter import *
from pyfirmata import *
from datetime import datetime

#Connecting to the Arduino Port
board = Arduino(Arduino.AUTODETECT)
#If it fail, you can use the manual selection : board = Arduino('COM4')
#You can find which COM is used on the Device Manager of windows board or on Arduino board

#Creation of the graphic window
window = Tk()

#Creation of timers that allow me to save if the Valves are open or not
compteur1 = 0
compteur2 = 0
compteur3 = 0
compteur4 = 0
compteur5 = 0
compteur6 = 0

#Definition of functions that are activated when we click on the switch button
def Valve1():
        #Definition of our timers as global
        global compteur1
        #Increment of the timer
        compteur1 = compteur1 +1
        #Extraction of the time
        now=datetime.now()
        #Definition of the form of the time information that i want
        current_time = now.strftime("%H:%M:%S")
        #If timer is even , it significate that the valve has to be off
        if (compteur1 % 2) == 0:
            #I write a message in the console with the time to have a history of the activations/desactivation  
            print("Valve 1 Off , time =",current_time)
            #I create a Button without effect that just show to the user that the valve is Off
            Button1Off = Button(window, text="Off",bg = "red",fg="white")
            #I place this Button
            Button1Off.place(x=170,y=25)
            #Desactivation of the arduino pin 13
            board.digital[13].write(0)
        #If timer is odd, it significate that the valve has to be on
        else:
            #I write a message in the console to have a history of the activations/desactivation  
            print("Valve 1 On, time =",current_time)
            #I create a Button without effect that just show to the user that the valve is On
            Button1On = Button(window, text="On",bg = "green",fg="white")
            #I place this Button
            Button1On.place(x=170,y=25)
            #Activation of the arduino pin 13
            board.digital[13].write(1)

def Valve2():
        #Definition of our timers as global
        global compteur2
        #Increment of the timer
        compteur2 = compteur2 +1
        #Extraction of the time
        now=datetime.now()
        #Definition of the form of the time information that i want
        current_time = now.strftime("%H:%M:%S")
        #If timer is even , it significate that the valve has to be off
        if (compteur2 % 2) == 0:
            #I write a message in the console to have a history of the activations/desactivation  
            print("Valve 2 Off , time =",current_time)
            #I create a Button without effect that just show to the user that the valve is Off
            Button2Off = Button(window, text="Off",bg = "red",fg="white")
            #I place this Button
            Button2Off.place(x=170,y=75)
            #Desactivation of the arduino pin 12
            board.digital[12].write(0)
        #If timer is odd, it significate that the valve has to be on
        else:
            #I write a message in the console to have a history of the activations/desactivation  
            print("Valve 2 On , time =",current_time)
            #I create a Button without effect that just show to the user that the valve is On
            Button2On = Button(window, text="On",bg = "green",fg="white")
            #I place this Button
            Button2On.place(x=170,y=75)
            #Activation of the arduino pin 12
            board.digital[12].write(1)

def Valve3():
        #Definition of our timers as global
        global compteur3
        #Increment of the timer
        compteur3 = compteur3 +1
        #Extraction of the time
        now=datetime.now()
        #Definition of the form of the time information that i want
        current_time = now.strftime("%H:%M:%S")
        #If timer is even , it significate that the valve has to be off
        if (compteur3 % 2) == 0:
            #I write a message in the console to have a history of the activations/desactivation  
            print("Valve 3 Off , time =",current_time)
            #I create a Button without effect that just show to the user that the valve is Off
            Button3Off = Button(window, text="Off",bg = "red",fg="white")
            #I place this Button
            Button3Off.place(x=170,y=125)
            #Desactivation of the arduino pin 11
            board.digital[11].write(0)
        #If timer is odd, it significate that the valve has to be on
        else:
            #I write a message in the console to have a history of the activations/desactivation  
            print("Valve 3 On , time =",current_time)
            #I create a Button without effect that just show to the user that the valve is On
            Button3On = Button(window, text="On",bg = "green",fg="white")
            #I place this Button
            Button3On.place(x=170,y=125)
            #Activation of the arduino pin 11
            board.digital[11].write(1)

def Valve4():
        #Definition of our timers as global
        global compteur4
        #Increment of the timer
        compteur4 = compteur4 +1
        #Extraction of the time
        now=datetime.now()
        #Definition of the form of the time information that i want
        current_time = now.strftime("%H:%M:%S")
        #If timer is even , it significate that the valve has to be off
        if (compteur4 % 2) == 0:
            #I write a message in the console to have a history of the activations/desactivation  
            print("Valve 4 Off , time =",current_time)
            #I create a Button without effect that just show to the user that the valve is Off
            Button4Off = Button(window, text="Off",bg = "red",fg="white")
            #I place this Button
            Button4Off.place(x=170,y=175)
            #Desactivation of the arduino pin 10
            board.digital[10].write(0)
        #If timer is odd, it significate that the valve has to be on
        else:
            #I write a message in the console to have a history of the activations/desactivation  
            print("Valve 4 On , time =",current_time)
            #I create a Button without effect that just show to the user that the valve is On
            Button4On = Button(window, text="On",bg = "green",fg="white")
            #I place this Button
            Button4On.place(x=170,y=175)
            #Activation of the arduino pin 10
            board.digital[10].write(1)


def Valve5():
        #Definition of our timers as global
        global compteur5
        #Increment of the timer
        compteur5 = compteur5 +1
        #Extraction of the time
        now=datetime.now()
        #Definition of the form of the time information that i want
        current_time = now.strftime("%H:%M:%S")
        #If timer is even , it significate that the valve has to be off
        if (compteur5 % 2) == 0:
            #I write a message in the console to have a history of the activations/desactivation  
            print("Valve 5 Off , time =",current_time)
            #I create a Button without effect that just show to the user that the valve is Off
            Button5Off = Button(window, text="Off",bg = "red",fg="white")
            #I place this Button
            Button5Off.place(x=170,y=225)
            #Desactivation of the arduino pin 9
            board.digital[9].write(0)
        #If timer is odd, it significate that the valve has to be on
        else:
            #I write a message in the console to have a history of the activations/desactivation  
            print("Valve 5 On , time =",current_time)
            #I create a Button without effect that just show to the user that the valve is On
            Button5On = Button(window, text="On",bg = "green",fg="white")
            #I place this Button
            Button5On.place(x=170,y=225)
            #Activation of the arduino pin 9
            board.digital[9].write(1)

def Valve6():
        #Definition of our timers as global
        global compteur6
        #Increment of the timer
        compteur6 = compteur6 +1
        #Extraction of the time
        now=datetime.now()
        #Definition of the form of the time information that i want
        current_time = now.strftime("%H:%M:%S")
        #If timer is even , it significate that the valve has to be off
        if (compteur6 % 2) == 0:
            #I write a message in the console to have a history of the activations/desactivation  
            print("Valve 6 Off , time =",current_time)
            #I create a Button without effect that just show to the user that the valve is Off
            Button6Off = Button(window, text="Off",bg = "red",fg="white")
            #I place this Button
            Button6Off.place(x=170,y=275)
            #Desactivation of the arduino pin 8
            board.digital[8].write(0)
        #If timer is odd, it significate that the valve has to be on
        else:
            #I write a message in the console to have a history of the activations/desactivation  
            print("Valve 6 On , time =",current_time)
            #I create a Button without effect that just show to the user that the valve is On
            Button6On = Button(window, text="On",bg = "green",fg="white")
            #I place this Button
            Button6On.place(x=170,y=275)
            #Activation of the arduino pin 8
            board.digital[8].write(1)

#Definition of the size of the window
window.geometry('250x330')

#Definition of the title of the window
window.title("Valve Control")

#Creation of the indications
label1 = Label(text="Valve 1")
label1.place(x=20,y=20,height =40)

label2 = Label(text="Valve 2")
label2.place(x=20,y=70,height =40)

label3 = Label(text="Valve 3")
label3.place(x=20,y=120,height =40)

label4 = Label(text="Valve 4")
label4.place(x=20,y=170,height =40)

label5 = Label(text="Valve 5")
label5.place(x=20,y=220,height =40)

label6 = Label(text="Valve 6")
label6.place(x=20,y=270,height =40)

#Switch Button creation
#When this button is activated it call the functions Valve1
Button1 = Button(window, text="Switch",bg = "black",fg="white",command=Valve1)
Button1.place(x=100,y=25)

#When this button is activated it call the functions Valve2
Button2 = Button(window, text="Switch",bg = "black",fg="white",command=Valve2)
Button2.place(x=100,y=75)

#When this button is activated it call the functions Valve3
Button3 = Button(window, text="Switch",bg = "black",fg="white",command=Valve3)
Button3.place(x=100,y=125)

#When this button is activated it call the functions Valve4
Button4 = Button(window, text="Switch",bg = "black",fg="white",command=Valve4)
Button4.place(x=100,y=175)

#When this button is activated it call the functions Valve5
Button5 = Button(window, text="Switch",bg = "black",fg="white",command=Valve5)
Button5.place(x=100,y=225)

#When this button is activated it call the functions Valve6
Button6 = Button(window, text="Switch",bg = "black",fg="white",command=Valve6)
Button6.place(x=100,y=275)


#Creation of the intial "Off" display
Button1Off = Button(window, text="Off",bg = "red",fg="white")
Button1Off.place(x=170,y=25)
Button2Off = Button(window, text="Off",bg = "red",fg="white")
Button2Off.place(x=170,y=75)
Button3Off = Button(window, text="Off",bg = "red",fg="white")
Button3Off.place(x=170,y=125)
Button4Off = Button(window, text="Off",bg = "red",fg="white")
Button4Off.place(x=170,y=175)
Button5Off = Button(window, text="Off",bg = "red",fg="white")
Button5Off.place(x=170,y=225)
Button6Off = Button(window, text="Off",bg = "red",fg="white")
Button6Off.place(x=170,y=275)



#Show the window
window.mainloop()


