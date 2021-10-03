import csv
from prettytable import PrettyTable
x = PrettyTable()
refdict = {}
x.field_names = ["Country", "Cost"]
with open('data.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        if (row["Indicator Id"] == "42573"):
            refdict[row["Country Name"]].append(row["2019"])
            x.add_row([row["Country Name"], row["2019"]])
            '''print(
                f'\t current in  {row["Country Name"]} costs around        {row["2019"]}')'''
            line_count += 1
    print(x)
    print(f'Processed {line_count} lines.')
