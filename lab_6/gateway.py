from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('http://localhost:5002/currencies')
    currencies_list = response.json()
    return render_template('index.html', currencies = currencies_list)

@app.route('/load', methods=['POST'])
def load_currency():
    data = {
        'currency_name': request.form['currency_name'],
        'rate': request.form['rate']
    }
    requests.post('http://localhost:5001/load', json = data)
    
    resp_data = requests.get('http://localhost:5002/currencies')
    return render_template('index.html', currencies = resp_data.json())

@app.route('/update_currency', methods=['POST'])
def update_currency():
    data = {
        'currency_name': request.form['currency_name'],
        'rate': request.form['rate']
    }
    requests.post('http://localhost:5001/update_currency', json = data)
    
    resp_data = requests.get('http://localhost:5002/currencies')
    return render_template('index.html', currencies = resp_data.json())

@app.route('/delete', methods=['POST'])
def delete_currency():
    data = {'currency_name': request.form['currency_name']}
    requests.post('http://localhost:5001/delete', json = data)
    
    resp_data = requests.get('http://localhost:5002/currencies')
    return render_template('index.html', currencies = resp_data.json())

@app.route('/convert', methods = ['GET'])
def convert_currency():
    c_name = request.args.get('currency_name')
    t_sum = request.args.get('total_sum')
    
    response = requests.get('http://localhost:5002/convert', params = {
        'currency_name': c_name, 
        'total_sum': t_sum
    })
    
    result = response.json().get('result')
    
    resp_data = requests.get('http://localhost:5002/currencies')
    
    return render_template('index.html', 
                           currencies = resp_data.json(), 
                           conversion_result = result, 
                           curr_name = c_name)

if __name__ == '__main__':
    app.run(port=5000)