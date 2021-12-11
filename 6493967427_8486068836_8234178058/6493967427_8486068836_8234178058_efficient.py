from stringGenerator import stringGenerator
from utils import get_memory_diff, get_memory_point, get_time_diff, get_time_point, write_output

mapping = {"A":0,"C":1,"G":2,"T":3}
penalty = [
    [0,110,48,94],
    [110,0,118,48],
    [48,118,0,110],
    [94,48,110,0]
]
delta = 30


#Basic Version
def dynamicSequentialAlignmentBasic(string1,string2):
    start_time = get_time_point()
    start_memory = get_memory_point()

    m,n = len(string1),len(string2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # print(dp)
    
    for i in range(n+1):
        dp[0][i] = i * delta
    for i in range(m + 1):
        dp[i][0] = i * delta 
        
    for i in range(1,m+1):
        for j in range(1,n+1):
            if string1[i-1] == string2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                index1,index2 = mapping[string1[i-1]],mapping[string2[j-1]]
                currentPen = penalty[index1][index2]
                dp[i][j] = min(dp[i-1][j-1] + currentPen, dp[i-1][j] + delta, dp[i][j-1] + delta)
            
    max_len = m + n 
    i = m
    j = n
    xIdx, yIdx = max_len, max_len
    string1result = [None for _ in range(max_len+1)]
    string2result = [None for _ in range(max_len+1)]
    
    while ( i!=0 and j!=0 ):
        if string1[i-1] == string2[j-1]:
            string1result[xIdx] = string1[i-1]
            xIdx -= 1
            i -= 1
            string2result[yIdx] = string2[j-1]
            yIdx -= 1
            j -= 1
            
            
        elif dp[i-1][j-1] + penalty[mapping[string1[i-1]]][mapping[string2[j-1]]] == dp[i][j]:
            string1result[xIdx] = string1[i-1]
            string2result[yIdx] = string2[j-1]
            xIdx -= 1
            yIdx -= 1
            i -= 1
            j -= 1
            
        elif dp[i-1][j] + delta == dp[i][j]:
            string1result[xIdx] = string1[i-1]
            string2result[yIdx] = '_'
            xIdx -= 1
            yIdx -= 1
            i -= 1
            
        elif dp[i][j-1] + delta == dp[i][j]:
            string1result[xIdx] = '_'
            string2result[yIdx] = string2[j-1]
            xIdx -= 1
            yIdx -= 1
            j -= 1
            
        # else:
        #     print(i,j,dp[i][j])
        #     print(string1[29],string2[28])
        #     print(dp[29-1][28-1] + penalty[mapping[string1[29-1]]][mapping[string2[28-1]]])
        #     print(dp[29-1][28] + delta)
        #     dp[29][28-1] + delta
        #     print("exception")
    
    # print("step1 done")
    while xIdx > 0 :
        if i > 0:
            i -= 1
            string1result[xIdx] = string1[i]
            xIdx -= 1
        else:
            string1result[xIdx] = '_'
            xIdx -= 1
        
    while yIdx > 0:
        if j > 0:
            j -= 1
            string2result[yIdx] = string2[j]
            yIdx -= 1
        else:
            string2result[yIdx] = '_'
            yIdx -= 1
    
    startIdx = max_len
    for i in range(max_len,0,-1):
        if string2result[i] == '_' and string1result[i] == '_':
            startIdx = i + 1
            break 
    end_time = get_time_point()
    end_memory = get_memory_point()
    return "".join(string1result[startIdx:]),"".join(string2result[startIdx:]),dp[-1][-1],get_time_diff(start_time,end_time),get_memory_diff(start_memory,end_memory)



#Space Optimized Efficient Version
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
    
