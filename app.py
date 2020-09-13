from flask import Flask, render_template, request
import requests
from secrets import yelp_api_key
app = Flask(__name__)

# basic endpoint, returns the home.html file in the templates dir
@app.route('/', methods=['GET','POST'])
def main():
    parking_garages = []
    if request.method == "POST":
        print(request.form.get('location'))
        location = request.form.get('location')

        url = "https://api.yelp.com/v3/businesses/search"
        payload = {'location':location, "term":"Parking Garage"}
        headers = {'Authorization': 'Bearer ' + yelp_api_key}
        r = requests.get(url, headers=headers, params=payload)

        p_g = r.json().get("businesses")
        p_g = sorted(p_g, key=lambda k: k['rating'])

        parking_garages = []

        # extract data from api
        for p in p_g:
            d = {}
            d['name'] = p.get('name')
            d['address'] = ' '.join(p.get('location').get('display_address'))
            d['image_url'] = p.get("image_url")
            d['review_count'] = p.get('review_count')
            d['rating'] = p.get('rating')
            d['url'] = p.get("url")

            # score calculation
            # score = ( number of reviews * rating ) / (number of reviews + 1)
            score = ( int(p.get("review_count")) * float(p.get('rating')) / int(p.get("review_count")) + 1) 
            d['score'] = score
            print(d)
            parking_garages.append(d)

        parking_garages = list({v['name']:v for v in parking_garages}.values())


    #return data to html page
    return render_template('home.html', parking_garages=parking_garages)

if __name__ == "__main__":
    app.run(debug=True)