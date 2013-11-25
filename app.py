from flask import Flask, session, redirect, request, url_for, render_template

app = Flask(__name__)
app.secret_key = 'Murder'

@app.route('/welcome')
def welcome():
    return render_template ("welcome.html")
@app.route('/location')
def location():
    return render_template ("location.html")
@app.route('/weather')
def weather():
    return render_template ("weather.html")
@app.route ('/lawsuit')
def lawsuit():
    return render_template ("lawsuit.html")



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port =9000)
                        
                    
