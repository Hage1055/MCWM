#Automated BioChar Injection System
#Mean Clean Water Machine

# --- Import Libraries ---

import RPi.GPIO as GPIO
import time
from tkinter import *
import tkinter.font

# --- Pin settings ---

PWMPin = 12 #PWM Pin connected to ENA
Motor1 = 16 #Grinder motor connected to input 1
Motor2 = 18 #Grinder motor connected to input 2

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) #This accesses GPIOs according to physical location
GPIO.setup(PWMPin, GPIO.OUT) #Sets pin to an output
GPIO.setup(Motor1, GPIO.OUT) #Sets pin to an output
GPIO.setup(Motor2, GPIO.OUT) #Sets pin to an output

GPIO.output(PWMPin, GPIO.LOW) #Set pins to low on startup
GPIO.output(Motor1, GPIO.LOW)
GPIO.output(Motor2, GPIO.LOW)

PwmValue = GPIO.PWM(PWMPin, 2000) #Sets PWM frequency
PwmValue.start(100) #Duty cycle of motor in percent

# --- GUI settings ---

Gui = Tk()
Gui.title("Automated BioChar Injection System")
Gui.config(background = "#00FFFF")
Gui.minsize(800,300)
Font1 = tkinter.font.Font(family = 'Helvetica', size = 18, weight = 'bold')

def MotorClockwise():
    GPIO.output(Motor1, GPIO.LOW) #Motor will move clockwise
    GPIO.output(Motor2, GPIO.HIGH)
    Text2 = Label(Gui,text='                              ',font=Font1,fg='#FFFFFF',bg='#00FFFF',padx=0)
    Text2.grid(row=0,column=1)
    Text2 = Label(Gui,text='Clockwise',font=Font1,fg='#FFFFFF',bg='#00FFFF',padx=0)
    Text2.grid(row=0,column=1)
    
def MotorAntiClockwise():
    GPIO.output(Motor1, GPIO.HIGH) #Motor will move anti-clockwise
    GPIO.output(Motor2, GPIO.LOW)
    Text2 = Label(Gui,text='                        ',font=Font1,fg='#FFFFFF',bg='#00FFFF',padx=0)
    Text2.grid(row=0,column=1)
    Text2 = Label(Gui,text='Anti-Clockwise',font=Font1,fg='#FFFFFF',bg='#00FFFF',padx=0)
    Text2.grid(row=0,column=1)

def MotorStop():
    GPIO.output(Motor1, GPIO.LOW) #Motor will stop
    GPIO.output(Motor2, GPIO.LOW)
    Text2 = Label(Gui,text='                        ',font=Font1,fg='#FFFFFF',bg='#00FFFF',padx=0)
    Text2.grid(row=0,column=1)
    Text2 = Label(Gui,text='Stop',font=Font1,fg='#FFFFFF',bg='#00FFFF',padx=0)
    Text2.grid(row=0,column=1)

def ChangePWM(self):
    PwmValue.ChangeDutyCycle(Scale1.get())

Text1 = Label(Gui,text='Grinder Motor Status:',font=Font1,fg='#FFFFFF',bg='#00FFFF',padx=50,pady=50)
Text1.grid(row=0,column=0)

Text2 = Label(Gui,text='    ',font=Font1,fg='#FFFFFF',bg='#00FFFF',padx=0)
Text2.grid(row=0,column=1)

Text1 = Label(Gui,text='    ',font=Font1,fg='#FFFFFF',bg='#00FFFF',padx=150,pady=50)
Text1.grid(row=0,column=2)

Button1 = Button(Gui,text='Clockwise',font=Font1,command=MotorClockwise,bg='bisque2',height=1,width=10)
Button1.grid(row=1,column=0)

Button2 = Button(Gui,text='Stop',font=Font1,command=MotorStop,bg='bisque2',height=1,width=10)
Button2.grid(row=1,column=1)

Button3 = Button(Gui,text='Anti-Clockwise',font=Font1,command=MotorAntiClockwise,bg='bisque2',padx=50,height=1,width=10)
Button3.grid(row=1,column=2)

Text3 = Label(Gui,text='Grinder Motor Speed',font=Font1,bg='#00FFFF',fg='#FFFFFF',padx=50,pady=50)
Text3.grid(row=2,columnspan=2)

Scale1 = Scale(Gui, from_=0, to=100, orient = HORIZONTAL, resolution = 1, command = ChangePWM)
Scale1.grid(row=2,column=2)

Gui.mainloop()
