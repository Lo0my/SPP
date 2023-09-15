#Kinematics Program: Linear and Two Dimensional Motion
#By: Juan Robles
#This will help my brother and other students

import numpy as np
import math
import matplotlib.pyplot as plt

#Functions that I will use for the program

#Time function that will make the recursion for time, with a specified step
def time():
    initialT = float(input("Initial time: "))
    finalT = float(input("Final time: "))
    stepDelta = 0.1
    i = 0
    time = []
    while i < 11:
        recursiveT = initialT + i*stepDelta*finalT
        time.append(recursiveT)
        i += 1
    return time

#Horizontal function that will calculate the motion along the horizontal axis
def horizonalPosition(time):
    userXInput = float(input("Initial horizontal position: "))
    userVxInput = float(input("Initial horizontal speed: "))
    userAxInput = float(input("Horizontal acceleration: "))
    i = 0
    xAxis = []
    vxF = []
    ax = []
    time = time()
    if userAxInput != 0.0:
        while i < 11:
            xFinal = userXInput + userVxInput*time[i] + 0.5*userAxInput*(time[i]**2)
            xAxis.append(xFinal)
            vxFinal = userVxInput*time[i] + userAxInput * time[i]
            vxF.append(vxFinal)
            axconstant = userAxInput
            ax.append(axconstant)
            i += 1
    else:
        while i < 11:
            xFinal = userXInput + userVxInput*time[i] + 0.5*userAxInput*(time[i]**2)
            xAxis.append(xFinal)
            vxFinal = userVxInput
            vxF.append(vxFinal)
            axconstant = userAxInput
            ax.append(axconstant)
            i += 1
    return (xAxis, vxF, ax)

#Vertical function that will calculate the motion along the vertical axis
def verticalPosition(time):
    yAxis = []
    vyF = []
    ay = []
    userYInput = float(input("Initial vertical position: "))
    userVyInput = float(input("Initial vertical speed: "))
    userAyInput = float(input("Vertical acceleration: "))
    time = time()
    i = 0
    if userAyInput != 0.0:
        while i < 11:
            yFinal = userYInput + userVyInput*time[i] + 0.5*userAyInput*(time[i]**2)
            yAxis.append(yFinal)
            vyFinal = userVyInput*time[i] + userAyInput * time[i]
            vyF.append(vyFinal)
            ayconstant = userAyInput
            ay.append(ayconstant)
            i += 1
    else:
        while i < 11:
            yFinal = userYInput + userVyInput*time[i] + 0.5*userAyInput*(time[i]**2)
            yAxis.append(yFinal)
            vyFinal = userVyInput
            vyF.append(vyFinal)
            ayconstant = userAyInput
            ay.append(ayconstant)
            i += 1
    return (yAxis, vyF, ay)

#Function that will utilize both the horizontal and the vertical functions
def TwoDimensions(time):
    xAxis = []
    xSpeed = []
    ax = []
    yAxis = []
    ySpeed = []
    ay = []
    rVector = []
    velocityVector = []
    accelerationVector = []
    userXInput = float(input("Initial horizontal position: "))
    userVxInput = float(input("Initial horizontal speed: "))
    userAxInput = float(input("Horizontal acceleration: "))
    userYInput = float(input("Initial vertical position: "))
    userVyInput = float(input("Initial vertical speed: "))
    userAyInput = float(input("Vertical acceleration: "))
    time = time()
    i = 0
    if userAxInput == 0.0:
        while i < 11:
            xFinal = userXInput + userVxInput*time[i] + 0.5*userAxInput*(time[i]**2)
            xAxis.append(xFinal)
            vxFinal = userVxInput
            xSpeed.append(vxFinal)
            axconstant = userAxInput
            ax.append(axconstant)
            yFinal = userYInput + userVyInput*time[i] + 0.5*userAyInput*(time[i]**2)
            yAxis.append(yFinal)
            vyFinal = userVyInput*time[i] + userAyInput * time[i]
            ySpeed.append(vyFinal)
            ayconstant = userAyInput
            ay.append(ayconstant)
            rComp = math.sqrt(xFinal**2 + yFinal**2)
            rVector.append(rComp)
            vComp = math.sqrt(vxFinal**2+vyFinal**2)
            velocityVector.append(vComp)
            aComp = -math.sqrt(axconstant**2 + ayconstant**2)
            accelerationVector.append(aComp)
            i += 1
    elif userAyInput == 0.0:
        while i < 11:
            xFinal = userXInput + userVxInput*time[i] + 0.5*userAxInput*(time[i]**2)
            xAxis.append(xFinal)
            vxFinal = userVxInput*time[i] + userAxInput * time[i]
            xSpeed.append(vxFinal)
            axconstant = userAxInput
            ax.append(axconstant)
            yFinal = userYInput + userVyInput*time[i] + 0.5*userAyInput*(time[i]**2)
            yAxis.append(yFinal)
            vyFinal = userVyInput
            ySpeed.append(vyFinal)
            ayconstant = userAyInput
            ay.append(ayconstant)
            rComp = math.sqrt(xFinal**2 + yFinal**2)
            rVector.append(rComp)
            vComp = math.sqrt(vxFinal**2+vyFinal**2)
            velocityVector.append(vComp)
            aComp = math.sqrt(axconstant**2 + ayconstant**2)
            accelerationVector.append(aComp)
            i += 1
    else:
        while i < 11:
            xFinal = userXInput + userVxInput*time[i] + 0.5*userAxInput*(time[i]**2)
            xAxis.append(xFinal)
            vxFinal = userVxInput*time[i] + userAxInput * time[i]
            xSpeed.append(vxFinal)
            axconstant = userAxInput
            ax.append(axconstant)
            yFinal = userYInput + userVyInput*time[i] + 0.5*userAyInput*(time[i]**2)
            yAxis.append(yFinal)
            vyFinal = userVyInput
            ySpeed.append(vyFinal)
            ayconstant = userAyInput
            ay.append(ayconstant)
            rComp = math.sqrt(xFinal**2 + yFinal**2)
            rVector.append(rComp)
            vComp = math.sqrt(vxFinal**2+vyFinal**2)
            velocityVector.append(vComp)
            aComp = math.sqrt(axconstant**2 + ayconstant**2)
            accelerationVector.append(aComp)
            i += 1
    return (rVector, velocityVector, accelerationVector)

#Function that will give the user the choice of which axes to use for their calculations
def UserChoice():
    userChoice = input("Which axes do you want to use, x or y or both: ") 
    #Need to make the function that will include both of the axes
    while userChoice != 'X' or userChoice != 'x' or userChoice != 'Y' or userChoice != 'y':
        if userChoice == 'x' or userChoice == 'X':
            userPosition,userSpeed,userAcceleration = horizonalPosition(time)
            return (userPosition, userSpeed, userAcceleration)
        elif userChoice == 'y' or userChoice == 'Y':
            userPosition, userSpeed, userAcceleration = verticalPosition(time)
            return (userPosition, userSpeed, userAcceleration)
        elif userChoice == 'XY' or userChoice == 'xy':
            userPosition, userSpeed, userAcceleration = TwoDimensions(time)
            return (userPosition, userSpeed, userAcceleration)
        else:
            print("Enter a valid choice.")
            userChoice = input("Which axes do you want to use, x or y: ")

#Main function that will use all of the functions from above
def main():
    (position, speed, acceleration) = UserChoice()
    print(position)
    print(speed)
    plt.plot(position)
    plt.plot(speed)
    plt.plot(acceleration)
    plt.show()

if __name__ == "__main__": 
    main()



###################################################################################
#Room for notes for the things I want to add onto the program and whatnot
