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
        # todo: check if location is none, return empty list + error message
        url = "https://api.yelp.com/v3/businesses/search"
        payload = {'location':location, "term":"Parking Garage"}
        headers = {'Authorization': 'Bearer ' + yelp_api_key}
        r = requests.get(url, headers=headers, params=payload)

        p_g = r.json().get("businesses")
        p_g = sorted(p_g, key=lambda k: k['rating'])
        # print(p_g)
        # image if available
        # star rating
        # review count
        # link to the yelp page
        parking_garages = []

        for p in p_g:
            d = {}
            d['name'] = p.get('name'), 
            d['address'] = ' '.join(p.get('location').get('display_address')), 
            d['image_url'] = p.get("image_url")
            d['review_count'] = p.get('review_count'),
            d['rating'] = p.get('rating'), 
            d['url'] = p.get("url")
        
            # score calculation
            # score = ( number of reviews * rating ) / (number of reviews + 1)
            score = ( int(p.get("review_count")) * float(p.get('rating')) / int(p.get("review_count")) + 1) 
            d['score'] = score

            parking_garages.append(d)



    return render_template('home.html', parking_garages=parking_garages)

if __name__ == "__main__":
    app.run(debug=True)