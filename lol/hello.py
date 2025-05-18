from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine the base ASCII value (a=97, A=65)
            base = ord('a') if char.islower() else ord('A')
            # Apply the shift
            if encrypt:
                shifted = (ord(char) - base + shift) % 26
            else:
                shifted = (ord(char) - base - shift) % 26
            # Convert back to character
            result += chr(base + shifted)
        else:
            result += char
    return result

@app.route('/')
def index():
    return render_template('ceasers_cypher.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    text = data.get('text', '')
    shift = int(data.get('shift', 3))
    result = caesar_cipher(text, shift, True)
    return jsonify({'result': result})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()
    text = data.get('text', '')
    shift = int(data.get('shift', 3))
    result = caesar_cipher(text, shift, False)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
