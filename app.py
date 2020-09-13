from flask import Flask, render_template
import requests

app = Flask(__name__)

# basic endpoint, returns the home.html file in the templates dir
@app.route('/', methods=['GET','POST'])
def main():

    


    return render_template('home.html')

if __name__ == "__main__":
    app.run()