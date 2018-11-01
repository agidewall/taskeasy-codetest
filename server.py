#! flask/bin/python

import sys

from flask import Flask, render_template, request, redirect, Response
from geocode import translate
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

@app.route('/geo_address', methods=['GET', 'POST'])		
def geoApi():
    js = translate('201+E+South+Temple', 'Salt+Lake+City', 'UT')
    return render_template('address_page.html', info=js)
	
if __name__ == 'main':
    app.run()
