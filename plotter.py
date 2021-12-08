"""
Plotter.py

Author: Amal Jose

Purpose: Generate input and plot time and memory stats for the algorithm
"""
import matplotlib.pyplot as plt
import numpy as np
from sequential import dynamicSequentialAlignment
from utils import get_memory_point, get_time_point
import random

PLOT_X_LIMIT=1000
NUM_POINTS=10

char_set = ["A","T","G","C"]

def augment_strings(string1,string2):
    random_char=random.choice(["A","T","G","C"])
    if((len(string1)+len(string2))%2==0):
        string1=string1+random_char
    else:
        string2=string2+random_char
    return string1,string2



if __name__  == '__main__':

    inefficient_time=[]
    inefficient_memory=[]
    efficient_time=[]
    efficient_memory=[]
    string1="A"
    string2="T"
    
    inputs=[]


    while(len(string1)+len(string2)<PLOT_X_LIMIT):
        inputs.append((string1,string2))
        for i in range(0,int(PLOT_X_LIMIT/NUM_POINTS)):
            string1,string2=augment_strings(string1,string2)

    for (string1,string2) in inputs:

        r1,r2,c,time,memory=dynamicSequentialAlignment(string1,string2)

        inefficient_time.append(time)
        inefficient_memory.append(memory)


        r1,r2,c,time,memory=dynamicSequentialAlignment(string1,string2)  

        efficient_time.append(time)
        efficient_memory.append(memory)

        print(memory)
      

    x=np.linspace(0, PLOT_X_LIMIT,NUM_POINTS)
    inefficient_time_values=np.array(inefficient_time)
    inefficient_memory_values=np.array(inefficient_memory)
    efficient_time_values=np.array(efficient_time)
    efficient_memory_values=np.array(efficient_memory)

    fig, ax = plt.subplots(2,1)
    plt.subplots_adjust(hspace=0.5)

    ax[0].plot(x, inefficient_time_values, linewidth=2.0,label="Inefficient Algorithm",color="r")
    ax[0].plot(x, efficient_time_values, linewidth=2.0,label="Efficient Algorithm",color="g")
    ax[0].set_title("CPU Time(s) vs Problem Size")
    ax[0].legend()

    ax[1].plot(x, inefficient_memory_values, linewidth=2.0,label="Inefficient Algorithm",color="r")
    ax[1].plot(x, efficient_memory_values, linewidth=2.0,label="Efficient Algorithm",color="g")
    ax[1].set_title("Memory Usage(KB) vs Problem Size")
    ax[1].legend()

    plt.savefig("plot.png")
