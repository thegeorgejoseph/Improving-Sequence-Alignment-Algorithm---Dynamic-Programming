from A_G_S_basic import dynamicSequentialAlignmentBasic
from stringGenerator import stringGenerator
from utils import get_memory_diff, get_memory_point, get_time_diff, get_time_point, write_output


def find_min_cost_eff(string1,string2):
    return ""

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
    
    if m < 2 or n < 2:
            res1,res2,min_cost = dynamicSequentialAlignmentBasic(string1,string2)
            end_time = get_time_point()
            end_memory = get_memory_point()
            return res1,res2,min_cost,get_time_diff(start_time,end_time),get_memory_diff(start_memory,end_memory)

    left_cost = find_min_cost_eff(string1, string2[:n//2])
    right_cost = find_min_cost_eff(string1[::-1], string2[n//2:][::-1])

    split_index = 0
    for i in range(0, m+1):
        min_cost = left_cost[split_index][0] + right_cost[m-split_index][0]
        cur_cost = left_cost[i][0] + right_cost[m-i][0]
        if cur_cost < min_cost:
            split_index = i

    partition = []
    left_cost = []
    right_cost = []
    left = dynamicSequentialAlignmentEfficient(string1[:split_index], string2[:n//2])
    right = dynamicSequentialAlignmentEfficient(string1[split_index:], string2[n//2:])
    res=[]
    for r in range(3):
        res.append(left[r]+right[r])
    return res




  
    
  
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
    
