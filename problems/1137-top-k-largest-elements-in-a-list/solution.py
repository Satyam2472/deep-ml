def top_three_largest(values):
    # values: list of numbers
    # return the three  largest values in descending order

    if len(values) <= 3:
        return values
    
    ans = []
    max_num = 1e8*(-1)
    pos = -1

    

    for k in range(3):
        for i in range(len(values)):

            if values[i] > max_num:
                max_num = values[i]
                pos = i
            
        ans.append(max_num)
        max_num = 1e8*(-1)
        values[pos] = 1e9*(-1)

    return ans
        

