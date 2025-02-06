# A Number Classification Flask API - HNG DevOps Task 1

This flask API classifies numbers based on their mathematical properties like prime, perfect, Armstrong, digit sum, even/odd and fun fact of the number.

The API utilizes external resources to obtain the fun fact by calling [Numbers API](http://numbersapi.com/#42)

## Features

1. Accepts GET requests with a number parameter
2. Classifies numbers as armstrong, perfect, even/odd, prime numbers
3. Returns digit sums and fun fact about the number
4. Returns responses in JSON format
5. Handles CORS to be accessible from different origin
6. Hosted on Render for public accessibility
7. Handles invalid input with appropriate error message
8. API endpoint: GET /api/classify-number?number=

## Installation

1. Clone the repository: 
   `git clone https://github.com/omiete01/numbers_api.git` `cd numbers_api`
2. Create a virtual environment: 
   `python3 -m venv venv`
   `source venv/bin/activate`  # On Windows: venv\Scripts\activate
3. Install the dependencies: 
   `pip3 install -r requirements.txt`
4. Run the application locally: 
   `waitress-serve --listen=0.0.0.0:5000 numbers_api:app`

## API Usage

Open your browser and go to http://127.0.0.1:5000//api/classify-number?number=371

✅ Success Response (200 OK):
{
    "digit_sum": 11,
    "fun_fact": "371 is a narcissistic number.",
    "is_perfect": false,
    "is_prime": false,
    "number": 371,
    "properties": [
        "armstrong",
        "odd"
    ]
}

❌ Error Response (400 Bad Request):
{ "number": "alphabet", "error": true }