#! flask/bin/python

import sys

from flask import Flask, render_template, request, redirect, Response
from geocode import translate, toURL
import random, json, urllib, time

app = Flask(__name__)

@app.route('/')
def output():
    # serve index template
	return render_template('index.html', page_title='Hello World')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    return render_template('upload_page.html', info=request)
    #if request.method == 'POST':
	#    f = request.files['file']
	#    f.save('/uploads/uploaded_file.txt')
	#    return render_template('upload_page.html', info='hahahaha')

@app.route('/geo_address', methods=['GET', 'POST'])		
def geoApi():
    js = translate(toURL(request.form['main_add']), toURL(request.form['city_add']), toURL(request.form['state_add']))
    if js['status'] == 'OK':
	    latitude = js['geometry']['location']['lat']
	    longitude = js['geometry']['location']['lng']
	    return render_template('address_page.html', lat=latitude, lng=longitude, info="")
    else:
        return render_template('address_page.html', lat="", lng="", info=js)
	
if __name__ == 'main':
    app.run()
