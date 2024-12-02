with open("day_2/day_2_input.txt") as f:
    lines = f.readlines()
    count = 0
    for report in lines:
        report = report.split()
        #report is a list of strs which coorespond to each number
        d = [] #differential between nums (must be same sign and 1, 2, or 3)
        safe = True
        #checks each value in the report
        for i in range(len(report) -1):
            d.append(int(report[i]) - int(report[i+1]))
            if abs(d[-1]) not in [1, 2, 3]:
                #not safe
                safe = False
                break
        #first element determines if increasing
        if d[0] > 0:
            pos = True
        else:
            pos = False
        for j in range(1, len(d)):
            if pos and d[j] < 0:
                safe = False
                continue
            elif not pos and d[j] > 0:
                safe = False
                continue
        if safe:
            count += 1

print(count)