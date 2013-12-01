from googlemaps import GoogleMaps

def convert(address):
    gmaps=GoogleMaps(AIzaSyB8BMVcgDDaxWB5kVxgQD9jT5Nsg58cA2c)
    lat, lng = gmaps.address_to_latlng(address)
    return lat,lang

def location(address):
    gmaps=GoogleMaps(AIzaSyB8BMVcgDDaxWB5kVxgQD9jT5Nsg58cA2c)
    local = gmaps.local_search('Park near ' + destination)
    return local['responseData']['results'][0]['titleNoFormatting']
