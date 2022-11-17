# app.py file for Flask app

from flask import Flask,render_template

# Create the app
app = Flask(__name__)

# Create a homepage for the app
@app.route("/")
# When we go to our.URL.com/
    # Then flask will run this function below

    # In our function, we will "return" 
    # the HTML that we want flask to serve
def home_page():
    return render_template("base.html")

@app.route("/user/Herbert")

def about_page():
    return 'hello,Herbert'

 