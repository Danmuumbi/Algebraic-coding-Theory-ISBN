from flask import Flask, request, jsonify

app = Flask(__name__)


def compute_isbn10_check_digit(isbn9):
    total = 0
    for i in range(9):
        digit = int(isbn9[i])
        total += digit * (i + 1)

    remainder = total % 11

    if remainder == 10:
        return "X"
    return str(remainder)


def validate_isbn10(isbn):
    if len(isbn) != 10:
        return False

    total = 0

    for i in range(9):
        if not isbn[i].isdigit():
            return False
        total += int(isbn[i]) * (i + 1)

    # Handle last digit
    if isbn[9] == 'X':
        total += 10 * 10
    elif isbn[9].isdigit():
        total += int(isbn[9]) * 10
    else:
        return False

    return total % 11 == 0


def compute_isbn13_check_digit(isbn12):
    total = 0

    for i in range(12):
        digit = int(isbn12[i])
        if i % 2 == 0:
            total += digit
        else:
            total += digit * 3

    remainder = total % 10
    check_digit = (10 - remainder) % 10

    return str(check_digit)


def validate_isbn13(isbn):
    if len(isbn) != 13 or not isbn.isdigit():
        return False

    check_digit = compute_isbn13_check_digit(isbn[:12])
    return isbn[-1] == check_digit


def convert_isbn10_to_isbn13(isbn10):
    if not validate_isbn10(isbn10):
        return None

    core = isbn10[:9]
    isbn12 = "978" + core
    check_digit = compute_isbn13_check_digit(isbn12)

    return isbn12 + check_digit



@app.route('/isbn10/check-digit', methods=['POST'])
def isbn10_check_digit():
    data = request.get_json()
    isbn9 = data.get("isbn")

    if not isbn9 or len(isbn9) != 9 or not isbn9.isdigit():
        return jsonify({"error": "Invalid ISBN-9 input"}), 400

    check_digit = compute_isbn10_check_digit(isbn9)

    return jsonify({
        "input": isbn9,
        "check_digit": check_digit
    })


@app.route('/isbn10/validate', methods=['POST'])
def isbn10_validate():
    data = request.get_json()
    isbn = data.get("isbn")

    if not isbn:
        return jsonify({"error": "ISBN required"}), 400

    is_valid = validate_isbn10(isbn)

    return jsonify({
        "input": isbn,
        "valid": is_valid
    })


@app.route('/isbn10/to-isbn13', methods=['POST'])
def isbn10_to_isbn13():
    data = request.get_json()
    isbn10 = data.get("isbn")

    if not isbn10:
        return jsonify({"error": "ISBN required"}), 400

    converted = convert_isbn10_to_isbn13(isbn10)

    if not converted:
        return jsonify({"error": "Invalid ISBN-10"}), 400

    return jsonify({
        "input": isbn10,
        "isbn13": converted
    })


@app.route('/isbn13/validate', methods=['POST'])
def isbn13_validate():
    data = request.get_json()
    isbn = data.get("isbn")

    if not isbn:
        return jsonify({"error": "ISBN required"}), 400

    is_valid = validate_isbn13(isbn)

    return jsonify({
        "input": isbn,
        "valid": is_valid
    })

if __name__ == '__main__':
    app.run(debug=True)
