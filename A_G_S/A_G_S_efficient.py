from stringGenerator import stringGenerator
from utils import get_memory_point, get_time_point, write_output


# @Srini, you'll need to edit this function to work with the efficient algorithm
def dynamicSequentialAlignmentEfficient(string1,string2):
    mapping = {"A":0,"C":1,"G":2,"T":3}
    penalty = [
        [0,110,48,94],
        [110,0,118,48],
        [48,118,0,110],
        [94,48,110,0]
    ]
    delta = 30
    #how to calculate penalty of alpha(A,C) = index0 = mapping["A"], index1 = mapping["C"] => penalty[index0][index1]
    

    start_time = get_time_point()
    start_memory = get_memory_point()

    m,n = len(string1),len(string2)
  
  
    end_time = get_time_point()
    end_memory = get_memory_point()
    return "","",0,end_time-start_time,end_memory-start_memory


if __name__  == '__main__':
    string1, string2 = stringGenerator()

    # print("Generated Strings:")
    # print(string1+f" ({str(len(string1))})")
    # print(string2+f" ({str(len(string2))})")
    
    # print(f"\nValidating Generated String and Input Strings : {unitTest(string1,string2)}")
    res1,res2, cost,time,memory = dynamicSequentialAlignmentEfficient(string1,string2)




    # print("\nResults:")
    # print(res1)
    # print(res2)
    # print("\nCost: "+str(cost))
    # print("Time Taken: "+str(time))
    # print("Memory Used(KB): "+str(memory))
    write_output(res1,res2,cost,time,memory)
    
