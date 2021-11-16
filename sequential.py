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
    dp = [[0 for _ in range(n + 2)] for _ in range(m + 2)]
    # print(dp)
    
    for i in range(n+m):
        dp[i][0] = i * delta
        dp[0][i] = i * delta
        
        
    for i in range(1,m+1):
        for j in range(1,n+1):
            if string1[i-1] == string2[i-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                index1,index2 = mapping[string1[i-1]],mapping[string2[j-1]]
                currentPen = penalty[index1][index2]
                dp[i][j] = min(dp[i-1][j-1] + currentPen, dp[i-1][j] + delta, dp[i][j-1] + delta)
            
    print(dp)
    max_len = m + n 
    i = m
    j = n
    xIdx, yIdx = max_len, max_len
    string1result = ['' for _ in range(max_len+1)]
    string2result = ['' for _ in range(max_len+1)]
    
    while ( i!=0 and j!=0 ):
        if string1[i-1] == string2[j-1]:
            string1result[xIdx] = string1[i-1]
            xIdx -= 1
            i -= 1
            string2result[yIdx] = string2[j-1]
            yIdx -= 1
            j -= 1
            print("here ",i,"xxx",j)
            print(string1result)
            print(string2result)
            
        elif dp[i-1][j-1] + penalty[mapping[string1[i-1]]][mapping[string2[j-1]]] == dp[i][j]:
            string1result[xIdx] = string1[i-1]
            string2result[yIdx] = string2[j-1]
            xIdx -= 1
            yIdx -= 1
            i -= 1
            j -= 1
            print("here2 ",i,"xxx",j)
            print(string1result)
            print(string2result)
        elif dp[i-1][j] + delta == dp[i][j]:
            string1result[xIdx] = string1[i-1]
            string2result[yIdx] = '_'
            xIdx -= 1
            yIdx -= 1
            i -= 1
            print("here3 ",i,"xxx",j)
            print(string1result)
            print(string2result)
        elif dp[i][j-1] + delta == dp[i][j]:
            string1result[xIdx] = '_'
            string2result[yIdx] = string2[j-1]
            xIdx -= 1
            yIdx -= 1
            j -= 1
            print("here4 ",i,"xxx",j)
            print(string1result)
            print(string2result)
        else:
            print(i,j,dp[i][j])
            print(string1[29],string2[28])
            print(dp[29-1][28-1] + penalty[mapping[string1[29-1]]][mapping[string2[28-1]]])
            print(dp[29-1][28] + delta)
            dp[29][28-1] + delta
            print("exception")
    
    print("step1 done")
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
    
    startIdx = 1
    for i in range(max_len,0,-1):
        if string2result[i] == '_' and string1result[i] == '_':
            startIdx += 1
            break 
    
    
    print(f"Minimum Penalty is {dp[m][n]}")
    print("".join(string1result))
    print("".join(string2result))
    

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
            
            
if __name__  == '__main__':
    string1, string2 = stringGenerator()
    input1 = "ACACTGACTACTGACTGGTGACTACTGACTGG"
    input2 =  "TATTATACGCTATTATACGCGACGCGGACGCG"
    print(f'The First Generated String is ${string1} and the Second Generated String is ${string2}')
    print(f"String1 equal to Input1: {string1 == input1}")
    print(f"String2 equal to Input2: {string2 == input2}")
    
    dynamicSequentialAlignment(string1,string2)