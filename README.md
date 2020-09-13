# AdityaAirgarageChallenge


## Requirements to run this application
- Must have Python3 installed, preferabely Python 3.7
- Have Pip3 installed as well



## How to run this application (on Linux or Mac)
  1. clone this repository using the command ` git clone https://github.com/adialachar/AdityaAirgarageChallenge.git ` in your terminal and enter the directory that has just been created with `cd AdityaAirgarageChallenge`
  2. Install virtualenv with the command `pip3 install virtualenv`
  3. Create a new virtual environment called myenv with the command `virtualenv myenv`
  4. Activate the virtual environment with `souce myenv/bin/activate` for Mac or `source ./myenvenv/bin/activate` for Linux
  5. Install the necessary packages with the command `pip3 install -r requirements.txt`
  6. Create a file called `secrets.py` in the `AdityaAirgarageChallenge` directory. In that file create a variable called `yelp_api_key` and assign it to the Yelp API Key. The file should look like 
  ```
  yelp_api_key = "API-KEY-GOES-HERE"
  ```
  7. Launch the application with `python3 app.py` and go to localhost:5000 in your browser
  
