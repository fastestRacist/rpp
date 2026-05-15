from flask import Flask, request, jsonify
import psycopg2


app = Flask(__name__)


connection = psycopg2.connect(
    host = 'localhost',
    database = 'currencies',
    user = 'postgres',
    password = 'postgres'
)


@app.route('/convert', methods=['GET'])
def convert_currency():
    currency_name = request.args.get('currency_name')
    total_sum = float(request.args.get('total_sum'))

    cursor = connection.cursor()
    cursor.execute('SELECT rate FROM currencies WHERE currency_name = %s', (currency_name,))
    currency = cursor.fetchone()
    
    cursor.close()

    if currency is not None:
        result = total_sum * float(currency[0])
        return jsonify({'result': result})
    else:
        return jsonify({'result': 'Валюта не найдена'})


@app.route('/currencies', methods=['GET'])
def get_currencies():
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM currencies')

    currencies = cursor.fetchall()

    result = []

    for currency in currencies:
        result.append({
            'id': currency[0],
            'currency_name': currency[1],
            'rate': float(currency[2])
        })

    cursor.close()

    return jsonify(result)


if __name__ == '__main__':
    app.run(port=5002)