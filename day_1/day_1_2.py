with open('day_1/day_1_input.txt') as f:
    lines = f.readlines()
    dict2 = {}
    list1 = []
    list2 = []
    similarity_score = 0 
    for item in lines:
        list1.append(item[:5])
        list2.append(item[8:-1])
    for item in list2:
        dict2[item] = dict2.get(item, 0) + 1
    
    for item in list1:
        temp_score = 0
        if item in dict2:
            temp_score += (int(dict2.get(item))) * int(item)
            similarity_score += temp_score
        
    print(similarity_score)
