import time 

def dynamicSequentialAlignment(string1,string2):
    mapping = {"A":0,"C":1,"G":2,"T":3}
    penalty = [
        [0,110,48,94],
        [110,0,118,48],
        [48,118,0,110],
        [94,48,110,0]
    ]
    delta = 30
    #how to calculate penalty of alpha(A,C) = index0 = mapping["A"], index1 = mapping["C"] => penalty[index0][index1]
    
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
    
    
    print(f"Minimum Penalty is {dp[-1][-1]}")
    print(" ".join(string1result[startIdx:]))
    print(" ".join(string2result[startIdx:]))
    print("Done")   

def stringGenerator():
    results = []
    flag = False
    with open("input.txt") as file:
        for line in file:
            line = line.strip('\n')
            if line.isdigit() is False:
                if flag is True:
                    results.append(string)
                string = line
                flag = False
            else:
                flag = True
                result = string[:int(line)+1] + string + string[int(line)+1:]
                string = result
                # print(string)
                
        if flag is True:
            results.append(string)
            
    file.close()
    return results[0],results[1]
            

def unitTest(string1,string2):
    input1 = "ACACTGACTACTGACTGGTGACTACTGACTGG" #this is a test string based on prompt
    input2 =  "TATTATACGCTATTATACGCGACGCGGACGCG" #this is another test string based on prompt
    return input1 == string1 and input2 == string2

if __name__  == '__main__':
    string1, string2 = stringGenerator()
    print(f'The First Generated String is ${string1} and the Second Generated String is ${string2}')
    print(f"Validating Generated String and Input Strings : {unitTest(string1,string2)}")
    dynamicSequentialAlignment(string1,string2)
