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
    B=[[float("inf") for i in range(2)] for j in range(len(string1)+1)]
    m,n = len(string1),len(string2)

    for i in range(0,m+1):
        B[i][0]=i*delta

    for j in range(1,n+1):
        B[0][1]=j*delta
        for i in range(1,m+1):
            index1,index2 = mapping[string1[i-1]],mapping[string2[j-1]]
            currentPen = penalty[index1][index2]
            B[i][1]=min(currentPen+B[i-1][0],delta+B[i-1][1],delta+B[i][0])
    
        for i in range(0,m+1):
            B[i][0]=B[i][1]
            B[i][1]=0

    return [B[i][0] for i in range(0,m+1)]

def DivideAndConquerAlignment(string1,string2):
    m,n = len(string1),len(string2)

    if(m < 2 or n < 2):
            res1,res2,min_cost,time,mem = dynamicSequentialAlignmentBasic(string1,string2)
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

    left = DivideAndConquerAlignment(string1[:q], string2[:n//2])
    right = DivideAndConquerAlignment(string1[q:], string2[n//2:])
	
    return left[0]+right[0],left[1]+right[1],left[2]+right[2]

def dynamicSequentialAlignmentEfficient(string1,string2):
   
    start_time = get_time_point()
    start_memory = get_memory_point()
    res1,res2,cost=DivideAndConquerAlignment(string1,string2)
    end_time = get_time_point()
    end_memory = get_memory_point()
    return res1,res2,cost,get_time_diff(start_time,end_time),get_memory_diff(start_memory,end_memory)


if __name__  == '__main__':
    string1, string2 = stringGenerator()
    res1,res2, cost,time,memory = dynamicSequentialAlignmentEfficient(string1,string2)
    write_output(res1,res2,cost,time,memory)
    
