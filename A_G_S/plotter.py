"""
Plotter.py

Author: Amal Jose

Purpose: Generate input and plot time and memory stats for the algorithm
"""
import matplotlib.pyplot as plt
import numpy as np
from A_G_S_basic import dynamicSequentialAlignmentBasic
from A_G_S_efficient import dynamicSequentialAlignmentEfficient
import random

PLOT_X_LIMIT=10000
NUM_POINTS=20

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
        r1,r2,c,time,memory=dynamicSequentialAlignmentBasic(string1,string2)
        inefficient_time.append(time)
        inefficient_memory.append(memory)

    for (string1,string2) in inputs:
        r1,r2,c,time,memory=dynamicSequentialAlignmentEfficient(string1,string2)  
        efficient_time.append(time)
        efficient_memory.append(memory)
      

    x=np.linspace(0, PLOT_X_LIMIT,NUM_POINTS)
    inefficient_time_values=np.array(inefficient_time)
    inefficient_memory_values=np.array(inefficient_memory)
    efficient_time_values=np.array(efficient_time)
    efficient_memory_values=np.array(efficient_memory)

    plt.plot(x, inefficient_time_values, linewidth=2.0,label="Inefficient Algorithm",color="r")
    plt.plot(x, efficient_time_values, linewidth=2.0,label="Efficient Algorithm",color="g")
    plt.title("CPU Time(s) vs Problem Size")
    plt.legend()
    plt.savefig("CPUPlot.png")


    plt.plot(x, inefficient_memory_values, linewidth=2.0,label="Inefficient Algorithm",color="r")
    plt.plot(x, efficient_memory_values, linewidth=2.0,label="Efficient Algorithm",color="g")
    plt.title("Memory Usage(KB) vs Problem Size")

    plt.savefig("MemoryPlot.png")
