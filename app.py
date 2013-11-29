from flask import Flask
from flask import render_template,session,redirect,request,url_for
import requests

app=Flask(__name__)
app.secret_key = "ULTIMATEMURDERGUIDE"

@app.route('/home',methods=["POST","GET"])
def home():
        if request.method == 'GET':
                return render_template("Home.html")
@app.route('/weather',methods=["POST","GET"])
def weather():
        if request.method == 'GET':
		blah =  "http://api.wunderground.com/api/01c5e2f1dd1d7086/conditions/q/11209.json"
                return render_template("Weather.html", blah = blah)
@app.route('/maps',methods=["POST","GET"])
def maps():
        if request.method == 'GET':
                return render_template("Maps.html")
@app.route('/lawyer',methods=["POST","GET"])
def lawyer():
        if request.method == 'GET':
                return render_template("Lawyer.html")
                 
if __name__ == "__main__":
        app.debug = True
        app.run()
