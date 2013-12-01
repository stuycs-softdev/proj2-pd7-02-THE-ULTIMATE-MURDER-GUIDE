from googlemaps import GoogleMaps

def convert(address):
    api_key= AIzaSyB8BMVcgDDaxWB5kVxgQD9jT5Nsg58cA2c
    gmaps=GoogleMaps(api_key)
    lat, lng = gmaps.address_to_latlng(address)
    return lat,lang

def location(address):
    api_key= AIzaSyB8BMVcgDDaxWB5kVxgQD9jT5Nsg58cA2c
    gmaps=GoogleMaps(api_key)
    local = gmaps.local_search('Park near ' + destination)
    return local['responseData']['results'][0]['titleNoFormatting']
