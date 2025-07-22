from flask import Flask, request, jsonify
import psycopg2 as pg
import os
app = Flask(__name__)

def get_db_connection():
    try:
        conn = pg.connect(
    host=os.getenv('DB_HOST', 'localhost'),
    database=os.getenv('DB_NAME', 'postgres'),
    user=os.getenv('DB_USER', 'postgres'),
    password=os.getenv('DB_PASSWORD'),
    port=os.getenv('DB_PORT', '5432')
)
        return conn
    except pg.Error as e:
        print(f"Error connecting to the databse: {e}")
        return None
    
get_db_connection()

@app.route('/getorder/<int:order_id>', methods=['GET'])
def get_order_data(order_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM df_orders WHERE order_id = %s;', (order_id,))
    order = cursor.fetchone()
    cursor.close()
    conn.close()
    
    return jsonify({
        'order_id': order[0],
        'order_date': order[1],
        'ship_mode': order[2], 
        'segment': order[3], 
        'country' : order[4], 
        'city': order[5], 
        'state': order[6], 
        'postal_code': order[7], 
        'region': order[8], 
        'category': order[9], 
        'sub_category': order[10], 
        'product_id': order[11], 
        'quantity': order[12], 
        'discount': order[13], 
        'sale_price': order[14], 
        'profit': order[15],
    })

if __name__ == '__main__':
    app.run(debug=True)
