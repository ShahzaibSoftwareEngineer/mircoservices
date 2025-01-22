from flask import Flask, redirect, url_for
import requests

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def users():
    response = requests.get('http://user-service:5000/users')
    return response.json()

@app.route('/products', methods=['GET'])
def products():
    response = requests.get('http://product-service:5001/products')
    return response.json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
