from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__, template_folder='templates')

clicks = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clicks', methods=['POST'])
def store_click():
    try: 
        data = request.get_json() 
        timestamp = data.get('timestamp') 
        if timestamp is not None:
            clicks.append(timestamp) 
            return jsonify(message='Click added successfully'), 201
        else:
            return jsonify(error='Invalid JSON data'), 400 
    except Exception as e:
        return jsonify(error='An error occurred'), 500 


@app.route('/clicks', methods=['GET'])
def get_clicks():
    return jsonify({'clicks': clicks})

if __name__ == '__main__':
    app.run(debug=True)
