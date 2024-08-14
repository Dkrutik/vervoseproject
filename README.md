# Flask Data Processing Application

## Overview

This is a simple Flask application that simulates a data retrieval and processing system. It includes the following features:

1. **API Endpoint `/fetch-data`**: Simulates fetching data from an external service, processes it, and stores it in temporary in-memory storage.
2. **API Endpoint `/get-processed-data`**: Retrieves the processed data from the in-memory storage.

## Requirements

- Python 3.x
- Flask

## Installation

1. Clone or download the repository.
2. Navigate to the project directory.
3. Install Flask using pip:

    ```bash
    pip install flask
    ```

## Running the Application

1. Start the Flask application by running:

    ```bash
    python app.py
    ```

2. The application will be accessible at `http://127.0.0.1:5000`.

## Endpoints

- **GET `/fetch-data`**: Fetches and processes data. Returns the processed data.
- **GET `/get-processed-data`**: Returns the processed data stored in memory.

## Example Requests

- Fetch data and process it:

    ```bash
    curl http://127.0.0.1:5000/fetch-data
    ```

- Retrieve processed data:

    ```bash
    curl http://127.0.0.1:5000/get-processed-data
    ```
