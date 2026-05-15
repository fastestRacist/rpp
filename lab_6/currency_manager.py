from flask import Flask, request
import psycopg2


app = Flask(__name__)


connection = psycopg2.connect(
    host = 'localhost',
    database = 'currencies',
    user = 'postgres',
    password = 'postgres'
)


@app.route('/load', methods=['POST'])
def load_currency():
    data = request.json

    currency_name = data['currency_name']
    rate = data['rate']

    cursor = connection.cursor()

    cursor.execute('SELECT * FROM currencies WHERE currency_name = %s', (currency_name,))

    currency = cursor.fetchone()

    if currency is None:
        cursor.execute('INSERT INTO currencies (currency_name, rate) VALUES (%s, %s)', (currency_name, rate))

        connection.commit()

    cursor.close()

    return 'OK', 200


@app.route('/update_currency', methods=['POST'])
def update_currency():
    data = request.json

    currency_name = data['currency_name']
    rate = data['rate']

    cursor = connection.cursor()

    cursor.execute('SELECT * FROM currencies WHERE currency_name = %s', (currency_name,))

    currency = cursor.fetchone()

    if currency is not None:
        cursor.execute('UPDATE currencies SET rate = %s WHERE currency_name = %s', (rate, currency_name))

        connection.commit()

    cursor.close()

    return 'OK', 200


@app.route('/delete', methods=['POST'])
def delete_currency():
    data = request.json
    currency_name = data['currency_name']
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM currencies WHERE currency_name = %s', (currency_name,))

    currency = cursor.fetchone()

    if currency is not None:
        cursor.execute('DELETE FROM currencies WHERE currency_name = %s', (currency_name,))
        connection.commit() 
    
    cursor.close()
    return 'OK', 200

if __name__ == '__main__':
    app.run(port=5001)