from flask import Flask, render_template, request, jsonify

from sympy import (
    symbols,
    Matrix,
    sympify,
    simplify,
    sin,
    cos,
    tan,
    exp,
    log,
    sqrt,
    Abs,
    factor,
    cancel
)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():

    data = request.json

    try:
        n = int(data['num_variables'])

        if n <= 0:
            return jsonify({
                'error': 'Number of variables must be positive.'
            })

    except:
        return jsonify({
            'error': 'Invalid number of variables.'
        })

    theta_choice = data['theta_choice'].lower()

    variables = []

    if theta_choice == 'yes':

        if n == 1:
            variables = ['theta']

        else:
            variables.append('theta')

            for i in range(1, n):
                variables.append(f'x{i}')

    else:

        for i in range(1, n + 1):
            variables.append(f'x{i}')

    app.run(debug=True)
