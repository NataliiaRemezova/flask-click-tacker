from flask import Flask, render_template, request, jsonify
import json

# Initializing the app
app = Flask(__name__, template_folder='templates')

# Creating the array to store the clicks
clicks = []

# Defining the route and rendering the remplate
@app.route('/')
def index():
    return render_template('index.html')

# Defining the route to handle POST requests and add timestamps of the clicks to the array
@app.route('/clicks', methods=['POST'])
def store_click():
    try: # error handling
        data = request.get_json() # getting the JSON from the POST reques (from JS)
        timestamp = data.get('timestamp') # getting the timestamp code from the JSON
        if timestamp is not None:
            clicks.append(timestamp) # adding the timestamp to the
            return jsonify(message='Click added successfully'), 201 # return response code
            # jsonify converts Python dictionary into JSON response
        else:
            return jsonify(error='Invalid JSON data'), 400 # error handling
    except Exception as e:
        return jsonify(error='An error occurred'), 500 # error handling

# Defining the route to handle GET requests and get the timestamps of the clicks
@app.route('/clicks', methods=['GET'])
def get_clicks():
    return jsonify({'clicks': clicks}) # return JSON with the contents of the array clicks

if __name__ == '__main__':
    app.run(debug=True)
