import urllib.request as urllib2
dict = {}


def main():
    # open a connection to a URL using urllib2
    webUrl = urllib2.urlopen(
        "https://midcdmz.nrel.gov/apps/plot.pl?site=BMS&start=20200101&live=1&zenloc=222&amsloc=224&time=1&inst=103&inst=104&inst=105&inst=106&inst=107&inst=108&inst=109&inst=110&type=data&wrlevel=6&preset=0&first=3&math=0&second=-1&value=0.0&global=-1&direct=-1&diffuse=-1&user=0&axis=1")

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
    print(dict[-1])
    for row in data:
        '''if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1'''
        # print(row)
    # print(data)


if __name__ == "__main__":
    main()
