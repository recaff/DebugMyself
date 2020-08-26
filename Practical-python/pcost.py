def portfolio_cost(filename):
    with open(filename,'rt') as f:
        header = next(f).split('\t')
        sum = 0
        for line in f:
            row = line.split('\t')
            sum += int(row[1])*float(row[2])
        print('Total cost',sum)