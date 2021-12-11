import sys

def stringGenerator():
    input_filename="input.txt"
    if len(sys.argv) >1:
        input_filename=sys.argv[1]
    results = []
    idxCounts = []
    initialStrings = []
    flag = False
    validate = False
    with open(input_filename) as file:
        for line in file:
            line = line.strip('\n')
            if line.isdigit() is False:
                if flag is True:
                    results.append(string)
                    idxCounts.append(idxCount)   
                string = line
                flag = False
                idxCount = 0
                initialStrings.append(string)
            else:
                flag = True
                result = string[:int(line)+1] + string + string[int(line)+1:]
                string = result
                idxCount += 1
                # print(string)
                
        if flag is True:
            results.append(string)
            idxCounts.append(idxCount)
                
    file.close()
    if idxCount !=0  and len(results[0]) > 2 ** idxCounts[0] * len(initialStrings[0]):
        results[0] = results[0][:(2**idxCounts[0]*len(initialStrings[0]))]
        validate = True
    if idxCount !=0 and len(results[1]) > 2 ** idxCounts[1] * len(initialStrings[1]):
        results[1] = results[1][:(2**idxCounts[1]*len(initialStrings[1]))]
        validate = True
    if validate: print("The strings have been validated to meet the size constraint")
    if len(results) == 0: 
        with open(input_filename) as file:
            for line in file:
                line  = line.strip('\n')
                results.append(line)
    return results[0],results[1]


if __name__ == "__main__":
    stringGenerator()