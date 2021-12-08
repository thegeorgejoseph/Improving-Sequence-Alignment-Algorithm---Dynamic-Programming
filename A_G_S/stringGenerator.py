
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