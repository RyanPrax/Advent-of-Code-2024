with open('day_1/day_1_input.txt') as f:
    lines = f.readlines()
    list1 = []
    list2 = []
    sum = 0 
    for list in lines:
        list1.append(list[:5])
        list2.append(list[8:])
    list1.sort()
    list2.sort()
    for i in range(len(list1)):
        difference = abs(int(list1[i]) - int(list2[i]))
        sum += difference
    print(sum)
