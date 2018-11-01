import json, requests

GOOGLE_API_KEY = 'AIzaSyAs-V12J7qfvNlCK4ILfOcbo8YruNY8x3k'

def translate(address, city, state):
    r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?'
                     'address={}+{}+{}&key=AIzaSyAs-V12J7qfvNlCK4ILfOcbo8YruNY8x3k'.format(
                         address, city, state))
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return json.loads(r.content.decode('utf-8-sig'))
	
def toURL(text):
    text.replace(" ", "+")
    return text
	
def toRows(file):
    rows = file.splitlines()
    return rows
	
def toJSON(string):
    tuple = string.split(',')
    data = translate(toURL(tuple[1]), toURL(tuple[2]), toURL(tuple[3]))
    return data
	
def writeHTML(js):
    lat = js['geometry']['location']['lat']
	lng = js['geometry']['location']['lng']
    return "<p>Latitude: " + lat + " Longitude: " + lng + "</p>"
