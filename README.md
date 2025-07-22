# -API-Development-with-Flask-and-PostgreSQL

This script loads data from a CSV file into a PostgreSQL database table. It performs several data cleaning and transformation steps before inserting the data.

## Features

- Reads data from a CSV file.
- Handles 'Not Available' and 'unknown' values as NULL.
- Converts column names to lowercase and replaces spaces with underscores.
- Calculates derived columns: `discount`, `sale_price`, and `profit`.
- Converts `order_date` column to datetime objects.
- Drops unnecessary columns (`list_price`, `cost_price`, `discount_percent`) after calculations.
- Checks if the target table (`df_orders`) exists in the PostgreSQL database.
    - If the table exists, it truncates the table.
    - If the table does not exist, it creates the table with a predefined schema.
- Inserts the processed data from the DataFrame into the `df_orders` table.

## Dependencies

- pandas
- psycopg2

You can install these dependencies using pip:
```bash
pip install pandas psycopg2-binary
```

## Configuration

The script uses environment variables for configuration. Create a `.env` file in the same directory as the script with the following variables:

```env
CSV_FILE_PATH='path/to/your/orders.csv'  # Default: n/a
DB_HOST='your_db_host'                   # Default: 'localhost'
DB_NAME='your_db_name'                   # Default: 'postgres'
DB_USER='your_db_user'                   # Default: 'postgres'
DB_PASSWORD='your_db_password'           # Default: n/a
DB_PORT='your_db_port'                   # Default: '5432'
```

If these environment variables are not set, the script will use the default values specified in the code. Some default values are not present and environnment variables for these must be set

## Usage

1.  **Set up your PostgreSQL database:** Ensure you have a PostgreSQL server running and accessible.
2.  **Create a `.env` file** (as described in the Configuration section) or ensure the default values in the script are correct for your setup.
3.  **Place your CSV file** at the location specified by `CSV_FILE_PATH`. The CSV file is expected is to be `orders.csv`
4.  **Run the script:**
    ```bash
    python "python to postgresql"
    ```
    (Note: If your Python script file is named `python to postgresql.py`, use `python "python to postgresql.py"`)

The script will connect to the database, process the CSV data, and load it into the `df_orders` table.

## Script Overview

The script performs the following main steps:

1.  **Import Libraries:** Imports `pandas` for data manipulation and `psycopg2` for PostgreSQL interaction.
2.  **Load CSV Data:**
    *   Reads the CSV file specified by the `CSV_FILE_PATH` environment variable (or a default path) into a pandas DataFrame.
    *   Replaces 'Not Available' and 'unknown' strings with NaN (which will become NULL in the database).
3.  **Data Transformation:**
    *   Converts all column names to lowercase.
    *   Replaces spaces in column names with underscores.
    *   Calculates `discount`, `sale_price`, and `profit` columns.
    *   Rounds `discount` and `profit` to two decimal places.
    *   Converts the `order_date` column to datetime objects.
    *   Drops the original `list_price`, `cost_price`, and `discount_percent` columns.
4.  **Database Connection:**
    *   Establishes a connection to the PostgreSQL database using credentials from environment variables (or default values).
5.  **Table Management (`table_exists_psycopg2` function):**
    *   Checks if the `df_orders` table exists.
    *   If it exists, the table is truncated (all existing data is removed).
    *   If it doesn't exist, a new table `df_orders` is created with a specific schema.
6.  **Data Insertion (`execute_values` function):**
    *   Converts the DataFrame rows into a list of tuples.
    *   Uses `psycopg2.extras.execute_values` for efficient bulk insertion of data into the `df_orders` table.
    *   Commits the transaction upon successful insertion or rolls back in case of an error.
7.  **Verification (Optional):**
    *   The script includes a line `cursor.execute('SELECT * FROM df_orders')` which can be used for basic verification that data was inserted. However, it doesn't print the results. You would typically query the database separately to confirm.
8.  **Cleanup:** Closes the database cursor and connection.
