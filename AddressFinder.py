#Address finder in just a seconds by -Ashutosh Pandey
import urllib.parse
import requests
main_api='https://maps.googleapis.com/maps/api/geocode/json?'
print("Welcome to my Address Finder:")
#address='lhr'
while True:
    address=input("Enter the query which you want to find or type q for quit")
    if address=="q":
        break
    url=main_api+urllib.parse.urlencode({"address":address})
    json_data=requests.get(url).json()
    #print(json_data)
    json_status=json_data['status']
    #print('API Status:'+json_status)
    if json_status=='OK':
        '''for each in json_data['results'][0]['address_components']:
            print(each['long_name'])
            print(each['types'])'''
        #print(url)
        formatted_address=json_data['results'][0]['formatted_address']
        print(formatted_address)
