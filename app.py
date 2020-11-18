from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
import csv

app = Flask(__name__,template_folder='.')

@app.route('/',methods=['GET'])
def main():
        return render_template("wordAffiliation.html")

@app.route('/', methods=['POST'])
def getcsv():

	if request.method == 'POST':

		file = request.files['data_file']
		if not file:
			return "no file"

		file_contents = file.stream.read().decode("utf-8")
		csv_input = csv.reader(file_contents)

		#implementation

		return render_template("wordAffiliation.html",output = type(file_contents))

@app.route('/synonyms', methods=['POST'])
def synonyms():

	if request.method == 'POST':

		word = str(request.form['synonyms'])

		#implementation

		return render_template("wordAffiliation.html",synonyms='')


@app.route('/antonyms', methods=['POST'])
def antonyms():

	if request.method == 'POST':

		word = str(request.form['antonyms'])

		#implementation

		return render_template("wordAffiliation.html",antonyms='')

@app.route('/wordrelations', methods=['POST'])
def wordrelations():

	if request.method == 'POST':

		w1 = str(request.form['word1'])
		w2 = str(request.form['word2'])
		w3 = str(request.form['word3'])

		#implementation

		return render_template("wordAffiliation.html",word4='')

if __name__ == "__main__":
    app.run(debug=True)