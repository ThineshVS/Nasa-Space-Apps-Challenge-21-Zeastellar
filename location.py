import requests
import json
send_url = "http://api.ipstack.com/check?access_key=716837ec670b004b7728dfe71a174afd"
geo_req = requests.get(send_url)
geo_json = json.loads(geo_req.text)
latitude = geo_json['latitude']
longitude = geo_json['longitude']
city = geo_json['city']
location1 = "https://www.google.com/maps?q={},{}".format(
    latitude, longitude)
# st.write(location1)
#submit = st.button('Submit')
