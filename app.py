from flask import Flask
from flask import render_template,session,redirect,request,url_for


app=Flask(__name__)
app.secret_key = "ULTIMATEMURDERHUIDE"

@app.route('/',methods=["POST","GET"])
def home():
        if request.method == 'GET':
                return render_template("Home.html")
                 
if __name__ == "__main__":
        app.debug = True
        app.run()
