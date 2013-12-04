from flask import Flask
from flask import render_template,session,redirect,request,url_for
import urllib2
import method
from googlemaps import GoogleMaps
import mapsmethod


app=Flask(__name__)
app.secret_key = "ULTIMATEMURDERGUIDE"

@app.route('/',methods=["POST","GET"])
def home():
        if request.method == 'GET':
                return render_template("Home.html")

@app.route('/home',methods=["POST","GET"])
def hometwo():
        if request.method == 'GET':
                return render_template("Home.html")

@app.route('/weather',methods=["POST","GET"])
def weather():
        if request.method == 'GET':
		blah = '11209'
		link = 'http://api.wunderground.com/api/01c5e2f1dd1d7086/conditions/q/' + blah + '.json'
		connection = urllib2.urlopen(link)
		response = connection.read()
		a = method.temperature(response)
		b = method.winds(response)
		c = method.rainfall(response)
		d = link[(link.find('conditions') + 13):(link.find('conditions') + 18)]
		link = 'http://api.wunderground.com/api/01c5e2f1dd1d7086/forecast/q/10007.json'
		connection = urllib2.urlopen(link)
		response = connection.read()
		e = method.img(response,1)
		f = method.img(response,3)
		g = method.img(response,5)
		h = method.img(response,7)
		i = method.stat(response,1)
		j = method.stat(response,3)
		k = method.stat(response,5)
		l = method.stat(response,7)
		m = method.today(response)
		n = method.tomorrow(response)
		o = method.datomorrow(response)
		p = method.edtomorrow(response)

                return render_template("Weather.html", temp = a, winds = b, rainfall = c, zips = d, icona = e, iconb = f, iconc = g, icond = h, today = i, tomorrow = j, datomorrow = k, edtomorrow = l, day1 = m, day2 = n, day3 = o, day4 = p)

	else: 
		zipcode = request.form['Zip'].encode('ascii','ignore')
		blah = str(zipcode)
		link = 'http://api.wunderground.com/api/01c5e2f1dd1d7086/conditions/q/' + blah + '.json'
		connection = urllib2.urlopen(link)
		response = connection.read()
		a = method.temperature(response)
		b = method.winds(response)
		c = method.rainfall(response)
		d = link[(link.find('conditions') + 13):(link.find('conditions') + 18)]
		link = 'http://api.wunderground.com/api/01c5e2f1dd1d7086/forecast/q/' + blah + '.json'
		connection = urllib2.urlopen(link)
		response = connection.read()
		e = method.img(response,1)
		f = method.img(response,3)
		g = method.img(response,5)
		h = method.img(response,7)
		i = method.stat(response,1)
		j = method.stat(response,3)
		k = method.stat(response,5)
		l = method.stat(response,7)

                return render_template("Weather.html", temp = a, winds = b, rainfall = c, zips = d, icona = e, iconb = f, iconc = g, icond = h, today = i, tomorrow = j, datomorrow = k, edtomorrow = l)


@app.route('/maps',methods=["POST","GET"])
def maps():
        if request.method == 'GET':
		function = """
          function initialize() {     
      var mapOptions = {
      center: new google.maps.LatLng(-34.397, 150.644),
      zoom: 8
      };
      var map = new google.maps.Map(document.getElementById("map-canvas"),
      mapOptions);
      }
      google.maps.event.addDomListener(window, 'load', initialize);
          """
                return render_template("Maps.html", jscripts = function)
        else:
		link = 'http://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&sensor=true'
		connection = urllib2.urlopen(link)
		response = connection.read()
		function = """function initialize() {
          var JSONObject = """ + str(response) + """;
	  var lat = JSONObject.results.geometry.location.lat
	  var lng = JSONObject.results.geometry.location.lng
          var mapOptions = {
          center: new google.maps.LatLng(lat, lng),
          zoom: 8
          };
          var map = new google.maps.Map(document.getElementById("map-canvas"),
            mapOptions);
          }
          google.maps.event.addDomListener(window, 'load', initialize);"""
                return render_template("Maps.html",jscripts = function)

@app.route('/lawyer',methods=["POST","GET"])
def lawyer():
        if request.method == 'GET':
                return render_template("Lawyer.html")
	
if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port =7002)
