# -API-Development-with-Flask-and-PostgreSQL

This repository contains a Python-based solution for extracting, transforming, and loading (ETL) order data into a PostgreSQL database, and then exposing that data through a RESTful API built with Flask.

## Features

**Data Ingestion**:
 - Reads order data from a CSV file using Pandas.
 - Cleans and preprocesses data by handling missing values ('Not Available', 'unknown'), standardizing column names (lowercase, underscores), and converting data types (e.g., order_date to datetime).
 - Calculates essential business metrics such as discount, sale_price, and profit from raw data.
 - Loads processed data into a PostgreSQL database using Psycopg2, ensuring efficient bulk inserts.
 - Intelligently manages database tables: it truncates the df_orders table if it already exists, or creates it with a predefined schema if it's new, preventing data duplication or schema conflicts.

**RESTful API**:
 - Provides real-time access to individual order records via a Flask-based API.
 - Features a /getorder/<int:order_id> endpoint that allows users to retrieve specific order details by their order_id.
 - Ensures secure and efficient database connections using environment variables.
 - Returns order data in a clear JSON format, making it easy to integrate with other applications.

## Project Structure
**python to postgresql.py**: The script responsible for reading, transforming, and loading the CSV data into PostgreSQL.

**api.py**: The Flask application that exposes the order data via a RESTful API.

**README.md**: This file.

**orders.csv**: The unedited base CSV data file. You'll need to specify its path via an environment variable.

**orders cleaned up.csv**: What the file would look like after running 'python to postgresql.py' 

## Setup and Installation
**Prerequisites**
Before running the scripts, ensure you have the following installed:

 - Python 3.x
 - PostgreSQL database
 - pip (Python package installer)

**Environment Variables**
Both scripts rely on environment variables for sensitive information (like database credentials) and file paths. Set the following variables in your environment (e.g., in a .env file and loaded with python-dotenv, or directly in your shell):

CSV_FILE_PATH: The absolute path to your order CSV file (e.g., /path/to/your_data.csv).

DB_HOST: Your PostgreSQL database host (e.g., localhost).

DB_NAME: Your PostgreSQL database name (e.g., postgres).

DB_USER: Your PostgreSQL database username.

DB_PASSWORD: Your PostgreSQL database password.

DB_PORT: Your PostgreSQL database port (default: 5432).


Example (for Linux/macOS):
```Bash
export CSV_FILE_PATH="/path/to/orders.csv"
export DB_HOST="localhost"
export DB_NAME="postgres"
export DB_USER="postgres"
export DB_PASSWORD="examplepassword123"
export DB_PORT="5432"
```

**Install Dependencies**
Navigate to your project directory and install the required Python libraries:

```Bash
pip install pandas psycopg2-binary Flask
```

## Usage
**1. Load Data into PostgreSQL**

First, run the data processing script to populate your database:

```Bash
python data_processing_script.py
```
This script will:
- Read your CSV data.
- Perform data cleaning and transformations.
- Connect to your PostgreSQL database.
- Truncate the df_orders table (if it exists) or create it (if it doesn't).
- Insert the processed data into the df_orders table.

**2. Run the Flask API**

Once the data is loaded, start the Flask API server:

```Bash
python api_app.py
```

The API will typically run on http://127.0.0.1:5000 (or localhost:5000) in debug mode.

**3. Accessing the API**

You can access order data by sending GET requests to the /getorder/<order_id> endpoint. Replace <order_id> with the actual ID of the order you want to retrieve.

Example using curl:

```Bash
curl http://127.0.0.1:5000/getorder/537
```

Example JSON Response:

```JSON
{
    "city": "Columbus",
    "category": "Technology",
    "country": "United States",
    "discount": 10.0,
    "order_date": "2023-01-15",
    "order_id": 12345,
    "postal_code": 43229,
    "product_id": "TEC-PH-10000000",
    "profit": 50.0,
    "quantity": 2,
    "region": "East",
    "sale_price": 100.0,
    "segment": "Consumer",
    "ship_mode": "Standard Class",
    "state": "Ohio",
    "sub_category": "Phones"
}
```
