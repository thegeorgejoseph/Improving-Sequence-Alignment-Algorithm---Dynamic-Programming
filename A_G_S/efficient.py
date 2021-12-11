from A_G_S_basic import dynamicSequentialAlignmentBasic
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

def move_col(self, dp):
    for i in range(len(dp)):
        dp[i][0], dp[i][1] = dp[i][1], 0
    return dp

def find_min_cost(string1, string2, return_cost=False):
    dp = [[float("inf") for i in range(2)] for j in range(len(string1)+1)]
    m = len(dp)
    n = len(dp[0])
    
    # Base case
    for i in range(m):
        dp[i][0] = i * delta

    for j in range(1, len(str2)+1):
        dp[0][1] = j * delta
        for i in range(1, len(str1)+1):
            dp[i][1] = min(
                    dp[i-1][0] + penalty[mapping[string1[i-1]][string2[j-1]],
                    dp[i-1][1] + delta,
                    dp[i][0] + delta
                )

        dp = self.move_col(dp)
    return dp if not return_cost else dp[-1][0]


# @Srini, you'll need to edit this function to work with the efficient algorithm
def dynamicSequentialAlignmentEfficient(string1,string2):
    # mapping = {"A":0,"C":1,"G":2,"T":3}
    # penalty = [
    #     [0,110,48,94],
    #     [110,0,118,48],
    #     [48,118,0,110],
    #     [94,48,110,0]
    # ]
    # delta = 30
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

    # partition = []
    left_cost = []
    right_cost = []
    left = dynamicSequentialAlignmentEfficient(string1[:split_index], string2[:n//2])
    right = dynamicSequentialAlignmentEfficient(string1[split_index:], string2[n//2:])
    res=[]
    for r in range(3):
        res.append(left[r]+right[r])
    # return res




  
    
  
    end_time = get_time_point()
    end_memory = get_memory_point()
    return res[0],res[1],res[2],end_time-start_time,end_memory-start_memory


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
    
