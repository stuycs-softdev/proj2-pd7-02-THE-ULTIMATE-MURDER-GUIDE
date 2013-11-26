from flask import Flask
from flask import render_template,session,redirect,request,url_for

<<<<<<< HEAD

app = Flask(__name__)
app.secret_key = "BLOGINATOR"


@app.route('/',methods=['POST','GET'])
def home():
=======
app = Flask(__name__)
app.secret_key = "ULTIMATEMURDERGUIDE"

@app.route('/',methods=['POST','GET'])
def home():
if request.method == 'GET':
>>>>>>> master
        return render_template('Home.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
