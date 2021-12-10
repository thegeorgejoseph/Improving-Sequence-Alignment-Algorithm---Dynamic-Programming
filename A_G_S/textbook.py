from types import DynamicClassAttribute
from stringGenerator import stringGenerator
from utils import get_memory_diff, get_memory_point, get_time_diff, get_time_point, write_output
from A_G_S_basic import dynamicSequentialAlignmentBasic

mapping = {"A":0,"C":1,"G":2,"T":3}
penalty = [
    [0,110,48,94],
    [110,0,118,48],
    [48,118,0,110],
    [94,48,110,0]
]
delta = 30

def SpaceEfficientAlignment(string1,string2):
    B=[]
    m,n = len(string1),len(string2)
    for i in range(0,m+1):
        B.append([0,0])
    for i in range(0,m+1):
        B[i][0]=i*delta

    for j in range(1,n+1):
        B[0][1]=j*delta
        for i in range(1,m):
            print("For ",i,j,"Comparing ",penalty[mapping[string1[i-1]]][mapping[string2[j-1]]]+B[i-1][0],delta+B[i-1][1],delta+B[i][0])
            index1,index2 = mapping[string1[i-1]],mapping[string2[j-1]]
            currentPen = penalty[index1][index2]
            B[i][1]=min(currentPen+B[i-1][0],min(delta+B[i-1][1],delta+B[i][0]))
    
        for i in range(0,m+1):
            B[i][0]=B[i][1]
            B[i][1]=0

    return [B[i][0] for i in range(0,m+1)]

def DivideAndConquerAlignment(string1,string2):
    m,n = len(string1),len(string2)

    if m < 2 or n < 2:
            res1,res2,min_cost,a,b = dynamicSequentialAlignmentBasic(string1,string2)
            return res1,res2,min_cost

    left_costs = SpaceEfficientAlignment(string1, string2[:n//2])
    right_costs = SpaceEfficientAlignment(string1[::-1], string2[n//2:][::-1])
    q=0
    sum=left_costs[0] + right_costs[m]
    for i in range(1,m+1):
        if(i == 0):
            sum = left_costs[i] + right_costs[m-i]
        if(sum > (left_costs[i] + right_costs[m-i])):
            sum = left_costs[i] + right_costs[m-i]
            q = i

    print(sum)
    left = DivideAndConquerAlignment(string1[:q], string2[:n//2])
    right = DivideAndConquerAlignment(string1[q:], string2[n//2:])
	
    return left[0]+right[0],left[1]+right[1],left[2]+right[2]

# @Srini, you'll need to edit this function to work with the efficient algorithm
def dynamicSequentialAlignmentEfficient(string1,string2):
   
    #how to calculate penalty of alpha(A,C) = index0 = mapping["A"], index1 = mapping["C"] => penalty[index0][index1]
    

    start_time = get_time_point()
    start_memory = get_memory_point()

  
    print(DivideAndConquerAlignment(string1,string2))


  
    
  
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
    
