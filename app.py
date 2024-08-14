
from flask import Flask, jsonify

app = Flask(__name__)

data_store = {}

# Simulate fetching data from an external service
def fetch_data_from_external_service():
    # Mock data simulating external service response
    return {
        'items': [
            {'id': 1, 'name': 'Product A', 'price': 100},
            {'id': 2, 'name': 'Product B', 'price': 200},
            {'id': 3, 'name': 'Product C', 'price': 300}
        ]
    }

# Function to process the fetched data
def process_data(data):
    # Example processing: Convert item names to uppercase
    processed_data = {
        'items': [
            {'id': item['id'], 'name': item['name'].upper(), 'price': item['price']}
            for item in data['items']
        ]
    }
    return processed_data

# Endpoint to fetch and process data
@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    global data_store
    data = fetch_data_from_external_service()
    data_store['processed_data'] = process_data(data)
    return jsonify(data_store['processed_data']), 200

# Endpoint to get processed data
@app.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    if 'processed_data' in data_store:
        return jsonify(data_store['processed_data']), 200
    else:
        return jsonify({'message': 'No data available'}), 404

if __name__ == '__main__':
    app.run(debug=True)
# # app.py

# from flask import Flask, jsonify

# app = Flask(__name__)

# # Simulated in-memory storage
# data_store = {}

# # Simulate fetching data from an external service
# def fetch_data_from_external_service():
#     # Mock data simulating external service response
#     return {
#         'items': [
#             {'id': 1, 'name': 'Product A', 'price': 100},
#             {'id': 2, 'name': 'Product B', 'price': 200},
#             {'id': 3, 'name': 'Product C', 'price': 300}
#         ]
#     }

# # Function to process the fetched data
# def process_data(data):
#     # Example processing: Convert item names to uppercase
#     processed_data = {
#         'items': [
#             {'id': item['id'], 'name': item['name'].upper(), 'price': item['price']}
#             for item in data['items']
#         ]
#     }
#     return processed_data

# # Endpoint to fetch and process data
# @app.route('/fetch-data', methods=['GET'])
# def fetch_data():
#     global data_store
#     data = fetch_data_from_external_service()
#     data_store['processed_data'] = process_data(data)
#     return jsonify(data_store['processed_data']), 200

# # Endpoint to get processed data
# @app.route('/get-processed-data', methods=['GET'])
# def get_processed_data():
#     if 'processed_data' in data_store:
#         return jsonify(data_store['processed_data']), 200
#     else:
#         return jsonify({'message': 'No data available'}), 404

# if __name__ == '__main__':
#     app.run(debug=True)
