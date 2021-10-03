def global_unit():
    import urllib.request as urllib2
    import csv
    from prettytable import PrettyTable
    x = PrettyTable()
    x.field_names = ["Country", "Cost"]
    Area = 6.1316
    r = 15.3
    Pr = 0.75
    dict = {}
    dict2 = []
    refvar = 2
    Irradiation_list = []
    refdict = {}
    cnt = "Global"
    with open('data.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            try:
                if (row["Indicator Id"] == "42573"):
                    #x.add_row([row["Country Name"], row["2019"]])
                    country_name = row["Country Name"]
                    Cost = row["2019"]
                    if (cnt == "Global"):
                        cst = float(12.1)
                    elif (country_name == cnt):
                        cst = float(row["2019"])
                    # refdict[country_name].append(Cost)

                    line_count += 1
            except KeyError:
                continue
    print(x)
    Irradiation = 0
    # open a connection to a URL using urllib2
    webUrl = urllib2.urlopen(
        "https://midcdmz.nrel.gov/apps/plot.pl?site=BMS;start=20200101;live=1;zenloc=222;amsloc=224;time=1;inst=60;inst=64;inst=65;inst=66;type=data;preset=0;first=3;math=0;second=-1;value=0.0;global=-1;direct=-1;diffuse=-1;user=0;axis=1;endyear=2021;endmonth=10;endday=1")
    # get the result code and print it
    print("result code: " + str(webUrl.getcode()))

    # read the data from the URL and print it
    data = webUrl.read()
    line_count = 0
    '''x = data.split("\n")
        print(x)'''
    # print(data.splitlines(0))
    dict = data.splitlines(0)
    # print(dict)
    # print(dict[-1])
    ref = str(dict[-1])
    ref = ref.rstrip("'")
    dict2 = ref.rsplit(",", 6)
    for element in dict2[2:]:
        print(element)
        Irradiation = Irradiation + float(element)
        # Irradiation_list.append(element)

    Irradiation = Irradiation / 4
    print("Irradiation: ", Irradiation)
    print(dict2[2:])
    Energy = Area * Pr * (50/100 * Irradiation) * r
    print("\n \n \n Energy = {0}".format(Energy))
    electricity_cost = Energy * (cst/100)
    print("\n \n \n Electricity cost per Year", electricity_cost)
    electricity_cost = electricity_cost * 12
    overall = (electricity_cost / 21090) * 100
    if overall >= 100:
        overall = overall - 100
    print("Overall Profitability: {} % ".format(round(overall), 3))
    overall = round(overall, 3)
    overall = str(overall) + " %"
    return overall
