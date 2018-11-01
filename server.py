#! flask/bin/python

import sys

from flask import Flask, render_template, request, redirect, Response
from geocode import translate, toURL, toRows, toJSON, writeHTML
import random, json, urllib, time, csv

app = Flask(__name__)

@app.route('/')
def output():
    # serve index template
	return render_template('index.html', page_title='Hello World')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    #return render_template('upload_page.html', info=request)
    if request.method == 'POST':
	    f = request.files['file']
	    csvfile = f.read()
	    rows = toRows(csvfile)
	    string = ""
	    for row in rows:
		    string += writeHTML(toJSON(row))
	    f.close()
	    return render_template('upload_page.html', info=string)

@app.route('/geo_address', methods=['GET', 'POST'])		
def geoApi():
    js = translate(toURL(request.form['main_add']), toURL(request.form['city_add']), toURL(request.form['state_add']))
    if js['status'] == 'OK':
	    string = writeHTML(js)
	    return render_template('address_page.html', info=string)
    else:
        return render_template('address_page.html', info=js)
	
if __name__ == 'main':
    app.run()
