#! flask/bin/python

import sys

from flask import Flask, render_template, request, redirect, Response
import random, json, urllib, time

app = Flask(__name__)

@app.route('/')
def output():
    # serve index template
	return render_template('index.html', page_title='Hello World')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
	    f = request.files['the_file']
	    f.save('/uploads/uploaded_file.txt')
	    return 'saved file'

@app.route('/geo_address', method="post")		
def geoApi(address, api="", delay=5)
    base = "https://maps.googleapis.com/maps/api/geocode/json?"
	addP = "address=" + address.replace(" ", "+")
	geoURL = base + addP + "&key" + api
	response = urllib.urlopen(geoURL)
	jsonData = json.loads(response.read())
	if jsonData['status'] == 'OK':
	    resu = jsonData['results'][0]
		finList = [resu['formatted_address'], resu['geometry']['location']['lat'], resu['geometry']['location']['lng']]
	else:
	    finList = [None, None, None]
	time.sleep(delay)
	return finList
	
if __name__ == 'main':
    app.run()
