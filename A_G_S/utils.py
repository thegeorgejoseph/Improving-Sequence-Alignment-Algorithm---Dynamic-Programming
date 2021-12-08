import time 
import os
import psutil


def get_time_point():
    return time.time()

def get_memory_point():
    process = psutil.Process(os.getpid())
    return float(process.memory_info().rss)/1024

def write_output(res1,res2,cost,time,memory):
     
    with open("output.txt","w") as file:
        if len(res1) > 100:
            file.write(res1[:51])
            file.write(" ")
            file.write(res1[len(res1)-50:])
            file.write("\n")
            file.write(res2[:51])
            file.write(" ")
            file.write(res2[len(res2)-50:])
        else:
            file.write(res1)
            file.write("\n")
            file.write(res2)
            
        file.write("\n"+str(cost))
        file.write(f"\n{float(time)}")
        file.write(f"\n{memory}")