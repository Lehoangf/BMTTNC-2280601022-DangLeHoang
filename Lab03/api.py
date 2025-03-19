from flask import Flask, request, jsonify
from cipher.rsa.rsa_cipher import RSACipher
from cipher.ecc.ecc_cipher import ECCCipher

app = Flask(__name__)

rsa_cipher = RSACipher()

def caesar_encrypt(plain_text, key):
    key = int(key)
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift + key) % 26 + shift)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(cipher_text, key):
    return caesar_encrypt(cipher_text, -int(key))

@app.route('/api/caesar/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    plain_text = data.get("plain_text", "")
    key = data.get("key", 0)
    if not plain_text or not key:
        return jsonify({"error": "Missing plain_text or key"}), 400
    
    encrypted_message = caesar_encrypt(plain_text, key)
    return jsonify({"encrypted_message": encrypted_message})

@app.route('/api/caesar/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    cipher_text = data.get("cipher_text", "")
    key = data.get("key", 0)
    if not cipher_text or not key:
        return jsonify({"error": "Missing cipher_text or key"}), 400
    
    decrypted_message = caesar_decrypt(cipher_text, key)
    return jsonify({"decrypted_message": decrypted_message})


@app.route('/api/rsa/generate_keys', methods=['GET'])
def rsa_generate_keys():
    rsa_cipher.generate_keys()
    return jsonify({'message': 'Keys generated successfully'})  # Fixed typo here

@app.route("/api/rsa/encrypt", methods=["POST"])
def rsa_encrypt():
    data = request.json
    message = data['message']
    key_type = data['key_type']
    private_key, public_key = rsa_cipher.load_keys()
    if key_type == 'private':
        key = private_key
    elif key_type == 'public':
        key = public_key
    else:
        return jsonify({'error': 'Invalid key type'})
    encrypted_message = rsa_cipher.encrypt(message, key)
    encrypted_hex = encrypted_message.hex()
    return jsonify({'encrypted_message': encrypted_hex})

@app.route("/api/rsa/decrypt", methods=["POST"])
def rsa_decrypt():
    data = request.json
    ciphertext_hex = data['ciphertext']
    print("Ciphertext received:", ciphertext_hex)
    key_type = data['key_type']
    private_key, public_key = rsa_cipher.load_keys()
    if key_type == 'public':
        key = public_key
    elif key_type == 'private':
        key = private_key
    else:
        return jsonify({'error': 'Invalid key type'})
    ciphertext = bytes.fromhex(ciphertext_hex)
    decrypted_message = rsa_cipher.decrypt(ciphertext, key)
    return jsonify({'decrypted_message': decrypted_message})

@app.route('/api/rsa/sign', methods=["POST"])
def rsa_sign_message():
    data = request.json
    message = data['message']
    private_key, public_key = rsa_cipher.load_keys()
    signature = rsa_cipher.sign(message, private_key)
    signature_hex = signature.hex()
    return jsonify({'signature': signature_hex})

@app.route('/api/rsa/verify', methods=["POST"])
def rsa_verify_signature():
    data = request.json
    message = data['message']
    signature_hex = data['signature']
    public_key, _ = rsa_cipher.load_keys()
    signature = bytes.fromhex(signature_hex)
    is_verified = rsa_cipher.verify(message, signature, public_key)
    return jsonify({'is_verified': is_verified})

ecc_cipher = ECCCipher()

@app.route('/api/ecc/generate_keys', methods=['GET'])
def ecc_generate_keys():
    ecc_cipher.generate_keys()
    return jsonify({'message': 'ECC keys generated successfully'})

@app.route('/api/ecc/sign', methods=["POST"])
def ecc_sign_message():
    data = request.json
    message = data['message']
    private_key,_ = ecc_cipher.load_keys()
    signature = ecc_cipher.sign(message, private_key)
    signature_hex = signature.hex()
    return jsonify({'signature': signature_hex})

@app.route('/api/ecc/verify', methods=["POST"])
def ecc_verify_signature():
    data = request.json
    message = data['message']
    signature_hex = data['signature']
    public_key,_ = ecc_cipher.load_keys()
    signature = bytes.fromhex(signature_hex)
    is_verified = ecc_cipher.verify(message, signature, public_key)
    return jsonify({'is_verified': is_verified})
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    
