from flask import Flask, jsonify
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load data from CSV
df = pd.read_csv('subway_location.csv')

@app.route('/')
def index():
    return 'Welcome to Subway Locations API!'

@app.route('/locations')
def get_locations():
    # Convert DataFrame to JSON and return
    return jsonify(df.to_dict(orient='records'))

@app.route('/location/<int:index>')
def get_location(index):
    # Get location details by index
    if index >= 0 and index < len(df):
        return jsonify(df.iloc[index].to_dict())
    else:
        return jsonify({'error': 'Index out of range'}), 404

if __name__ == '__main__':
    app.run(debug=True)