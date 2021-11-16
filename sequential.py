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