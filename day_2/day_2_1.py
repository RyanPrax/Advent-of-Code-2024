with open("day_2/day_2_input.txt") as f:
    lines = f.readlines()
    count = 0
    for report in lines:
        #Report is a list of strs which coorespond to each number
        report = report.split()

        #Differential between nums (must be same sign and 1, 2, or 3)
        d = []
        safe = True
        #Checks each value in the report
        for i in range(len(report) -1):
            d.append(int(report[i]) - int(report[i+1]))
            if abs(d[-1]) not in [1, 2, 3]:
                #Not safe
                safe = False
                break
        #First element determines if increasing/decreasing
        if d[0] > 0:
            pos = True
        else:
            pos = False
        #Every other element must match
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