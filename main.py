from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

# Global Variables
user_id = "john_doe_17091999"
email = "john@xyz.com"
roll_number = "ABCD123"

# POST method route
@app.route('/bfhl', methods=['POST'])
def bfhl_post():
    try:
        data = request.json.get('data', [])
        if not isinstance(data, list):
            raise ValueError("Invalid input data format")

        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        lower_case_alphabets = [char for char in alphabets if char.islower()]

        highest_lowercase = max(lower_case_alphabets) if lower_case_alphabets else ""

        response = {
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else []
        }

    except Exception as e:
        response = {
            "is_success": False,
            "message": str(e)
        }

    return jsonify(response)

# GET method route
@app.route('/bfhl', methods=['GET'])
def bfhl_get():
    return jsonify({
        "operation_code": 1
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
