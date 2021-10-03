def livestream():
    from geopy.geocoders import Nominatim
    import csv
    import requests
    import requests
    import json
    Area = 6.1316
    r = 15.3
    Pr = 0.75
    dict = {}
    dict2 = []
    refvar = 2
    Irradiation_list = []
    refdict = {}
    global val
    global ctry
    cnt = ""
    #from Global_Data import Irradiation
    send_url = "http://api.ipstack.com/check?access_key=716837ec670b004b7728dfe71a174afd"
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    latitude = geo_json['latitude']
    longitude = geo_json['longitude']
    city = geo_json['city']
    location1 = "https://www.google.com/maps?q={},{}".format(
        latitude, longitude)
    print(location1)
    cookies = {
        '72433e29e5a9aabda23011a87312c9f6': '95caff22feff53d170254d75a7038a05',
        '_ga': 'GA1.2.578532231.1633194278',
        '_gid': 'GA1.2.126791236.1633194278',
        'isfirst_undefined': 'false',
        '_gat': '1',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://power.larc.nasa.gov/data-access-viewer/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    params = (
        ('parameters', 'T2M,T2MDEW,T2MWET,TS,T2M_RANGE,T2M_MAX,T2M_MIN'),
        ('community', 'RE'),
        ('longitude', longitude),
        ('latitude', latitude),
        ('start', '20211003'),
        ('end', '20211003'),
        ('format', 'JSON'),
        ('user', 'DAV'),
    )

    response = requests.get('https://power.larc.nasa.gov/api/temporal/daily/point',
                            headers=headers, params=params, cookies=cookies, verify=False)
    print(response.text)
    Irradiation = {}
    '''Irradiation = response.text
    print("\n ", Irradiation)'''
    Irradiation = json.loads(response.text)
    #Irradiation = json.loads(response.read())
    print("\n ", Irradiation.keys())
    #print("\n ", Irradiation['properties'])
    properties = Irradiation['properties']
    print("\n param", properties.keys())
    print("\n param", properties)
    param = properties['parameter']
    T2M = param['T2M']

    print("\n T2M", T2M.keys())
    #value = T2M.keys()
    for key, value in T2M.items():
        value = abs(value)
        val = value
    # getting location

    # getting location
    # geolocator
    geolocator = Nominatim(user_agent="geoapiExercises")

    Lati = str(latitude)
    Longi = str(longitude)

    location = geolocator.reverse(Lati+","+Longi)

    print("\n \n \n", location)

    location = str(location)
    list_5 = location.split(',')
    print(list_5)
    print("\n \n \n")
    ctry = str(list_5[-1])
    state = str(list_5[-2])+str(list_5[-1])
    ctry = ctry.lstrip(" ")
    print(ctry)
    # geolocator

    # sorting country value
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
    # sorting country
    val = val / 4
    print("Irradiation: ", val)
    print(dict2[2:])
    cst = 12.1
    Energy = Area * Pr * (50/100 * val) * r
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
