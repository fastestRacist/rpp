from flask import Flask, request, jsonify
import requests
import random


app = Flask(__name__)


@app.route('/number/', methods=['GET'])
def get_request():
    param = int(request.args.get('param', 1))
    random_number = random.randint(1, 10)
    operation = random.choice(['sum', 'sub', 'mul', 'div'])

    return jsonify({
        'number': param * random_number,
        'operation': operation
    })


@app.route('/number/', methods=['POST'])
def post_request():
    data = request.get_json()
    param = int(data.get('jsonParam', 1))
    random_number = random.randint(1, 10)
    operation = random.choice(['sum', 'sub', 'mul', 'div'])

    return jsonify({
        'number': param * random_number,
        'operation': operation
    })


@app.route('/number/', methods=['DELETE'])
def delete_request():
    random_number = random.randint(1, 10)
    operation = random.choice(['sum', 'sub', 'mul', 'div'])

    return jsonify({
        'number': random_number,
        'operation': operation
    })


def main():
    url = "http://127.0.0.1:5000/number/"

    results = []

    param = random.randint(1, 10)
    response = requests.get(url, params={"param": param})
    data = response.json()
    results.append(data)
    
    param = random.randint(1, 10)
    response = requests.post(
        url,
        json={"jsonParam": param},
        headers={"Content-Type": "application/json"}
    )
    data = response.json()
    results.append(data)

    response = requests.delete(url)
    data = response.json()
    results.append(data)

    result = results[0]["number"]

    for item in results[1:]:
        operation = item["operation"]
        number = item["number"]

        print(f"{result} {operation} {number}")

        if operation == 'sum':
            result = result + number
        elif operation == 'sub':
            result = result - number
        elif operation == 'mul':
            result = result * number
        elif operation == 'div':
            result = result / number

    print("Итоговый результат:", int(result))


if __name__ == '__main__':
    app.run(debug=True)