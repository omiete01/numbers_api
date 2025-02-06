# this is an api that delivers fun facts about mathematical numbers

import requests
from flask import Flask, request, jsonify
from sympy import isprime
from waitress import serve

# creates a Flask application instance to determine the root path of the application
app = Flask(__name__)

# checking for prime number using sympy library
def is_prime(number):

    if isprime(number):
        return True
    else:
        return False

# checking if number is a perfect number    
def is_perfect(number):
    if number < 1:
        return False
    
    perfect = sum ([num for num in range(1, number) if number % num == 0])
    if perfect == number:
        return True
    else:
        return False
    
# adds the numbers together individually
def digit_sum(number):
    return (sum (int(digit) for digit in str(abs(int(number)))))

# checking if the number is an armstrong number
def is_armstrong(number):
    num_str = str(abs(int(number)))
    num = len(num_str)
    return sum(int(digit)**num for digit in num_str) == abs(number)

def fun_fact(number):

    # makes a GET request to the numbers API, returns an error message if status code does not return 200
    response = requests.get(f"http://numbersapi.com/{number}/math?json")
    response.raise_for_status()
    fun_fact = response.json()

    # extracts the text content of the response
    return fun_fact.get("text")

# defines a route for the endpoint which will handle GET requests
@app.route("/api/classify-number", methods=["GET"])

def classify_number():
    # allows users to pass a number as parameter when making a request to the /number-info endpoint
    number = request.args.get("number")

    # returns a json response if the number parameter is not provided
    if not(number):
        return jsonify({"error": "no number provided"}), 400

    # if number conversion to integer fails, returns a json response with an error message
    try:
        number = int(number)
    except ValueError:
        return jsonify({"error": "invalid number"}), 400
    
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    properties.append("even" if number % 2 == 0 else "odd")

    # returns a json response containing the result of the functions on the number
    try:
        output = {
            "number": number,
            "is_prime": is_prime(number),
            "is_perfect": is_perfect(number),
            "digit_sum": digit_sum(number),
            "fun_fact": fun_fact(number),
            "properties": properties
        }
        
        return jsonify(output), 200
    except Exception as e:
        return jsonify({
            "number": "alphabet",
            "error": True
        }), 400

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000, threads=2)
